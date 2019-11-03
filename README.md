# ldap-configuration
Configuration of ldap Server, Client and authentication

Inventory File
Create the inventory file for your institution

  cp inventories/template inventories/<institution>

Variables File
Create the variables file for your institution

cp group_vars/template group_vars/<institution>


Secrets File
Some values - passwords, credentials - are sensitive and should never be submitted to the Github repository. They are therefore stored in a file called secrets.yml, which is being ignored by Github.

Create the secrets.yml file

  cp group_vars/secrets.yml.example group_vars/secrets.yml
Open the secrets.yml file and add the sensitive values.

  openssl rand -base64 12
