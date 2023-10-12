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
        