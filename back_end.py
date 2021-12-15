from calculation import Network
from interface import Switch

subject = Network(50)
vlan_a = subject.vlan_go('manager', 7)
vlan_b = subject.vlan_go('yossi',7)
vlan_c = subject.vlan_go('ponzi',7)
vlan_list = []
vlan_list.append(vlan_a)
vlan_list.append(vlan_b)
print(vlan_list)
subject.switch(vlan_list)

# test = Switch(vlan_list, 24, 'access')
# a = test.pop_ip_out(vlan_list)
