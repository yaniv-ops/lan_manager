from switch import Switch
from network import finalize_net

switch_objects = []

def push_button(button, level):

    global one
    one = Switch(button, level)
    switch_objects.append(one)


def print_scripts():
    return_list = one.print()
    network = finalize_net(return_list, switch_objects)







