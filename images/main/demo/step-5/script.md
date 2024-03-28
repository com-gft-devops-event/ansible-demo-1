# Step-5

## Purpose

Show Playbook with Role for Connecting to the Postgres DB, Create a Table , Check for entries and Add Values to the Table. 
Also show the use of Ansible-Vault for Encrpting DB Password.

Show:

- Show  inventory defining Database Host
- Show Playbook with Roles
- Show Role Strcuture 
- Show added Variables in vars/main.yml
- Show how to create Ansible Vault File for adding sensitive information in encrypted format
- Show encrypted password file used for the DB connection

## Execution

ansible-playbook -i inventory step-5.yaml -vv