
#the function takes switch name, vlans(names, gw ip, end ips, subnet) and returns

class Switch:

    def __init__(self,ip_list, interface_number, position):
        self.vlans_list = ip_list
        self.switch_details = {'switch': {'name': 'Yaniv',
                                          'vlans': [{'vlan_name': 'Manager',
                                                     'vlan_ip_scope':['iplist','other']}],
                                          'intefaces': interface_number,
                                          'level': position }}
        list = self.switch_details['switch']['vlans']
        a = self.pop_ip_out(list)



    def pop_ip_out(self, list):
        list.pop(0)
        poped_list = list
        self.switch_details['switch']['vlans'] = poped_list
        return self.switch_details













