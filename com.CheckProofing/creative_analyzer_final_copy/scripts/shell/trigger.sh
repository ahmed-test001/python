#!/bin/bash

cd ${PWD}/../..

export etl_name="comlink_data"

function process_summary()
{
        elapsed_time()
    {
        sseconds=$1
        eseconds=$2
        dt=$((eseconds - sseconds))
        ds=$((dt % 60))
        dm=$(((dt / 60) % 60))
        dh=$((dt / 3600))
        printf '%d:%02d:%02d' $dh $dm $ds
     }
    echo "Start Time: ${start_time}"
    end_time=$(date)
    end_seconds=$(date +%s)
    echo "End Time: ${end_time}"
    elapsed_time=$(elapsed_time $start_seconds $end_seconds)
    echo "Total Elapsed Time = $elapsed_time"
}

timestamp()
{
 date +%Y-%m-%d_%H%M%S
}

export start_time=$(date)
export start_seconds=$(date +%s)
export job_date_time=$(date +%Y-%m-%d_%H%M%S)

export app_dir=${PWD}
export scripts_dir=${PWD}/scripts
export python_dir=${scripts_dir}/python
export data_dir=${PWD}/data
export input_dir=${data_dir}/input
export output_dir=${data_dir}/output
export log_dir=${app_dir}/logs
#export log_file=${log_dir}/log_file.log
export log_file=${log_dir}/logfile'_'${job_date_time}'.log'


rm -f ${output_dir}/proof_files/*                   >>${log_file} 2>&1
rm -f ${output_dir}/proof_images/*                  >>${log_file} 2>&1
rm -f ${output_dir}/proof_reports/*                 >>${log_file} 2>&1

for path in `ls ${input_dir}/*.htm`
do
  export file_name=`basename ${path}`                                                                  >>${log_file} 2>&1
  #/Users/l.reddy/miniconda/envs/3.6/bin/python ${python_dir}/wrapper.py -i ${file_name}                >>${log_file} 2>&1
#  C:/Users/a.ferdous.CORP/Anaconda3/envs/com.CheckProofing/python.exe ${python_dir}/wrapper.py -i ${file_name}                >>${log_file} 2>&1
  C:/Users/a.ferdous.CORP/AppData/Local/Programs/Python/Python38/python ${python_dir}/wrapper.py -i ${file_name}                >>${log_file} 2>&1
done


#rm ${output_dir}/proof_files/*
#rm ${output_dir}/proof_images/*
#rm -f ${output_dir}/proof_reports/*
process_summary                                                               >> $log_file 2>&1

echo 'done'                                           >>${log_file} 2>&1
exit 0