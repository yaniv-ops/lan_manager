import numpy as np
import math
class Vlan:

    def __init__(self, name, number):
        self.name = name
        self.number = number

    # def calculate_vlan(a, vlan):
    #     subnet_ip_num = a - (a - (vlan + 2))
    #     print(subnet_ip_num)

    def calculate_bits(self, number_comp):
        self.number_comp = number_comp
        number_twice = 2
        number_bits = 1



        while self.number_comp > number_twice:

            number_twice = number_twice *2
            number_bits += 1

        return number_bits

    def calculate_ip_scope(self, number_bits):
        number_bits = number_bits
        subnet_3 = (255 - (2 ** number_bits - 1))
        print(subnet_3)
        subnet_4 = (255 - (255 - ((2 ** number_bits) - 1)))
        ip_scope = f"192.168.{subnet_3}.{subnet_4}"
        subnet = f"255.255.{subnet_3}.{subnet_4}"
        print(subnet)





subject = Vlan('MAN','10')
a = subject.calculate_bits(5)
subject.calculate_ip_scope(a)
print(a)
#subject.calculate_ip_scope(a)

    # print(ip_scope)


    # number_comp = 64
    # print(math.sqrt(4096))
    # print(2**12)


    # sum_1 = int(2**power_of)
    #
    # print(sum_1)




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
#a = calculate_interfaces(250, 2, 2, 2)
#calculate_vlan(a, vlan)

#print(a)