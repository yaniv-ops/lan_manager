import numpy as np
import math



class Network:

    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.array = np.arange(0,256)
        print(self.array[0])
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





subject = Network('MAN','10')
a = subject.calculate_bits(10)
subject.calculate_ip_scope(a)
print(a)


def calculate_interfaces(comp_sum, dist_sum, core_sum, router_sum):
    router_to_router = 0
    router_to_core = 2

    if router_sum == 2:
        router_to_router = 4
    if core_sum == 2 or core_sum == 0 and dist_sum == 2:
        router_to_core = 4

    total_ip_int = round(float((comp_sum + router_to_core + router_to_router)) * 1.5)
    return total_ip_int

n=0
n_list=[]
for _ in range(1280):
    n_list.append(_)

print(n_list)

z = 1
a = 0
y = 0

for _ in range(z):

    text = f"192.168.{a}.{y}"

    for x in range(len(n_list)):

        if y > 255:
            z += 1
            a += 1
            x = 0
            y = 0
        text = f"192.168.{a}.{y}"
        print(text)
        y += 1


print(n_list)
vlan = 7
#a = calculate_interfaces(250, 2, 2, 2)
#calculate_vlan(a, vlan)

#print(a)