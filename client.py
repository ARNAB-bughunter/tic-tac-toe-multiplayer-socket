from tkinter import *
from functools import partial 
import tkinter
import tkinter.font as font
import socket
import threading

client=socket.socket()
client.connect(("localhost",9999))

def disable_all_bt():
	for i in bt_list:
		i["state"]=DISABLED

def recive():
	while True:
		msg=(client.recv(2048).decode());
		sym=msg[1]
		if msg[0]=="D":
			disable_all_bt()
			l["text"]="PLAYER '"+msg[1]+"' WIN"
		elif int(msg[0])==1:
			bt1["text"]=sym
			bt1["state"]=DISABLED
		elif int(msg[0])==2:
			bt2["text"]=sym
			bt2["state"]=DISABLED
		elif int(msg[0])==3:
			bt3["text"]=sym
			bt3["state"]=DISABLED
		elif int(msg[0])==4:
			bt4["text"]=sym
			bt4["state"]=DISABLED
		elif int(msg[0])==5:	
			bt5["text"]=sym
			bt5["state"]=DISABLED
		elif int(msg[0])==6: 
			bt6["text"]=sym
			bt6["state"]=DISABLED
		elif int(msg[0])==7:	
			bt7["text"]=sym
			bt7["state"]=DISABLED
		elif int(msg[0])==8:	
			bt8["text"]=sym
			bt8["state"]=DISABLED
		elif int(msg[0])==9:	
			bt9["text"]=sym
			bt9["state"]=DISABLED
			
threading.Thread(target=recive).start()

root=Tk()
root.geometry('300x350')
root.resizable(False,False)
root.config(bg="black")
root.title("CLIENT")
bt_font=font.Font(family='Helvetica', size=55, weight='bold')
l_font=font.Font(family='Helvetica', size=25, weight='bold')


def send_select_bt(x):
	if x==1:
		client.send(bytes(str(x),"utf-8"))
	if x==2:
		client.send(bytes(str(x),"utf-8"))
	if x==3:
		client.send(bytes(str(x),"utf-8"))
	if x==4:
		client.send(bytes(str(x),"utf-8"))
	if x==5:
		client.send(bytes(str(x),"utf-8"))
	if x==6:
		client.send(bytes(str(x),"utf-8"))
	if x==7:
		client.send(bytes(str(x),"utf-8"))						
	if x==8:
		client.send(bytes(str(x),"utf-8"))
	if x==9:
		client.send(bytes(str(x),"utf-8"))		

bt1=Button(root,font=bt_font,text="",bg="black",bd=10,command=partial(send_select_bt,1))
bt1.place(x=0,y=0,width=100,height=100)

bt2=Button(root,font=bt_font,text="",bg="black",bd=10,command=partial(send_select_bt,2))
bt2.place(x=100,y=0,width=100,height=100)

bt3=Button(root,font=bt_font,text="",bg="black",bd=10,command=partial(send_select_bt,3))
bt3.place(x=200,y=0,width=100,height=100)

bt4=Button(root,font=bt_font,text="",bg="black",bd=10,command=partial(send_select_bt,4))
bt4.place(x=0,y=100,width=100,height=100)

bt5=Button(root,font=bt_font,text="",bg="black",bd=10,command=partial(send_select_bt,5))
bt5.place(x=100,y=100,width=100,height=100)

bt6=Button(root,font=bt_font,text="",bg="black",bd=10,command=partial(send_select_bt,6))
bt6.place(x=200,y=100,width=100,height=100)

bt7=Button(root,font=bt_font,text="",bg="black",bd=10,command=partial(send_select_bt,7))
bt7.place(x=0,y=200,width=100,height=100)

bt8=Button(root,font=bt_font,text="",bg="black",bd=10,command=partial(send_select_bt,8))
bt8.place(x=100,y=200,width=100,height=100)

bt9=Button(root,font=bt_font,text="",bg="black",bd=10,command=partial(send_select_bt,9))
bt9.place(x=200,y=200,width=100,height=100)

l=Label(root,font=l_font,text="",bg="black",fg="green",bd=5,relief=RAISED)
l.place(x=0,y=300,width=300,height=50)

bt_list=[bt1,bt2,bt3,bt4,bt5,bt6,bt7,bt8,bt9]

root.mainloop()