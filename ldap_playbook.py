---
- hosts: ldap_server
  vars_files:
    - "inventories/{{ stage }}/vars/ldap_secret.yml"
  roles:
    - ldap_server
    - ldap_entry
- hosts: ldap_client
    - batch
  vars_files:
    - "inventories/{{ stage }}/vars/ldap_secret.yml"
  roles:
    - ldap_client