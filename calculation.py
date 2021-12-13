import numpy as np
import math



class Network:

    def __init__(self, number, vlan=1):
        self.ip_list = []
        self.vlan = vlan
        self.number = number
        self.array = np.arange(0,256)
        number_of_bits  = self.calculate_bits(number)
        self.calculate_ip_scope(number_of_bits)
        self.ip_numbers()

    def calculate_bits(self, number_comp):
        self.number_comp = number_comp
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
        subnet = (255 - (2 ** number_bits - 1))
        print(subnet)
        mask_subnet = (255 - (255 - ((2 ** number_bits) - 1)))
        ip_scope = f"192.168.{octet_3}.{octet_4}"
        mask_scope = f"255.255.{octet_3}.{octet_4}"
        print(mask_scope)
        print(self.vlan)

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
        print(self.ip_list)

subject = Network(9)

def calculate_interfaces(comp_sum, dist_sum, core_sum, router_sum):

    router_to_router = 0
    router_to_core = 2

    if router_sum == 2:
        router_to_router = 4
    if core_sum == 2 or core_sum == 0 and dist_sum == 2:
        router_to_core = 4

    total_ip_int = round(float((comp_sum + router_to_core + router_to_router)) * 1.5)
    return total_ip_int

vlan = 7
