#
#
#
import sys, os, shutil
import numpy as np
#
# Final temp: 0.3, 0.6, 1.2
#
# TEMP + 0.2
#
CaMKII     = [250, 500, 1000]
TEMP       = [0.3, 0.6, 1.2]
GluN       = 1500
DELTA_TEMP = 0.0
CaMKII_, TEMP_  = np.meshgrid(CaMKII, TEMP)
CaMKII_ = CaMKII_.reshape(-1)
TEMP_   = TEMP_.reshape(-1)
#
base_dir = os.getcwd()
targ = 'targs'
struct_source_file = "structure_source.prm"
struct_targ_file   = "structure.prm"
energy_file        = "energy.prm"
param_source_file  = "param_source.key"
param_targ_file    = "param.key"
qsub_file          = "exe.sh"
#
for i, (CKII,T) in enumerate(zip(CaMKII_, TEMP_)):

    ##
    subdir = str(i).zfill(3)[-3:]
    ## If you make control dirs, uncomment the follows:
    #subdir = 'c' + str(i).zfill(3)[-3:]
    #energy_file = "energy_ctl.prm"

    print(subdir)
    print('CaMKII: ', str(CKII), '; T: ', str(T), '; GluN2B: ', str(GluN))

    ## Make dir
    targ_dir = os.path.join(base_dir, targ, subdir)
    os.makedirs(targ_dir, exist_ok=True)

    ## structure file
    with open(struct_source_file) as f:
        data_lines=f.read()
    data_lines = data_lines.replace("## CaMKII_NUM ##", str(CKII))
    data_lines = data_lines.replace("## GluN2B_NUM ##", str(GluN))
    with open(os.path.join(targ_dir, struct_targ_file), mode="w") as f:
        f.write(data_lines)

    ## param file
    with open(param_source_file) as f:
        data_lines=f.read()
    struct_file = os.path.join(targ_dir, struct_targ_file)
    output_prefix = os.path.join(targ_dir, "SMol")
    energy_file = os.path.join(base_dir, energy_file)
    data_lines = data_lines.replace("## STRUCT_FILE ##", struct_file)
    data_lines = data_lines.replace("## ENERGY_FILE ##", energy_file)
    data_lines = data_lines.replace("## MC_DELTA_TEMP ##"   , str(DELTA_TEMP))
    data_lines = data_lines.replace("## MC_TEMP ##"   , str(T))
    data_lines = data_lines.replace("## OUTPUT_DIR_PREFIX ##", output_prefix)
    with open(os.path.join(targ_dir, param_targ_file), mode="w") as f:
        f.write(data_lines)
    
    ## qsub file
    with open(os.path.join(targ_dir, qsub_file), mode="w") as f:
        f.write('#!/bin/bash\n')
        f.write('#PBS -N '+ subdir + ' \n')
        f.write('#PBS -q bio\n')
        f.write('cd $PBS_O_WORKDIR\n')
        f.write(os.path.join(os.path.dirname(base_dir), 'lassi')+'\n')
