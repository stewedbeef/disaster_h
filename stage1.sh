#!/bin/bash
#
#SBATCH --job-name=prep_data_stage_1
#
#SBATCH --ntasks=1
#SBATCH --time=4:00:00
#SBATCH --mem-per-cpu=32G
#
#SBATCH --array=1-96

BASE=/hb/home/aesymons/hurr_data/ICOADS/IMMA1_R3.0.2_

YRS=(2015 2016 2017 2018 2019 2020 2021 2022)
MNS=(01 02 03 04 05 06 07 08 09 10 11 12)

FILES=()

for yr in ${YRS[@]}; do
	for mn in ${MNS[@]}; do 
		FILES+=("$BASE$yr-$mn.gz")
	done
done

echo "imma_test.py..."
python3 imma_test.py -d ${FILES[$SLURM_ARRAY_TASK_ID]}
echo "done!"
