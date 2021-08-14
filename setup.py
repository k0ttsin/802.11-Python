####not to run
####Just sample code for 802.11 Python PDF
from subprocess import *
from pathlib import Path
from sys import exit

VENV_NAME='.venv'
REQUIREMENTS='requirements.txt'


#############################Check Python3 is Installed?###############################
check_python=run(['which','python3'],capture_output=True,text=True)

if check_python.returncode != 0:
    raise OSError("Python3 is not installed")
    exit(1)

python3_path=check_python.stdout.strip()
print (f"Python3 Found at :{python3_path}")

#######################################################################################
#############################Install from requirements.txt#############################
create_venv=run([python3_path,'-m','venv',VENV_NAME],check=True)
if create_venv.returncode !=0:
    print (f"Can't Create {VENV_NAME}")
    exit(2)

pip_bin=f'{VENV_NAME}/bin/pip3'
if Path(REQUIREMENTS).exists():
    print (f"Requirements file '{REQUIREMENTS}' found")
    print ('Installing requirements')
    run([pip_bin,'install','-r',REQUIREMENTS])
    print ("Process Completed! Now you activate your environemnt with 'source .venv/bin/activate'")
    exit(0)
else:
    print (f"{REQUIREMENTS} Not Found !!")
