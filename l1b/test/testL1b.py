# import required functions
from common.io.writeToa import readToa
from numpy import abs, mean, std
import matplotlib.pyplot as plt
# Load data from files
toa0_ref = readToa(r"C:\EODP_all\EODP-TS-L1B\output", r"l1b_toa_VNIR-0.nc")
toa0_own = readToa(r"C:\EODP_all\EODP-TS-L1B\myoutputs", r"l1b_toa_VNIR-0.nc")

toa1_ref = readToa(r"C:\EODP_all\EODP-TS-L1B\output", r"l1b_toa_VNIR-1.nc")
toa1_own = readToa(r"C:\EODP_all\EODP-TS-L1B\myoutputs", r"l1b_toa_VNIR-1.nc")

toa2_ref = readToa(r"C:\EODP_all\EODP-TS-L1B\output", r"l1b_toa_VNIR-2.nc")
toa2_own = readToa(r"C:\EODP_all\EODP-TS-L1B\myoutputs", r"l1b_toa_VNIR-2.nc")

toa3_ref = readToa(r"C:\EODP_all\EODP-TS-L1B\output", r"l1b_toa_VNIR-3.nc")
toa3_own = readToa(r"C:\EODP_all\EODP-TS-L1B\myoutputs", r"l1b_toa_VNIR-3.nc")

# 3-sigma limit
diff0 = abs(toa0_ref - toa0_own)/toa0_ref * 100
mean0 = mean(diff0)
stdv0 = std(diff0)
sig30 = mean0 + 3*stdv0

diff1 = abs(toa1_ref - toa1_own)/toa1_ref * 100
mean1 = mean(diff1)
stdv1 = std(diff1)
sig31 = mean1 + 3*stdv1

diff2 = abs(toa2_ref - toa2_own)/toa2_ref * 100
mean2 = mean(diff2)
stdv2 = std(diff2)
sig32 = mean2 + 3*stdv2

diff3 = abs(toa3_ref - toa3_own)/toa3_ref * 100
mean3 = mean(diff3)
stdv3 = std(diff3)
sig33 = mean3 + 3*stdv3

# <0.01% outside 3-sigma
print('\nTEST L1B START\n')
ok = True
if sig30 >= 0.0001:
    print(f'FAIL: 3-sigma for channel 0 is {sig30:.5f}, expected less than 1e-4')
    ok = False
else:
    print(f'PASS: 3-sigma for channel 0 is {sig30:.5f}')

if sig31 >= 0.0001:
    ok = False
    print(f'FAIL: 3-sigma for channel 1 is {sig31:.5f}, expected less than 1e-4')
else:
    print(f'PASS: 3-sigma for channel 1 is {sig31:.5f}')

if sig32 >= 0.0001:
    print(f'FAIL: 3-sigma for channel 2 is {sig32:.5f}, expected less than 1e-4')
    ok = False
else:
    print(f'PASS: 3-sigma for channel 2 is {sig32:.5f}')

if sig33 >= 0.0001:
    print(f'FAIL: 3-sigma for channel 3 is {sig33:.5f}, expected less than 1e-4')
    ok = False
else:
    print(f'PASS: 3-sigma for channel 3 is {sig33:.5f}')

if ok:
    print(f'\nSUCCESS: all channels passed')
else:
    print(f'ERROR: Some channels did not pass the test')


# Plots to verify behaviour
## No EQ, EQ & ISRF comparison -- channel 0 as examples
isrf0 = readToa(r"C:\EODP_all\EODP-TS-ISM\output", r"ism_toa_isrf_VNIR-0.nc")
toa0_neq = readToa(r"C:\EODP_all\EODP-TS-L1B\neq", r"l1b_toa_VNIR-0.nc")

plt.plot(toa0_neq[50,:])
plt.plot(toa0_own[50,:])
plt.plot(isrf0[50,:])
plt.grid()
plt.legend(['Not equalised', 'Equalised', 'After ISRF'])
plt.xlabel('ACT pixel (N/A)')
plt.ylabel('TOA (mW m-2 sr-1)')
plt.show()