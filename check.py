import sys
import rebound
import math
if len(sys.argv) != 2:
    exit
dt = float(sys.argv[1])
N = 80
s = 0.0
for i in range(N):
    sa = rebound.Simulationarchive("/scratch/rein/out_%.1e/out_%.1e_%04d.bin"%(dt, dt, i))
    prog = sa.tmax/(5e9*math.pi*2.0)*100
    s += prog
    print("%.1e %04d %.2f%%"%(dt, i, prog))
print("%.1e avg  %.2f%%"%(dt, s/N))

