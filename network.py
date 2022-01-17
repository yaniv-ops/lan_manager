class finalize_net:

    def __init__(self, vlan_list, switch_objects):
        self.vlan_list = vlan_list
        self.switch_objects = switch_objects


        for item in self.switch_objects:
            Wrapit(item, vlan_list)

class Wrapit:

    def __init__(self, item, vlan):

        vlan_list = vlan
        print(f"for the switch '{item.switch_dict['switch_name']}'\n")
        print(f"in the topology level: {item.switch_dict['switch_level']}")
        for key, value in item.switch_dict['switch_details'].items():

            egg_list = []

            for vlan in vlan_list:
                if vlan['vlan_name'] == key:
                    print(f"The vlan name is '{vlan['vlan_name']}'")
                    print(f"the network ip is: {vlan['network_ip']}")
                    print(f"the broadcast ip is: {vlan['broadcast_ip']}")
                    print(f"the subnet ip is: {vlan['subnet']}")
                    print(f"the gateway ip is: {vlan['gateway_ip']}")
                    print('end_devices_are:')

                    for _ in range(int(value)):

                        egg = vlan['end_devices_ip'].pop()
                        print(egg)
                        egg_list.append(egg)








