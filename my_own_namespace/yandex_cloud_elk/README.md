# Ansible Collection - my_own_namespace.yandex_cloud_elk

Ansible collection for education with course netology.

## Requirements

Ansible v2.9.10 or newer

## Install

* ansible must be installed

```shell
pip install ansible
```

* build tar.gz

```shell
ansible-galaxy collection build
```

* install with ansible-galaxy

```shell
ansible-galaxy collection install -p ansible_collections my_own_namespace-yandex_cloud_elk-<version>.tar.gz
```

## Plugins

Collections contains roles:

1. my_own_role

#### descriptions

for create file with path and content

#### parameters

* path - path to file (default: /tmp/file.txt)
* content - content file (default: content)

#### example playbook site.yml

```yaml
---
- name: test playbook
  hosts: localhost
  roles:
    - my_own_namespace.yandex_cloud_elk.my_own_role
```

```shell
ansible-playbook site.yml -v

PLAY [test playbook] ***********************************************************************************************************

TASK [Gathering Facts] *********************************************************************************************************
ok: [localhost]

TASK [my_own_namespace.yandex_cloud_elk.my_own_role : create file with content] ************************************************
changed: [localhost] => {"changed": true, "message": "success save content to the file", "original_message": "/tmp/file.txt"}

PLAY RECAP *********************************************************************************************************************
localhost                  : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```
