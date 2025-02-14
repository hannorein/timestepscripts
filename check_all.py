import sys
import rebound
import math
tmax = 5e9*math.pi*2.0
N = 80
for dt in [6, 12, 24, 48]:
    s = 0.0
    for i in range(N):
        try:
            sa = rebound.Simulationarchive("/scratch/rein/out_%.1e/out_%.1e_%04d.bin"%(dt, dt, i))
            prog = sa.tmax/tmax*100
            s += prog
        except:
            pass
    try:
        sim = sa[-1]
        secleft = max(0.0,(1.-s/N/100.0)*sim.walltime/sim.t*tmax)
    except:
        secleft = math.nan
    print("%.1e avg  %6.2f%%  (%5.2fh left) "%(dt, s/N, secleft/60/60))

