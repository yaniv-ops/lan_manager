
#----------UI-SETUP--------------------#

from tkinter import Tk, LabelFrame, Canvas, IntVar, Radiobutton, Button, Label, OptionMenu, Entry
from PIL import ImageTk, Image




### attributes ###


is_on = 'False'

router_list = []
core_list = []
dis_list = []
access_list = []
comp_list = []

### FUNCTION ###

def button_on(vlan):
    global is_on
    if is_on == 'False':
        vlan.config(bg='pink')
        is_on = 'TRUE'
        print(is_on)
    else:
        is_on = 'False'
        vlan.config(bg='white')
        print(is_on)

def router_on(router):

    router.config(bg='black', command=lambda: router_off(router))

def router_off(router):

    router.config(bg='white', command=lambda: router_on(router))





def switch_on(switch):
    def take_values():
        for widget in window_test_frame.winfo_children():
            widget.destroy()
        window_test_frame.pack()
        for _ in range(clicked.get()):

            label_department_number = Label(window_test_frame,text=f"department no. {_ +1}")
            label_department_number.pack(pady=5)
            item_button = Label(window_test_frame, text="Name of department?")
            item_button.pack(padx=10, pady=5)
            item_entry = Entry(window_test_frame)
            item_entry.pack()
            number_in_vlan = Label(window_test_frame, text="How many computers?")
            number_in_vlan.pack(padx=10, pady=5)
            number_in_vlan_entry = Entry(window_test_frame)
            number_in_vlan_entry.pack(pady=5)
        submit_button = Button(window_test_frame, text='Submit')
        submit_button.pack()

    window_test = Tk()
    window_test.config(bg='#E6DDC4')
    window_test.title('LAN Manager')
    window_test.iconbitmap('favicon.png')
    window_test.geometry("400x800")

    item_button = Label(window_test, text="How many department connecting to that switch?")
    item_button.pack()
    clicked = IntVar(window_test)
    clicked.set(1)

    drop = OptionMenu(window_test, clicked, 1, 2, 3, 4)
    drop.pack(padx = 3)
    pick_button = Button(window_test, text='Enter', command=take_values)
    pick_button.pack()

    window_test_frame = LabelFrame(window_test, text="Configure switch")



    # if switch == btn_switch_a or switch == btn_switch_b:
    #     core_list.append(switch)
    #     print(f' core_list: {core_list}')
    # elif switch == btn_switch_c or switch == btn_switch_d:
    #     dis_list.append(switch)
    #     print(f' distro list: {dis_list}')
    # elif switch == btn_switch_e or switch == btn_switch_f or switch == btn_switch_g or switch == btn_switch_h:
    #     access_list.append(switch)
    #     print(f'access_list: {access_list}')
    # else:
    #     comp_list.append(switch)
    #     print(comp_list)

    switch.config(bg="black", command=lambda: switch_off(switch_a, switch))

    window_test.mainloop()


def switch_off(switch_a, switch):

    switch.config(bg='white', command=lambda: switch_on(switch))
    if switch == btn_switch_a or switch == btn_switch_b:
        core_list.remove(switch)
        print(f' core_list: {core_list}')
    elif switch == btn_switch_c or switch == btn_switch_d:
        dis_list.remove(switch)
        print(f' distro list: {dis_list}')
    elif switch == btn_switch_e or switch == btn_switch_f or switch == btn_switch_g or switch == btn_switch_h:
        access_list.remove(switch)
        print(f'access_list: {access_list}')
    else:
        comp_list.remove(switch)


window= Tk()
window.config(bg='#E6DDC4')
window.title('LAN Manager')
window.iconbitmap('favicon.png')

# make the virtual board

virtual_frame = LabelFrame(window, width=800, text="This is the virtual board", padx=10, pady=10)
virtual_frame.grid(row=0, column=0, columnspan=5, padx=5, pady=5)
virtual_canvas = Canvas(virtual_frame, width=800, height=400, bg='#F3F0D7')
virtual_canvas.pack(padx=5, pady=5)
core_label = Label(virtual_canvas, text='Core')
core_label.grid(row=1, column=0,padx=10, pady=20)
distr_label = Label(virtual_canvas, text='Distribution')
distr_label.grid(row=2, column=0,padx=10, pady=20)
access_label = Label(virtual_canvas, text="Access")
access_label.grid(row=3, column=0,padx=10, pady=20)
router_img3 = ImageTk.PhotoImage(Image.open('router.png').resize((70, 70)))
btn_router_a = Button(virtual_canvas, width=40, height=40, image=router_img3, command=lambda :router_on(btn_router_a))
btn_router_a.grid(row=0, column=2,padx=10, pady=20)
btn_router_b = Button(virtual_canvas, width=40, height=40, image=router_img3, command=lambda :router_on(btn_router_b))
btn_router_b.grid(row=0, column=3, padx=10, pady=20)
switch_img2 = ImageTk.PhotoImage(Image.open('switch.png').resize((50, 50)))
btn_switch_a = Button(virtual_canvas, width=40, height=40, image=switch_img2, command=lambda :switch_on(btn_switch_a))
btn_switch_a.grid(row=1, column=2,padx=10, pady=20)
btn_switch_b = Button(virtual_canvas, width=40, height=40, image=switch_img2, command=lambda :switch_on(btn_switch_b))
btn_switch_b.grid(row=1, column=3,padx=10, pady=20)
btn_switch_c = Button(virtual_canvas, width=40, height=40, image=switch_img2, command=lambda :switch_on(btn_switch_c))
btn_switch_c.grid(row=2, column=2,padx=10, pady=20)
btn_switch_d = Button(virtual_canvas, width=40, height=40, image=switch_img2, command=lambda :switch_on(btn_switch_d))
btn_switch_d.grid(row=2, column=3,padx=10, pady=20)

