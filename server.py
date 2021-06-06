import threading
import socket

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('localhost',9999))
server.listen()
print("Server listing........")

clients_list=[]
total_client=0
symbol=1
board=["0","1","2","3","4","5","6","7","8"]

def check():
	if board[0]==board[1]==board[2]:
		return True
	elif board[3]==board[4]==board[5]:
		return True
	elif board[6]==board[7]==board[8]:
		return True
	elif board[0]==board[3]==board[6]:
		return True	
	elif board[1]==board[4]==board[7]:
		return True
	elif board[2]==board[5]==board[8]:
		return True	
	elif board[0]==board[4]==board[8]:
		return True
	elif board[2]==board[4]==board[6]:
		return True
	else:
		False
		
def set_text_list(msg,sym):
	if int(msg)==1:
		board[0]=sym
	elif int(msg)==2:
		board[1]=sym
	elif int(msg)==3:
		board[2]=sym
	elif int(msg)==4:
		board[3]=sym
	elif int(msg)==5:
		board[4]=sym			
	elif int(msg)==6:
		board[5]=sym
	elif int(msg)==7:
		board[6]=sym
	elif int(msg)==8:
		board[7]=sym
	elif int(msg)==9:
		board[8]=sym				

def handel_client(conn,addr):
	global symbol
	while True:
		msg=(conn.recv(2048).decode())
		print("<Data Recived:>",msg)
		for i in clients_list:
			if symbol%2!=0:
				i.send(bytes(msg+"X","utf-8"))
				set_text_list(msg,"X")
				print("<Data Send:>","X")
			else:
				i.send(bytes(msg+"O","utf-8"))
				set_text_list(msg,"O")
				print("<Data Send:>","O")
		if check():
			if symbol%2!=0:
				p="X"
			else:
				p="O"
			for i in clients_list:
				i.send(bytes("D"+p,"utf-8"))				
		symbol+=1

def handel_connection():
	global total_client
	while True:
		conn,addr=server.accept()
		print("Client connected.....")
		total_client+=1
		if total_client<=2:
			clients_list.append(conn)
			threading.Thread(target=handel_client,args=(conn,addr)).start()
		else:
			break

if __name__ == '__main__':
	handel_connection()