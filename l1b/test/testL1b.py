# plot the isrf vs l1b
from common.io.writeToa import readToa

toa = readToa(r"C:\EODP_all\EODP-TS-L1B\myoutputs", "l1b_toa_VNIR-" + band + ".nc")

toa0_ref = readToa("C:\EODP_all\EODP-TS-L1B\output", "l1b_toa_VNIR-0.nc")
toa0_own = readToa("C:\EODP_all\EODP-TS-L1B\myoutputs", "l1b_toa_VNIR-0.nc")
diff0 = abs(toa0_ref - toa3_tab)

toa1_ref = readToa("C:\EODP_all\EODP-TS-L1B\output", "l1b_toa_VNIR-1.nc")
toa1_own = readToa("C:\EODP_all\EODP-TS-L1B\myoutputs", "l1b_toa_VNIR-1.nc")
diff1 = abs(toa1_ref - toa1_own)

toa2_ref = readToa("C:\EODP_all\EODP-TS-L1B\output", "l1b_toa_VNIR-2.nc")
toa2_own = readToa("C:\EODP_all\EODP-TS-L1B\myoutputs", "l1b_toa_VNIR-2.nc")
diff2 = abs(toa2_ref - toa2_own)

toa3_ref = readToa("/Users/rubencorraliza/Documents/GitHub/EODP-TS-L1B/output/", "l1b_toa_VNIR-3.nc")
toa3_own = readToa("C:\EODP_all\EODP-TS-L1B\myoutputs", "l1b_toa_VNIR-3.nc")
diff3 = abs(toa3_ref - toa3_own)

