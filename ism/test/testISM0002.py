from common.io.writeToa import readToa
from numpy import mean, std, isnan
from numpy import abs as npabs

print('\nTEST ISM START\n')
all_ok = True

fail = []
saturated = []
ok = True
print('Final TOA test')
for band in range(4):
    saturated_in_band = 0
    toa_ref = readToa(r"C:\EODP_all\EODP-TS-ISM\output", r"ism_toa_VNIR-"+str(band)+".nc")
    toa_own = readToa(r"C:\EODP_all\EODP-TS-ISM\myoutput", r"ism_toa_VNIR-"+str(band)+".nc")
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

    for pixel in toa_own.flatten():
        if pixel >= 4095:
            saturated_in_band += 1
    saturated.append(saturated_in_band/(toa_own.shape[0]*toa_own.shape[1])*100)

if ok:
    print(f'\nSUCCESS: all channels passed the final TOA test')
else:
    print(f'ERROR: Some channels did not pass the final TOA test:')
    print(f'The following bands have failed: {fail}')
    all_ok = False

print(f'\nSaturated pixels per band (%):')
print(saturated)
