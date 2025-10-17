from common.io.writeToa import readToa
from numpy import mean, std, isnan
from numpy import abs as npabs

print('\nTEST E2E START\n')
all_ok = True

fail = []
ok = True
print('ISM-E2E test')
for band in range(4):
    saturated_in_band = 0
    toa_ref = readToa(r"C:\EODP_all\EODP-TS-E2E\ism_out", r"ism_toa_VNIR-"+str(band)+".nc")
    toa_own = readToa(r"C:\EODP_all\EODP-TS-E2E\myISMoutput", r"ism_toa_VNIR-"+str(band)+".nc")
    # 3-sigma limit
    diff = npabs(toa_ref - toa_own)/toa_ref * 100
    avrg = mean(diff)
    stdv = std(diff)
    sig3 = avrg + 3*stdv
    if sig3 >= 0.0001:
        print(f'FAIL: 3-sigma for channel {band} is {sig3:.5f}, expected less than 1e-4')
        ok = False
        fail.append(band)
    else:
        print(f'PASS: 3-sigma for channel {band} is {sig3:.5f}')

if ok:
    print(f'\nSUCCESS: all channels passed the ISM-E2E test')
else:
    print(f'ERROR: Some channels did not pass the ISM-E2E test:')
    print(f'The following bands have failed: {fail}')
    all_ok = False

fail = []
ok = True
print('L1B-E2E test')
for band in range(4):
    saturated_in_band = 0
    toa_ref = readToa(r"C:\EODP_all\EODP-TS-E2E\l1b_out", r"l1b_toa_VNIR-"+str(band)+".nc")
    toa_own = readToa(r"C:\EODP_all\EODP-TS-E2E\myL1Boutputs", r"l1b_toa_VNIR-"+str(band)+".nc")
    # 3-sigma limit
    diff = npabs(toa_ref - toa_own)/toa_ref * 100
    avrg = mean(diff)
    stdv = std(diff)
    sig3 = avrg + 3*stdv
    if sig3 >= 0.0001:
        print(f'FAIL: 3-sigma for channel {band} is {sig3:.5f}, expected less than 1e-4')
        ok = False
        fail.append(band)
    else:
        print(f'PASS: 3-sigma for channel {band} is {sig3:.5f}')

if ok:
    print(f'\nSUCCESS: all channels passed the L1B-E2E test')
else:
    print(f'ERROR: Some channels did not pass the L1B-E2E test:')
    print(f'The following bands have failed: {fail}')
    all_ok = False

if all_ok:
    print('\nFull PASS: E2E tests completed')
else:
    print('ERROR: Check console output, some tests have failed')
