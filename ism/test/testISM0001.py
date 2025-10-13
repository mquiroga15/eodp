from common.io.writeToa import readToa
from numpy import mean, std, isnan
from numpy import abs as npabs

print('\nTEST ISM START\n')
all_ok = True

ok = True
print('Spectral Filter test')
for band in range(4):
    toa_ref = readToa(r"C:\EODP_all\EODP-TS-ISM\output", r"ism_toa_isrf_VNIR-"+str(band)+".nc")
    toa_own = readToa(r"C:\EODP_all\EODP-TS-ISM\myoutput", r"ism_toa_isrf_VNIR-"+str(band)+".nc")
    # 3-sigma limit
    diff = npabs(toa_ref - toa_own) * 100
    avrg = mean(diff)
    stdv = std(diff)
    sig3 = avrg + 3*stdv
    if sig3 >= 0.0001:
        print(f'FAIL: 3-sigma for channel {band} is {sig3:.5f}, expected less than 1e-4')
        ok = False
    else:
        print(f'PASS: 3-sigma for channel {band} is {sig3:.5f}')
if ok:
    print(f'\nSUCCESS: all channels passed the spectral filter test')
else:
    print(f'ERROR: Some channels did not pass the spectral filter test')
    all_ok = False

ok = True
print('MTF application test')
for band in range(4):
    toa_ref = readToa(r"C:\EODP_all\EODP-TS-ISM\output", r"ism_toa_optical_VNIR-"+str(band)+".nc")
    toa_own = readToa(r"C:\EODP_all\EODP-TS-ISM\myoutput", r"ism_toa_optical_VNIR-"+str(band)+".nc")
    # 3-sigma limit
    diff = npabs(toa_ref - toa_own)/toa_ref * 100
    diff = diff[~isnan(diff)]
    avrg = mean(diff)
    stdv = std(diff)
    sig3 = avrg + 3*stdv
    if sig3 >= 0.0001:
        print(f'FAIL: 3-sigma for channel {band} is {sig3:.5f}, expected less than 1e-4')
        ok = False
    else:
        print(f'PASS: 3-sigma for channel {band} is {sig3:.5f}')
if ok:
    print(f'\nSUCCESS: all channels passed the MTF application test')
else:
    print(f'ERROR: Some channels did not pass the MTF application test')
    all_ok = False

if all_ok:
    print('\nALL TESTS PASSED')
else:
    print('SOME TESTS HAVE FAILED')
