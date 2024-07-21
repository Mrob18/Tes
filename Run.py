import yaml

with open('LM_Windows_Github_RDP.yml', 'r') as f:
    data = yaml.safe_load(f)

for command in data['commands']:
    subprocess.run(command, shell=True)
