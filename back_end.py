from calculation import Network
from switch import Switch

def push_button(button, level):
    one = Switch(button, level)
    print(one)

def numbers(some_dict):
    print(some_dict)


def calculate_network():
    network_a = Network(30)
    global returnvalue
    returnvalue = network_a.vlan_go('mana', 20)
    network_a.vlan_by_switch()
    network_a.vlan_by_switch()




