class finalize_net:

    def __init__(self, vlan_list, switch_objects):
        self.vlan_list = vlan_list
        self.switch_objects = switch_objects


        for item in self.switch_objects:
            Wrapit(item, vlan_list)

class Wrapit:

    def __init__(self, item, vlan):

        vlan_list = vlan
        f = open(f"{item.switch_dict['switch_name']}.txt", "w")
        f.write(f"for the switch '{item.switch_dict['switch_name']}'\n")
        print(f"for the switch '{item.switch_dict['switch_name']}'\n")
        f.write(f"in the topology level: {item.switch_dict['switch_level']}\n\n")
        print(f"in the topology level: {item.switch_dict['switch_level']}")
        for key, value in item.switch_dict['switch_details'].items():

            egg_list = []

            for vlan in vlan_list:
                if vlan['vlan_name'] == key:
                    f.write(f"\nThe vlan name is '{vlan['vlan_name']}'\n")
                    print(f"The vlan name is '{vlan['vlan_name']}'")
                    f.write(f"the network ip is: {vlan['network_ip']}\n")
                    print(f"the network ip is: {vlan['network_ip']}")
                    f.write(f"the broadcast ip is: {vlan['broadcast_ip']}\n")
                    print(f"the broadcast ip is: {vlan['broadcast_ip']}\n")
                    f.write(f"the subnet ip is: {vlan['subnet']}\n")
                    print(f"the subnet ip is: {vlan['subnet']}")
                    f.write(f"the gateway ip is: {vlan['gateway_ip']}\n")
                    print(f"the gateway ip is: {vlan['gateway_ip']}")
                    f.write('end_devices_are:\n')
                    print('end_devices_are:')

                    for _ in range(int(value)):

                        egg = vlan['end_devices_ip'].pop()
                        f.write(f"{egg}\n")
                        print(egg)
                        egg_list.append(egg)

        f.close()






