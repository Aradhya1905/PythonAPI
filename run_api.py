import os
import subprocess

# Activate Conda environment
activate_cmd = 'conda activate facial_analysis_env'
# Start Uvicorn server
uvicorn_cmd = 'python -m uvicorn main:app --reload --port 9000'

# Combine the commands in one shell call
full_command = f"{activate_cmd} && {uvicorn_cmd}"

# Run the combined command in the shell
subprocess.run(full_command, shell=True)
