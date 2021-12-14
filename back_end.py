
class Router:

    def __init__(self, protocol, hsrp, name, manager_address):
        self.interface = 8
        self.protocol = protocol
        self.hsrp = hsrp
        self.name = name
        self.manager_address = manager_address

    def cal_interface(self, int):
        self.interface = self.interface - int
        return self.interface

    def write_script(self):
        pass

    def deploy_item(self):
        pass

