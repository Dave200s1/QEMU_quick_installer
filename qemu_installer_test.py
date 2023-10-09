from qemu_installer import Script
from unittest.mock import patch
import unittest
import sys
import subprocess
import configparser

class Test_qemu_installer_Script(unittest.TestCase):

    @patch('subprocess.run')
    def test_if_updates_run(self,mock_run):
        #Arrange
        test_object = Script()
        #Act
        test_object.run_updates()
        #Assert
        mock_run.assert_any_call("sudo apt update",shell=True)
        mock_run.assert_any_call("sudo apt upgrade",shell=True)
        sys.stdout = sys.__stdout__

    @patch('subprocess.run')
    def test_if_packages_can_be_installed(self,mock_run):
        #Arrange
        test_object = Script()
        #Act
        test_object.install_packages()
        #Assert
        mock_run.assert_any_call("sudo apt -y install qemu-kvm libvirt-daemon  bridge-utils virtinst libvirt-daemon-system",shell=True)
        sys.stdout = sys.__stdout__


    @patch("subprocess.run")
    def test_check_daemon_running(self,mock_run):
        #Arrange 
        test_object = Script()
        #Act
        test_object.check_if_daemon_runs()
        #Assert
        mock_run.assert_any_call("sudo systemctl status libvirtd.service",shell=True)
        sys.stdout = sys.__stdout__

    @patch("subprocess.run")
    def test_check_available_network_kvm(self,mock_run):
        #Arrange
        test_object = Script()
        #Act
        test_object.check_available_network_kvm()
        #Assert
        mock_run.assert_any_call("virsh net-list --all",shell=True)
        sys.stdout = sys.__stdout__

    @patch("subprocess.run")
    def test_if_default_network_activates(self,mock_run):
        #Arrange
        test_object = Script()
        #Act
        test_object.activate_default_network()
        #Assert
        mock_run.assert_any_call("virsh net-start default",shell=True)
        sys.stdout = sys.__stdout__

    @patch("subprocess.run")
    def test_if_autostart_activates(self,mock_run):
        #Arrange
        test_object = Script()
        #Act
        test_object.activate_autostart()
        #Asssert
        mock_run.assert_any_call("virsh net-autostart",shell = True)
        sys.stdout = sys.__stdout__

    
    @patch('subprocess.run')
    def test_if_download_iso_works(self,mock_run):
        #Arrange
        test_object = Script()
        #Act    
        test_object.download_iso()
        #Assert
        mock_run.assert_any_call("cd /ISOs",shell=True)
        mock_run.assert_any_call("wget https://cdimage.debian.org/cdimage/daily-builds/daily/arch-latest/amd64/isocd/debian-testing-amd64-netinst.iso", shell =True)
        sys.stdout = sys.__stdout__

    @patch('subprocess.run')
    def test_create_directories(self,mock_run):
        #Arrange
        test_object = Script()
        #Act
        test_object.create_directorieste_vm()
        #Assert
        mock_run.assert_any_call("mkdir /ISOs",shell=True)
        mock_run.assert_any_call("mkdir /VMs",shell=True)
        mock_run.assert_any_call("virsh list --all",shell=True)
        sys.stdout = sys.__stdout__

    @patch("subprocess.run")
    def test_if_backup_works(self,mock_run):
        #Arrange
        test_object = Script()
        #Act
        test_object.do_a_backup()
        #Assert
        mock_run.assert_any_call("sudo cp /etc/network/interfaces   /etc/network/interfaces.bak",shell=True)
        sys.stdout = sys.__stdout__

    @patch("subprocess.run")
    def test_if_check_for_vHost_works(self,mock_run):
        #Arrange
        test_object = Script()
        #Act
        test_object.check_for_vHost()
        #Assert
        mock_run.assert_any_call("lsmod | grep vhost",shell=True)
        sys.stdout = sys.__stdout__

if __name__ == 'main':
    unittest.main()

