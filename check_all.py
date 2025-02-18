import sys
import rebound
import math
import warnings
warnings.filterwarnings("ignore")

tmax = 5e9*math.pi*2.0
N = 80
for a in range(1,len(sys.argv)):
    if "wh" in sys.argv[a]:
        dt = float(sys.argv[a][2:])
        wh = "_whfast"
    else:
        dt = float(sys.argv[a])
        wh = ""
    s = 0.0
    for i in range(N):
        try:
            sa = rebound.Simulationarchive("/scratch/rein/out%s_%.1e/out_%.1e_%04d.bin"%(wh, dt, dt, i))
            prog = sa.tmax/tmax*100
            s += prog
        except:
            pass
    try:
        sim = sa[-1]
        secleft = max(0.0,(1.-s/N/100.0)*sim.walltime/sim.t*tmax)
    except:
        secleft = math.nan
    print("%.1e avg  %6.2f%%  (%5.2fh left) %s"%(dt, s/N, secleft/60/60, wh))

