dynamic-inventory-db
=========
This role uses a script to connect to the Database and get the host details, added it dynamically to the ansible inventory.


Requirements
------------
na

Role Variables
--------------
DB password is encrypted using Ansible Vault.

Dependencies
------------
na

Example Playbook
----------------
---
- name: Update Dynamic Inventory from Database
  hosts: localhost
  roles:
    - dynamic-inventory-db

License
-------
BSD

Author Information
------------------
Akshaya.Parthasarathy@gft.com