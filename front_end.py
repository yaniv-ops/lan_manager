
#----------UI-SETUP--------------------#

from tkinter import Tk, LabelFrame, Canvas, IntVar, Radiobutton, Button, Label
from PIL import ImageTk, Image
from back_end import Router



### attributes ###


is_on = 'False'

core_list = []
dis_list = []
access_list = []


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

    router_a = Router()
    core_list.append(router_a)
    router.config(bg="black", command=lambda: router_off(router_a, router))
    print(core_list)

def router_off(router_a, router):

    router.config(bg='white', command=lambda: router_on(router))
    core_list.remove(router_a)
    print(core_list)

def switch_on(switch):

    switch_a = Router()
    dis_list.append(switch_a)
    switch.config(bg="black", command=lambda: switch_off(switch_a, switch))
    print(dis_list)

def switch_off(switch_a, switch):

    switch.config(bg='white', command=lambda: switch_on(switch))
    dis_list.remove(switch_a)
    print(dis_list)

def comp_on(comp):

    comp_a = Router()
    access_list.append(comp_a)
    comp.config(bg="black", command=lambda: comp_off(comp_a, comp))
    print(access_list)

def comp_off(comp_a, comp):

    comp.config(bg='white', command=lambda: comp_on(comp))
    access_list.remove(comp_a)
    print(access_list)

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
comp_a = Button(virtual_canvas, width=40, height=40, image=comp_img2, command=lambda :comp_on(comp_a))
comp_a.grid(row=4, column=1,padx=10, pady=20)

comp_b = Button(virtual_canvas, width=40, height=40, image=comp_img2, command=lambda :comp_on(comp_b))
comp_b.grid(row=4, column=2,padx=10, pady=20)

comp_c = Button(virtual_canvas, width=40, height=40, image=comp_img2, command=lambda :comp_on(comp_c))
comp_c.grid(row=4, column=3,padx=10, pady=20)

comp_d = Button(virtual_canvas, width=40, height=40, image=comp_img2, command=lambda :comp_on(comp_d))
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


