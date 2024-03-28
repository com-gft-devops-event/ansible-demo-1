# Step-6

## Purpose

Show 1st Play  with Role to fetch host details from the Database and add it as Dynamic Inventory.
Show 2nd Play with Tasks to fetch details using the Hosts added in Dynamic Inventory.

Show:

- Show  inventory containing an empty file before running the Playbook.
- Show Playbook with 2 Plays.
- Show Role Strcuture 
- Show Script and Vault file being added under files/
- Show both ways of running 2nd play (with add-host in-memory and inventory file).
- Show inventory/main.yaml post running with added hosts.

## Execution

ansible-playbook step-6.yaml -vv