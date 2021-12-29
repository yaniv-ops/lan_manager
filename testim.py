from tkinter import *

class Switch:

    def __init__(self, button):
        def switch_turn_off():
            self.button.config(bg='white', command=lambda: Switch(self.button))
        self.button = button
        self.button.config(bg='black', command=switch_turn_off)
        Switch.take_values(self)

    def take_values(self):

        def get_values():
            for widget in self.window_test_frame.winfo_children():
                widget.destroy()

            dept = []
            comp = []

            switch_name = Label(self.window_test_frame, text='Name the switch:')
            switch_name.pack()
            switch_name_entry = Entry(self.window_test_frame)
            switch_name_entry.pack()
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
                dept.append(item_entry)
                comp.append(number_in_vlan_entry)
            submit_button = Button(self.window_test_frame, text='Submit', command='')
            submit_button.pack()

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
        pick_button = Button(self.window_test, text='Enter', command=get_values)
        pick_button.pack()
        self.window_test_frame = LabelFrame(self.window_test, text="Configure switch")
        self.window_test_frame.pack()










