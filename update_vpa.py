import os
import yaml

# Load environment variables
min_cpu = os.getenv("MIN_CPU", "300m")
max_cpu = os.getenv("MAX_CPU", "1")
min_memory = os.getenv("MIN_MEMORY", "300Mi")
max_memory = os.getenv("MAX_MEMORY", "1Gi")

# Load the VPA YAML file
vpa_file_path = 'vpa.yml'

with open(vpa_file_path, 'r') as file:
    vpa_data = yaml.load(file, Loader=yaml.FullLoader)

print(vpa_data)

# # Update minAllowed values
# vpa_data['spec']['resourcePolicy']['containerPolicies'][0]['minAllowed']['memory'] = min_memory
# vpa_data['spec']['resourcePolicy']['containerPolicies'][0]['minAllowed']['cpu'] = min_cpu

# # Update maxAllowed values
# vpa_data['spec']['resourcePolicy']['containerPolicies'][0]['maxAllowed']['memory'] = max_memory
# vpa_data['spec']['resourcePolicy']['containerPolicies'][0]['maxAllowed']['cpu'] = max_cpu

# # Save the updated YAML file
# with open(vpa_file_path, 'w') as file:
#     yaml.safe_dump(vpa_data, file)

# print(f"Updated {vpa_file_path} with new CPU and memory limits.")
