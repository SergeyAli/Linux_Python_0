# #!/bin/bash
# result=$(cat /etc/os-release)
# if [[ $result == *"22.04.1"* && *"jammy"* && $? == 0 ]];
# then echo "SUCCESS"
# else echo "FAIL"
# fi

import subprocess

def script_1():
    result = subprocess.run("cat /etc/os-release", shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    print(type(result))
    print(result.stdout)
    print(result.returncode)
    print(result.stderr)
    if ("jammy" in result.stdout  and "22.04.1" in result.stdout  and result.returncode == 0):
        print("SUCCESS")
    else:
        print("FAIL")

script_1()
