## Important Before starting the script please configure the bridge interface !

## 1: Use ip addr to see your networkInterface , example  enplsXXX

## 2: Edit the /etc/network/interfaces
    auto br0
    iface br0 inet static
        adress yourIP
        geteway yourIP.0
        bridge_ports enpXXX
        
## 3: Go to /etc/modules
add the following
firewire-sbp2
vhost_net

## 4: Change permissions
uncommen user="root" and group="root" 

    # The user for QEMU processes run by the system instance. It can be
    # specified as a user name or as a user id. The qemu driver will try to
    # parse this value first as a name and then, if the name doesn't exist,
    # as a user id.
    #
    # Since a sequence of digits is a valid user name, a leading plus sign
    # can be used to ensure that a user id will not be interpreted as a user
    # name.
    #
    # Some examples of valid values are:
    #
    #       user = "qemu"   # A user named "qemu"
    #       user = "+0"     # Super user (uid=0)
    #       user = "100"    # A user named "100" or a user with uid=100
    #
    user = "root"

    # The group for QEMU processes run by the system instance. It can be
    # specified in a similar way to user.
    group = "root"

    # Whether libvirt should dynamically change file ownership
    # to match the configured user/group above. Defaults to 1.
    # Set to 0 to disable file ownership changes.
    #dynamic_ownership = 1

    [root@dev1 ~]# service libvirtd restart
    Stopping libvirtd daemon:                                  [  OK  ]
    Starting libvirtd daemon:                                  [  OK  ]
        