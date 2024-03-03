Ansible Role: bat
=================

[![Tests](https://github.com/gantsign/ansible_role_bat/workflows/Tests/badge.svg)](https://github.com/gantsign/ansible_role_bat/actions?query=workflow%3ATests)
[![Ansible Galaxy](https://img.shields.io/badge/ansible--galaxy-gantsign.bat-blue.svg)](https://galaxy.ansible.com/gantsign/bat)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/gantsign/ansible_role_bat/master/LICENSE)

Role to download and install [bat](https://github.com/sharkdp/bat) the
advanced alternative to `cat`.

Requirements
------------

* Ansible Core >= 2.12

* Linux Distribution

    * Debian Family

        * Debian

            * Buster (10)
            * Bullseye (11)
            * Bookworm (12)

        * Ubuntu

            * Bionic (18.04)
            * Focal (20.04)

        * Note: other versions are likely to work but have not been tested.

Role Variables
--------------

The following variables will change the behavior of this role (default values
are shown below):

```yaml
# bat version number
bat_version: '0.23.0'

# The SHA256 of the bat redistributable package
bat_redis_sha256sum: '56b3d05e11c6d473643766c612d10c2d3de56ff2fcd14b3d82d86f5843307ced'

# Directory to store files downloaded for bat
bat_download_dir: "{{ x_ansible_download_dir | default(ansible_env.HOME + '/.ansible/tmp/downloads') }}"
```

Example Playbook
----------------

```yaml
- hosts: servers
  roles:
    - role: gantsign.bat
```

Tab Completion for Zsh
----------------------

### Using Ansible

The recommended way to enable Zsh support for `bat` is to use the
[gantsign.antigen](https://galaxy.ansible.com/gantsign/antigen) role (this must
be configured for each user).


```yaml
- hosts: servers
  roles:
    - role: gantsign.hub

    - role: gantsign.antigen
      users:
        - username: example
          antigen_bundles:
            - name: bat
              url: gantsign/zsh-plugins
              location: bat
```

### Using Antigen

If you prefer to use [Antigen](https://github.com/zsh-users/antigen) directly
add the following to your Antigen configuration:

```bash
antigen bundle gantsign/zsh-plugins bat
```

More Roles From GantSign
------------------------

You can find more roles from GantSign on
[Ansible Galaxy](https://galaxy.ansible.com/gantsign).

Development & Testing
---------------------

This project uses the following tooling:
* [Molecule](http://molecule.readthedocs.io/) for orchestrating test scenarios
* [Testinfra](http://testinfra.readthedocs.io/) for testing the changes on the
  remote
* [pytest](http://docs.pytest.org/) the testing framework
* [Tox](https://tox.wiki/en/latest/) manages Python virtual
  environments for linting and testing
* [pip-tools](https://github.com/jazzband/pip-tools) for managing dependencies

A Visual Studio Code
[Dev Container](https://code.visualstudio.com/docs/devcontainers/containers) is
provided for developing and testing this role.

License
-------

MIT

Author Information
------------------

John Freeman

GantSign Ltd.
Company No. 06109112 (registered in England)
