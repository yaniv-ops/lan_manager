class finalize_net:

    def __init__(self, vlan_list, switch_objects):
        self.vlan_list = vlan_list
        self.switch_objects = switch_objects
        for item in self.switch_objects:
            print(item.switch_dict)


