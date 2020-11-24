Ansible Role: bat
=================

[![Tests](https://github.com/gantsign/ansible_role_bat/workflows/Tests/badge.svg)](https://github.com/gantsign/ansible_role_bat/actions?query=workflow%3ATests)
[![Ansible Galaxy](https://img.shields.io/badge/ansible--galaxy-gantsign.bat-blue.svg)](https://galaxy.ansible.com/gantsign/bat)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/gantsign/ansible_role_bat/master/LICENSE)

Role to download and install [bat](https://github.com/sharkdp/bat) the
advanced alternative to `cat`.

Requirements
------------

* Ansible >= 2.8

* Linux Distribution

    * Debian Family

        * Debian

            * Jessie (8)
            * Stretch (9)

        * Ubuntu

            * Xenial (16.04)
            * Bionic (18.04)

        * Note: other versions are likely to work but have not been tested.

Role Variables
--------------

The following variables will change the behavior of this role (default values
are shown below):

```yaml
# bat version number
bat_version: '0.17.1'

# The SHA256 of the bat redistributable package
bat_redis_sha256sum: '0b50b6e654583e870725ed3b2db2c49f1e9612c5dd318f3fd4c4dafbb0f9ce84'

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

This project uses [Molecule](http://molecule.readthedocs.io/) to aid in the
development and testing; the role is unit tested using
[Testinfra](http://testinfra.readthedocs.io/) and
[pytest](http://docs.pytest.org/).

To develop or test you'll need to have installed the following:

* Linux (e.g. [Ubuntu](http://www.ubuntu.com/))
* [Docker](https://www.docker.com/)
* [Python](https://www.python.org/) (including python-pip)
* [Ansible](https://www.ansible.com/)
* [Molecule](http://molecule.readthedocs.io/)

Because the above can be tricky to install, this project includes
[Molecule Wrapper](https://github.com/gantsign/molecule-wrapper). Molecule
Wrapper is a shell script that installs Molecule and it's dependencies (apart
from Linux) and then executes Molecule with the command you pass it.

To test this role using Molecule Wrapper run the following command from the
project root:

```bash
./moleculew test
```

Note: some of the dependencies need `sudo` permission to install.

License
-------

MIT

Author Information
------------------

John Freeman

GantSign Ltd.
Company No. 06109112 (registered in England)
