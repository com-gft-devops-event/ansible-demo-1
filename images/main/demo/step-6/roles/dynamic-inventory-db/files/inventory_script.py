#!/usr/bin/env python3

import subprocess
import json

def fetch_inventory():
    try:
        # Use subprocess to run ansible-vault decrypt command
        decrypt_command = "ansible-vault decrypt roles/dynamic-inventory-db/files/db-password.yml --output -"
        decrypt_result = subprocess.run(decrypt_command, shell=True, capture_output=True, text=True, check=True)
        
        # Extract PostgreSQL password from the decrypted vault content
        decrypted_content = decrypt_result.stdout.strip()
        postgres_password = decrypted_content
        
        # Execute psql command to fetch inventory data from the database
        psql_command = f"PGPASSWORD={postgres_password} psql -h database -p 5432 -U postgres -d postgres -c 'SELECT hostname, groups FROM hosts' -t -A"
        result = subprocess.run(psql_command, shell=True, capture_output=True, text=True, check=True, input='postgres\n')
        
        # Process the output into inventory dictionary
        inventory = {
            '_meta': {
                'hostvars': {}
            }
        }
        
        for line in result.stdout.splitlines():
            hostname, groups = line.strip().split('|')
            inventory['_meta']['hostvars'][hostname] = {'ansible_host': hostname}
            for group in groups.split(','):
                group = group.strip()
                if group not in inventory:
                    inventory[group] = {'hosts': []}
                inventory[group]['hosts'].append(hostname)
                
        print(json.dumps(inventory))
        
    except subprocess.CalledProcessError as e:
        print("Error: Command returned non-zero exit status:", e.returncode)
        print("Command output:", e.output)
        exit(1)
        
if __name__ == "__main__":
    fetch_inventory()