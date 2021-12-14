from calculation import Network

subject = Network(70)
vlan_a = subject.vlan_go('manager', 1)
vlan_b = subject.vlan_go('yossi',1)
vlan_c = subject.vlan_go('ponzi', 1)
vlan_list = []
vlan_list.append(vlan_a)
vlan_list.append(vlan_b)

class Switch:

    def __init__(self, interfaces_num, vlans=vlan_list):
        self.interface = interfaces_num
        print(vlans)

    def cal_interface(self, int):
        self.interface = self.interface - int
        return self.interface

    def write_script(self):
        pass

    def deploy_item(self):
        pass

Switch(7)