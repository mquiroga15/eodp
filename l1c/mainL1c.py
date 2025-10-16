
# MAIN FUNCTION TO CALL THE L1C MODULE

from l1c.src.l1c import l1c

# Directory - this is the common directory for the execution of the E2E, all modules
auxdir = r"C:\EODP_all\eodp\auxiliary"
# GM dir + L1B dir
indir = r"C:\EODP_all\EODP-TS-L1C\input\gm_alt100_act_150,C:\EODP_all\EODP-TS-L1C\input\l1b_output"
outdir = r"C:\EODP_all\EODP-TS-L1C\myoutputs"

# Initialise the ISM
myL1c = l1c(auxdir, indir, outdir)
myL1c.processModule()
