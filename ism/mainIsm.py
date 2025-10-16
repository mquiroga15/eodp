
# MAIN FUNCTION TO CALL THE ISM MODULE

from ism.src.ism import ism

# Directory - this is the common directory for the execution of the E2E, all modules
auxdir = r"C:\EODP_all\eodp\auxiliary"
#indir = r"C:\EODP_all\EODP-TS-ISM\input\gradient_alt100_act150" # small scene
indir = r"C:\EODP_all\EODP-TS-E2E\sgm_out"
outdir = r"C:\EODP_all\EODP-TS-E2E\myISMoutput"

# Initialise the ISM
myIsm = ism(auxdir, indir, outdir)
myIsm.processModule()
