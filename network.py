class finalize_net:

    def __init__(self, vlan_list, switch_objects):
        self.vlan_list = vlan_list
        self.switch_objects = switch_objects
        ham ={}
        print(self.vlan_list)

        for item in self.switch_objects:
            print(item.switch_dict)
            for key ,value in item.switch_dict['switch_details'].items():
                print(key ,value)
                for vlan in self.vlan_list:
                    if vlan['vlan_name'] == key:
                        print(vlan)
                        for _ in range(int(value)):
                            print(vlan['end_devices_ip'])
                            vlan['end_devices_ip'].pop()

        print(self.vlan_list)





