class finalize_net:

    def __init__(self, vlan_list, switch_objects):
        self.vlan_list = vlan_list
        self.switch_objects = switch_objects
        ip_lists = []
        print(vlan_list)
        for item in self.switch_objects:
            print(item.switch_dict)
            vlan_switch_dict = item.switch_dict['switch_details']
            print(vlan_switch_dict)
            for key ,value in vlan_switch_dict.items():
                print(key, value)
                for item in range(int(value)):
                    for item in vlan_list:
                        if  item['vlan_name'] == key:
                            print(item['end_devices_ip'])
                            joy = item['end_devices_ip'].pop()
                            ip_lists.append(joy)
                        ham = {key: ip_lists}
                        print(ham)




