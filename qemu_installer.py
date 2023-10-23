#! /usr/bin/env python3

import subprocess
import configparser
import os

class Script():

    def __init__(self):
        pass

    def welcome(self):
        print("\nWelcome to QEmu-Installer !")
        print("\nInstallation will begin shortly....")


    def run_updates(self):
        cmd ="sudo apt update"
        subprocess.run(cmd,shell=True)
        cmd_upgrade ="sudo apt upgrade"
        subprocess.run(cmd_upgrade,shell=True)

    def install_packages(self):
        cmd ="sudo apt -y install qemu-kvm libvirt-clients qemu-utils libvirt-daemon  bridge-utils virtinst libvirt-daemon-system "
        subprocess.run(cmd,shell=True)

    def check_if_daemon_runs(self):
        cmd ="sudo systemctl status libvirtd.service"
        subprocess.run(cmd,shell=True)

    def check_available_network_kvm(self):
        cmd ="sudo virsh net-list --all"
        subprocess.run(cmd,shell=True)
    def enable_modprob(self):
        cmd = "sudo systemctl enable --now libvirtd"
        subprocess.run(cmd, shell=True)
        cmd_second = "sudo systemctl enable --now virtlogd"
        subprocess.run(cmd_second, shell=True)
        cmd_third = "sudo modprobe kvm"
        subprocess.run(cmd_third, shell=True)
        

    def activate_default_network(self):
        cmd = "sudo virsh net-start default"
        subprocess.run(cmd,shell=True)

    def activate_autostart(self):
        cmd = "sudo virsh net-autostart"
        subprocess.run(cmd,shell=True)


    def download_iso(self):
        #current_dir = os.getcwd()
        cmd ="sudo wget https://cdimage.debian.org/cdimage/release/current-live/amd64/iso-hybrid/debian-live-12.2.0-amd64-xfce.iso"
        
       
        new_dir = "/home/dsi/ISOs"
        os.chdir(new_dir)
        subprocess.run("pwd",shell=True)
        
        
        subprocess.run(cmd,shell=True)


    def create_directorieste_vm(self):
        cmd_isos = "sudo mkdir /home/dsi/ISOs"
        cmd_vms = "sudo mkdir /home/dsi/VMs"
        cmd_list = "sudo virsh list --all"

        subprocess.run(cmd_isos,shell=True)
        subprocess.run(cmd_vms,shell=True)
        subprocess.run(cmd_list,shell=True)

    def do_a_backup(self):
        cmd = "sudo cp /etc/network/interfaces   /etc/network/interfaces.bak"
        subprocess.run(cmd,shell=True)

    def check_for_vHost(self):
        cmd ="lsmod | grep vhost"
        subprocess.run(cmd,shell=True)

	#Needs to be fixed !!!
    def add_VHostNet_module(self):
        subprocess.call(['sudo','-v'])
        config = configparser.ConfigParser()

        text_to_insert = """
        firewire-sbp2
        vhost_net
        """
        #target path
        file_path = "/etc/modules"

        with open("temp.txt","w") as f:
            f.write(text_to_insert)

        cmd = f"sudo sh -c 'cat temp.text >> {file_path}'"
        subprocess.call([cmd],shell=True)

        #Remove temp_file
        subprocess.call(["rm","temp.txt"])

    def config_bidge(self):
        print("\nPlease go to nano /etc/network/interfaces and enter the following...")
        print("\n inface br0 inet static , leave the rest and add at the bottom bridge_ports (yourInterfaceName)")
        print("\nAfter your done do a reboot and us ip a s br0 to check config")

    def create_VM(self):
        name = input("Enter the name for the VM: ")
        ram = input("Enter the RAM size (in MB): ")
        vcpu = input("Enter the number of vCPUs: ")
        size = input("Enter the size of the disk (in GB): ")
        dp = input("Enter the diskpath_name (example: debian): ")
        command = f"sudo virt-install --name {name} --os-type linux --os-variant unknown --ram {ram} --vcpu {vcpu} --disk path=/home/dsi/VMs/{dp}.qcow2,size={size} --graphics vnc,listen=0.0.0.0 --noautoconsole --hvm --cdrom /home/dsi/ISOs/debian-live-12.2.0-amd64-xfce.iso --boot cdrom,hd --force --check all=off"
    
        subprocess.run(command,shell=True)

    def display_the_port(self):
        cmd = "sudo virsh list --all"
        subprocess.run(cmd,shell=True)
        yourVmName = input("Enter the Name of your VM: ")
        cmd_port = f"sudo virsh vncdisplay {yourVmName}"
        subprocess.run(cmd_port,shell=True)
        subprocess.run("ip addr",shell=True)

    #TODO
    def installation(self):
        self.welcome()
        self.run_updates()
        self.install_packages()
        self.enable_modprob()
        self.check_if_daemon_runs()
        print("\nPlease do a system reboot and start the programm again")
        self.activate_default_network()
        self.check_available_network_kvm()
        self.activate_autostart()
        self.do_a_backup()
        self.create_directorieste_vm()
        #self.add_VHostNet_module()
        self.check_for_vHost()
        #DO Not USE self.config_bidge()
        #self.download_iso()
        self.create_VM()
        self.display_the_port()
        print("\nAll done ....")
        
        
