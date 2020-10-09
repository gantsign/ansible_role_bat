import re


def test_version(host):
    version = host.check_output('bat --version')
    pattern = r'bat [0-9\.]+'
    assert re.search(pattern, version)
