import os
print('s')
print('s')
print('s')
a = os.popen('stty size', 'r').read()
#rows, columns = os.popen('stty size', 'r').read().split()
print a
import sys
sys.stdout.write(' %d/%d ' % (1, 1))