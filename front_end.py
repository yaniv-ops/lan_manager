
#----------UI-SETUP--------------------#

from tkinter import Tk, LabelFrame, Canvas, IntVar, Radiobutton, Button, Label
from PIL import ImageTk, Image



### attributes ###


is_on = 'False'
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

window= Tk()
window.config(bg='#E6DDC4')
window.title('LAN Manager')
window.iconbitmap('favicon.png')

# make the virtual board

virtual_frame = LabelFrame(window, text="This is the virtual board")
virtual_frame.grid(row=0, column=0, columnspan=5, padx=5, pady=5)
virtual_canvas = Canvas(virtual_frame, width=600, height=300, bg='#F3F0D7')
virtual_canvas.pack(padx=5, pady=5)

# make the icons bar

icon_frame = LabelFrame(window, text='icons', padx=5,pady=5)
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


