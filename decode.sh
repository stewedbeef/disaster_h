#!/bin/sh
#SBATCH --ntasks=1
#SBATCH --time=4:00:00
#SBATCH --mem-per-cpu=4G
#SBATCH --array=1-96

BASE=./IMMA/IMMA1_R3.0.2_

YRS=(2015 2016 2017 2018 2019 2020 2021 2022)
MNS=(01 02 03 04 05 06 07 08 09 10 11 12)

FILES=()

for y in ${YRS[@]}
do
	for m in ${MNS[@]}
	do
		FILES+=("$BASE$y-$m")
	done
done

echo "Executing execution"
./decode ${FILES[$SLURM_ARRAY_TASK_ID]} "${FILES[$SLURM_ARRAY_TASK_ID]}.out"
echo "Finished"
