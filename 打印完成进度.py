import sys
import time

for i in range(10000):
    percent = 1.0 * i / 10000 * 100
    print('complete percent:' + str(percent) + '%',)
    sys.stdout.write("\r")
    time.sleep(0.1)