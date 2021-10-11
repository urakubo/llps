#
# https://stackoverflow.com/questions/58031373/run-process-after-process-in-a-queue-using-python
#
import sys, os, shutil, glob
import time
import numpy as np
from subprocess import Popen, PIPE
from concurrent.futures import ThreadPoolExecutor
#
base_dir = os.getcwd()
exec = os.path.join(os.path.dirname(base_dir), 'lassi')
#
targ = 'targs'
dirs = glob.glob( os.path.join(base_dir, targ, "*") )
dirs = sorted(dirs)
cmds = [[exec, "-k", os.path.join(dir, "param.key") ] for dir in dirs]
#
#print(cmds)
#sys.exit()
#
def exec_(cmd):
    print(' '.join(cmd))
    proc = Popen(cmd, stdout=PIPE, stderr=PIPE)
    stdout, stderr = proc.communicate()
    #print(stdout, stderr)
#
with ThreadPoolExecutor(max_workers=4) as executor:
    start = time.time()
    futures = executor.map(exec_, cmds)
    for future in futures:
        pass
    end = time.time()
    elapsed = time.strftime("%H:%M:%S", time.gmtime(end - start))
    print(f'Took: {elapsed}')

