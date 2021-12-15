from calculation import Network

subject = Network(21)
vlan_a = subject.vlan_go('manager', 7)
vlan_b = subject.vlan_go('yossi',7)
vlan_c = subject.vlan_go('ponzi',7)
vlan_list = []

vlan_list.append(vlan_a)
vlan_list.append(vlan_b)
vlan_list.append(vlan_c)

print(vlan_list)
computers = [7 , 7 , 7]
switch_a = subject.switch(vlan_list, 'access')
switch_b = subject.switch(vlan_list, 'core')


