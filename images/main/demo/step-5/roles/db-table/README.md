db-table
=========

This role is used to connect to the Postgres Database and create a Table called 'hosts' with Two Columns - hostname and groups. 
Check if the entries already exsists in the table. If not,adds the values of hostname and groups to the table.

Requirements
------------
na

Role Variables
--------------
dbname - Name of the Database 
dbuser - User to connect to the database
table_name -  Name of the table to be created.
columns - Each array value corresponds to the Column Name to be add in to the Table and its Type.
data - Each array value corresponds to the values added in to the Table Columns.
dbpassword -  It is obtained from the vault file under files/db_password.yml

Dependencies
------------
na

Example Playbook
----------------

---
- name: Create PostgreSQL table and insert data
  hosts: database_host
  roles:
    - db-table

License
-------
BSD

Author Information
------------------
Akshaya.Parthasarathy@gft.com
