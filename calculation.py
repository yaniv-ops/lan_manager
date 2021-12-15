
import numpy as np

class Network:

    def __init__(self, number, vlan=1):
        self.ip_list = []
        self.vlan = vlan
        self.number = number + 6
        self.array = np.arange(0,256)
        number_of_bits  = self.calculate_bits(number)
        self.calculate_ip_scope(number_of_bits)
        self.ip_numbers()

    def calculate_bits(self, number_comp):
        self.number_comp = number_comp + 6
        number_twice = 2
        number_bits = 1

        while self.number_comp > number_twice:

            number_twice = number_twice *2
            number_bits += 1

        return number_bits

    def calculate_ip_scope(self, number_bits):
        if number_bits > 8 :
            octet_4 = 0
            number_bits = number_bits - 8
            octet_3 = (255 - (2 ** number_bits - 1))
        else:
            octet_3 = 255
            octet_4 = (255 - (2 ** number_bits - 1))
        self.subnet = (255 - (2 ** number_bits - 1))
        self.mask_subnet = (255 - (255 - ((2 ** number_bits) - 1)))
        ip_scope = f"192.168.{octet_3}.{octet_4}"
        self.subnet_scope = f"255.255.{octet_3}.{octet_4}"
        self.mask_scope = f"0.0.{255-octet_3}.{255-octet_4}"




    def ip_numbers(self):

        z = 1
        a = 0
        y = 0

        for _ in range(z):

            for x in range(self.number_comp):

                if y > 255:
                    z += 1
                    a += 1
                    x = 0
                    y = 0

                text = f"192.168.{a}.{y}"
                self.ip_list.append(text)
                y += 1


    def vlan_go(self, vlan_name, comp_in_vlan):
        vlans = []
        comp_in_vlan = comp_in_vlan + 3
        number_bits = self.calculate_bits(int(comp_in_vlan))
        self.calculate_ip_scope(number_bits)
        slice_ip_list = [value for value in self.ip_list[:(comp_in_vlan)]]
        self.network_ip = slice_ip_list.pop((0))
        self.broadcast = slice_ip_list.pop(-1)
        self.gw = slice_ip_list.pop(0)
        vlan_wrapped = {'vlan_name': vlan_name,
                        'network_ip': self.network_ip,
                        'broadcast_ip': self.broadcast,
                        'gateway_ip': self.gw,
                        'end_devices_ip': slice_ip_list ,
                        'subnet': self.subnet_scope,
                        'mask': self.mask_scope}

        for _ in range(0, len(slice_ip_list) +3):
            self.ip_list.pop(0)
        return vlan_wrapped

    def switch(self, vlan_list, level):
        vlans = []

        for _ in vlan_list:
            poped_ip = []
            dict = {key: value for key, value in _.items()}
            for _ in range(2):
                listi = dict['end_devices_ip'].pop()
                poped_ip.append(listi)
            vlans_object = {'vlan_name': dict['vlan_name'],
                            'vlan_ip_scope': poped_ip,
                            'number_of_interfaces': len(poped_ip),
                            'level': level}

            vlans.append(vlans_object)
            print(poped_ip)
            print(dict['end_devices_ip'])
            for x in vlans:
                print(x)








def calculate_interfaces(comp_sum, dist_sum, core_sum, router_sum):

    router_to_router = 0
    router_to_core = 2

    if router_sum == 2:
        router_to_router = 4
    if core_sum == 2 or core_sum == 0 and dist_sum == 2:
        router_to_core = 4

    total_ip_int = round(float((comp_sum + router_to_core + router_to_router)) * 1.5)
    return total_ip_int


