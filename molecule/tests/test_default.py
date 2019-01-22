import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_slurmdbd_package(host):
    assert host.package("slurm-slurmdbd-ohpc").is_installed


def test_slurmdbd_conf_file(host):
    f = host.file("/etc/slurm/slurmdbd.conf")
    assert f.exists
    assert f.is_file
    assert f.user == 'root'
    assert f.group == 'root'
    assert oct(f.mode) == '0644'


def test_munge_service(host):
    s = host.service('munge')
    assert s.is_running
    assert s.is_enabled


def test_slurmdbd_service(host):
    s = host.service('slurmdbd')
    assert s.is_running
    assert s.is_enabled


#  def test_cgred_service(host):
    #  s = host.service('cgred')
    #  assert s.is_running
    #  assert s.is_enabled


#  def test_cgconfig_service(host):
    #  s = host.service('cgconfig')
    #  assert s.is_running
    #  assert s.is_enabled
