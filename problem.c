#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <sched.h>
#include <stdbool.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>
#include "rebound.h"

int main(int argc, char* argv[]) {
    if(argc != 3) {
        printf("./rebound dt id\n");
        exit(1);
    }
    double dt = atof(argv[1]);
    int id = atoi(argv[2]);
    
    char directory[1024];
    char fullfilename[1024];
    sprintf(directory,    "/scratch/rein/out_%.1e",dt);
    sprintf(fullfilename, "/scratch/rein/out_%.1e/out_%.1e_%04d.bin",dt,dt,id);
    struct reb_simulationarchive* sa = reb_simulationarchive_create_from_file(fullfilename);
    struct reb_simulation* r = NULL;
    if (sa){
        r = reb_simulation_create_from_simulationarchive(sa,-1);
        reb_simulationarchive_free(sa);
    }else{
        printf("Can not open snapshots. Starting with initial conditions.\n");
        r = reb_simulation_create_from_file("initial.bin", 0);
        r->particles[3].x += 1e-13*(double)(id);
        reb_simulation_move_to_com(r);
    }
    printf("Current simulation time %.6f Gyr.\n", 1e-9*r->t/(M_PI*2.0));
    
    r->dt = dt/365.25*2*M_PI;
    r->exact_finish_time = 0;
    r->force_is_velocity_dependent = 0; 
    r->integrator = REB_INTEGRATOR_WHFAST512;
    r->ri_whfast512.gr_potential = 1;

    struct stat st = {0};
    if (stat(directory, &st) == -1) {
        mkdir(directory, 0700);
        printf("Created directory `%s`.\n", directory);
    }
    printf("Ouput file `%s`.\n", fullfilename);
    reb_simulation_save_to_file_interval(r, fullfilename, 5e6*2.0*M_PI);

    printf("Starting integration.\n");
    reb_simulation_integrate(r, 5e9*2.0*M_PI);
    return EXIT_SUCCESS;
}
