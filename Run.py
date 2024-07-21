import subprocess
import yaml

# Load the YAML file
with open('LM_Windows_Github_RDP.yml', 'r') as f:
    workflow = yaml.safe_load(f)

# Run each step in the workflow
for step in workflow['jobs']['build']['steps']:
    print(f"Running step: {step['name']}")
    command = step['run']
    print(f"Command: {command}")
    # Use the 'bash' shell to run the command
    subprocess.run(['bash', '-c', command])
