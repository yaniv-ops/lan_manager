class finalize_net:

    def __init__(self, vlan_list, switch_objects):
        self.vlan_list = vlan_list
        self.switch_objects = switch_objects
        ham ={}
        print(vlan_list)
        for item in self.switch_objects:
            print(item.switch_dict)
            vlan_switch_dict = item.switch_dict['switch_details']
            print(vlan_switch_dict)
            for key ,value in vlan_switch_dict.items():
                ip_lists = []
                print(key, value)
                for _ in range(int(value)):
                    for _ in vlan_list:
                        if  _['vlan_name'] == key:
                            print(_['gateway_ip'])
                            print(_['subnet'])
                            print(_['end_devices_ip'])
                            joy = _['end_devices_ip'].pop()
                            ip_lists.append(joy)
                    ham[key] = ip_lists
                    print(ham)
            item.switch_dict['switch_details'] = ham
            print(item.switch_dict)




