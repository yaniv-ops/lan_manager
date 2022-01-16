from tkinter import *
from calculation import Network

global total_comp
total_comp = 0
global total_vlans
total_vlans = {}


class Switch:


    def __init__(self, button, level):

        self.dept = []
        self.comp = []
        self.level = level
        self.button = button
        self.switch_dict = {}
        self.button.config(bg='black', command=lambda :self.switch_turn_off(button, level))
        self.take_values()

    def switch_turn_off(self, button, level):
        self.button.config(bg='white', command=lambda: Switch(button, level))
        self.window_test.destroy()

    def submited(self):
        global total_comp, total_vlans

        res = {self.dept[i].get(): self.comp[i].get() for i in range(len(self.dept))}
        self.switch_dict = {'switch_level': self.level,
                            'switch_name': self.switch_name_entry.get(),
                            'switch_details': res}

        for item in self.switch_dict['switch_details']:
            total_comp += int(self.switch_dict['switch_details'][item]) +3
            if item not in total_vlans:
                total_vlans[item] = int(self.switch_dict['switch_details'][item])
            else:
                total_vlans[item] += int(self.switch_dict['switch_details'][item])


    def get_values(self):


        for widget in self.window_test_frame.winfo_children():
            widget.destroy()

        switch_name = Label(self.window_test_frame, text='Name the switch:')
        switch_name.pack()
        self.switch_name_entry = Entry(self.window_test_frame)
        self.switch_name_entry.pack()
        for _ in range(self.clicked.get()):
            label_department_number = Label(self.window_test_frame, text=f"department no. {_ + 1}")
            label_department_number.pack(pady=5)
            item_button = Label(self.window_test_frame, text="Name of department?")
            item_button.pack(padx=10, pady=5)
            item_entry = Entry(self.window_test_frame)
            item_entry.pack()
            number_in_vlan = Label(self.window_test_frame, text="How many computers?")
            number_in_vlan.pack(padx=10, pady=5)
            number_in_vlan_entry = Entry(self.window_test_frame)
            number_in_vlan_entry.pack(pady=5)
            self.dept.append(item_entry)
            self.comp.append(number_in_vlan_entry)
        submit_button = Button(self.window_test_frame, text='Submit', command=self.submited)
        submit_button.pack()

    def take_values(self):

        self.window_test = Tk()
        self.window_test.config(bg='#E6DDC4')
        self.window_test.title('LAN Manager')
        self.window_test.iconbitmap('favicon.png')
        self.window_test.geometry("400x800")

        item_button = Label(self.window_test, text="How many department connecting to that switch?")
        item_button.pack()
        self.clicked = IntVar(self.window_test)
        self.clicked.set(1)

        drop = OptionMenu(self.window_test, self.clicked, 1, 2, 3, 4)
        drop.pack(padx=3)
        pick_button = Button(self.window_test, text='Enter', command=self.get_values)
        pick_button.pack()
        self.window_test_frame = LabelFrame(self.window_test, text="Configure switch")
        self.window_test_frame.pack()

    def print(self):
        global total_comp, total_vlans
        scripts_list = []
        network = Network(total_comp)
        for item in total_vlans:
            returnvalue = network.vlan_go(item, total_vlans[item])
            scripts_list.append(returnvalue)
        return scripts_list







