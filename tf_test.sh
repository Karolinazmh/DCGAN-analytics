#!/bin/sh
#PBS -q h-regular
#PBS -l select=1:mpiprocs=1:ompthreads=1
#PBS -W group_list=gj16
#PBS -l walltime=20:00:00 
cd $PBS_O_WORKDIR
. /etc/profile.d/modules.sh
module load tensorflow
python main.py --dataset celebA --input_height=108 --train --crop
