#!/usr/bin/python3

import configparser
import sys
import subprocess
import re

config = configparser.ConfigParser()
config.readfp(open(r'./config.ini'))

#print(config.get("CPU INFO", "test_enable"))
if config.get("CPU INFO", "test_enable") != "enable":
    sys.exit(1)
    
print("===Start to check CPU info===")

def show_proc_cpuinfo(proc_nums, target):
    current_proc = 0
    data = []
    result = subprocess.getoutput("cat /proc/cpuinfo")
    result = result.splitlines()

    for line in result:
        pattern = "^"+ target

        if re.match(pattern, line):
            tmp = line.split(":")
            list.append(data, tmp[1].strip())
            current_proc += 1
            
    if current_proc == proc_nums:
        return data
    else:
        print("!!Error: current processor numbers is NOT consistent\
with configured numbers")
        return None

print("[Processor numbers]")
proc_nums = subprocess.getoutput("cat /proc/cpuinfo | grep ^processor | wc -l")
conf_proc_nums = config.get("CPU INFO", "processor_num")
if conf_proc_nums == proc_nums:
    print("PASS. The number of Avialible processor:", proc_nums, "is consistent with \
Configured processor:", conf_proc_nums)
else:
    print("FAIL. The number of Avialible processor:", proc_nums, "is NOT consistent with \
Configured processor:", conf_proc_nums)
    sys.exit(1)
print()

for index in range(0, int(proc_nums)):
    print("[Vendor ID #", index, "]", sep='')
    ven_id = show_proc_cpuinfo(int(proc_nums), "vendor_id")[index]
    conf_ven_id = config.get("CPU INFO", "vendor_id_"+str(index))
    if ven_id == conf_ven_id:
        print("PASS. Vendor ID:", ven_id, "is correct")
    else:
        print("FAIL. Vendor ID:", ven_id, "!= Conf vendor ID:", conf_ven_id) 
    print()

    print("[Model Name #", index, "]", sep='')
    model = show_proc_cpuinfo(int(proc_nums), "model name")[index]
    conf_model = config.get("CPU INFO", "model_name_"+str(index))
    if model == conf_model:
        print("PASS. Model name:", model, "is correct")
    else:
        print("FAIL. Model name:", model, "!= Conf model name:", conf_model)
    print()
    
    print("[CPU frequency #", index, "]", sep='')
    freq = show_proc_cpuinfo(int(proc_nums), "cpu MHz")[index]
    conf_freq = config.get("CPU INFO", "cpu_MHz_"+str(index))
    if freq == conf_freq:
        print("PASS. CPU frequency", freq, "MHz is correct")
    else:
        print("FAIL. CPU frequency:", freq, "MHz != Conf CPU frequency:", conf_freq, "MHz")
    print()
    
    print("[CPU core #", index, "]", sep='')
    core = show_proc_cpuinfo(int(proc_nums), "cpu cores")[index]
    conf_core = config.get("CPU INFO", "cores_"+str(index))
    if freq == conf_freq:
        print("PASS. CPU cores", core, "is correct")
    else:
        print("FAIL. CPU cores:", core, "!= Conf CPU cores:", conf_core)
    print()
    


