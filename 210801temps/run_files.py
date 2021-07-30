#
#
#
import sys, os, shutil, glob
import numpy as np
import subprocess
#
base_dir = os.getcwd()
targ = 'targs'
run_command =['qsub', "exe.sh"]
#
dirs = glob.glob( os.path.join(base_dir, targ, "*") )
dirs = sorted(dirs)
#
for tdir in dirs:
    print(tdir)
    os.chdir(tdir)
    # ret_code = subprocess.run(run_command, shell=True)
    subprocess.run(run_command)
    os.chdir(base_dir)

    
