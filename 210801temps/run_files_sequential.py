#
#
#
import sys, os, shutil, glob
import numpy as np
import subprocess
from subprocess import PIPE
#
base_dir = os.getcwd()
exec = os.path.join(os.path.dirname(base_dir), 'lassi')
#
targ = 'targs'
dirs = glob.glob( os.path.join(base_dir, targ, "*") )
dirs = sorted(dirs)
#
for tdir in dirs:
    print(tdir)
    os.chdir(tdir)
    # ret_code = subprocess.run(run_command, shell=True)
    subprocess.run(exec, shell=True, stdout=PIPE, stderr=PIPE, text=True)
    os.chdir(base_dir)