btn_switch_e = Button(virtual_canvas, width=40, height=40, image=switch_img2, command=lambda :switch_on(btn_switch_e))
btn_switch_e.grid(row=3, column=1,padx=10, pady=20)

btn_switch_f = Button(virtual_canvas, width=40, height=40, image=switch_img2, command=lambda :switch_on(btn_switch_f))
btn_switch_f.grid(row=3, column=2,padx=10, pady=20)
btn_switch_g = Button(virtual_canvas, width=40, height=40, image=switch_img2, command=lambda :switch_on(btn_switch_g))
btn_switch_g.grid(row=3, column=3,padx=10, pady=20)
btn_switch_h = Button(virtual_canvas, width=40, height=40, image=switch_img2, command=lambda :switch_on(btn_switch_h))
btn_switch_h.grid(row=3, column=4,padx=10, pady=20)

comp_img2 = ImageTk.PhotoImage(Image.open('comp.png').resize((50, 50)))
comp_a = Button(virtual_canvas, width=40, height=40, image=comp_img2, command=lambda :switch_on(comp_a))
comp_a.grid(row=4, column=1,padx=10, pady=20)

comp_b = Button(virtual_canvas, width=40, height=40, image=comp_img2, command=lambda :switch_on(comp_b))
comp_b.grid(row=4, column=2,padx=10, pady=20)

comp_c = Button(virtual_canvas, width=40, height=40, image=comp_img2, command=lambda :switch_on(comp_c))
comp_c.grid(row=4, column=3,padx=10, pady=20)

comp_d = Button(virtual_canvas, width=40, height=40, image=comp_img2, command=lambda :switch_on(comp_d))
comp_d.grid(row=4, column=4,padx=10, pady=20)

# make the icons bar

icon_frame = LabelFrame(window, text='icons', padx=5, pady=5)
icon_frame.grid(row=1, column=0, padx=5, pady=5)
icon_canvas = Canvas(icon_frame, width=50, height=150, bg='white')
icon_canvas.pack(padx=5, pady=5)
router_img = ImageTk.PhotoImage(Image.open('router.png').resize((70, 70)))
router_label = Label(icon_canvas, image=router_img)
router_label.pack(padx=1, pady=1)
switch_img = ImageTk.PhotoImage(Image.open('switch.png').resize((50, 50)))
switch_label = Label(icon_canvas, image=switch_img)
switch_label.pack()
comp_img = ImageTk.PhotoImage(Image.open('comp.png').resize((50, 50)))
comp_label = Label(icon_canvas, image=comp_img)
comp_label.pack()


# make the protocols bar

protocol_frame = LabelFrame(window, text='Protocols', padx=5, pady=5)
protocol_canvas = Canvas(protocol_frame, width=70, height=150)
protocol_frame.grid(row=1, column=1, padx=5, pady=5)
protocol_canvas.pack(padx=5, pady=5)

protocol = IntVar()

Radiobutton(protocol_canvas, text='RIP', variable=protocol, value='RIP').pack()
Radiobutton(protocol_canvas, text='EIGRP', variable=protocol, value='EIGRP').pack()
Radiobutton(protocol_canvas, text='OSPF', variable=protocol, value='OSPF').pack()
Radiobutton(protocol_canvas, text='IS-IS', variable=protocol, value='IS-IS').pack()

# make the switching bar

switch_frame = LabelFrame(window, text='Switch menu', padx=5, pady=5)
switch_canvas = Canvas(switch_frame, width=70, height=150)
switch_frame.grid(row=1, column=2, padx=5, pady=5)
switch_canvas.pack(padx=5, pady=5)
vlan_button = Button(switch_canvas, text="VLAN", command=lambda :button_on(vlan_button))
vlan_button.pack(padx=5, pady=5)
ospf_button = Button(switch_canvas, text="Area", command=lambda :button_on(ospf_button))
ospf_button.pack()
hsrp_button = Button(switch_canvas, text="HSRP", command=lambda :button_on(hsrp_button))
hsrp_button.pack()

# make the deployment bar

deploy_frame = LabelFrame(window, text='Deploy menu', padx=5, pady=5)
deploy_canvas = Canvas(deploy_frame, width=70, height=150)
deploy_frame.grid(row=1, column=3, padx=5, pady=5)
deploy_canvas.pack(padx=5, pady=5)
print_button = Button(deploy_canvas, text="Print scripts", command='')
print_button.pack(padx=5, pady=5)
deploy_button = Button(deploy_canvas, text="Deploy net  work", command='')
deploy_button.pack()
exit_button = Button(deploy_canvas, text="EXIT", command=window.quit)
exit_button.pack()

# make an image desktop

image_frame = LabelFrame(window, padx=5, pady=5)
image_frame.grid(row=1, column=4, padx=5, pady=5)
desk_img = ImageTk.PhotoImage(Image.open('network.jpg').resize((200, 200)))
img_label = Label(image_frame, image=desk_img)
img_label.pack()

window.mainloop()


