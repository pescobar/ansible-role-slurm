ansible-role-slurm
=========

**this is still a work in progress**

Install slurm from OpenHPC repositories

Requirements
------------

None

Role Variables
--------------

By default this role will install slurm accounting daemon, slurm master daemon and slurm worker daemon in the same host.
I do it like that to test all the steps in a single machine when doing CI but most probably that's not what you want
for a production deployment.

```
# add the public OpenHPC yum repos
slurm_add_ohpc_repos: true

# use the OpenHPC rpms
# to use the public yum repos do "slurm_add_ohpc_repos: true"
# to use internal OHPC yum repos (provided outside of this role) do "slurm_add_ohpc_repos: false"
slurm_use_ohpc_rpms: true

slurm_ohpc_repos_url: https://github.com/openhpc/ohpc/releases/download/v1.3.GA/ohpc-release-1.3-1.el7.x86_64.rpm

slurm_accounting_host: true
slurm_master_host: true
slurm_worker_host: true

slurm_mysql_user: slurm
slurm_mysql_password: password
slurm_mysql_db: slurm_acct_db

slurm_cluster_name: "{{ hostvars[inventory_hostname].inventory_hostname }}"
```

Dependencies
------------

None

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: ansible-role-slurm }

License
-------

GPLv3

Author Information
------------------

Pablo Escobar
