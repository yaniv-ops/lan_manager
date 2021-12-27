from calculation import Network

def calculate_network(total_comps):
    subject = Network(total_comps)
    vlan_a = subject.vlan_go('manager', 7)
    vlan_b = subject.vlan_go('yossi',7)
    vlan_c = subject.vlan_go('ponzi',7)
    global vlan_list
    vlan_list = []

    vlan_list.append(vlan_a)
    vlan_list.append(vlan_b)
    vlan_list.append(vlan_c)

    print(vlan_list)
    computers = [7 , 7 , 7]
    switch_a = subject.switch(vlan_list, 'access')
    print(vlan_list)
    switch_b = subject.switch(vlan_list, 'core')
    print(vlan_list)
    print(switch_b)


def print_scripts(total_comp):
    calculate_network(total_comp)
