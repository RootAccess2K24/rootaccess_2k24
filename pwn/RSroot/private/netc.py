#!/usr/bin/python

import socketserver
import time
import threading
import pwn

class Service(socketserver.BaseRequestHandler):
	def handle(self):
		# this is where we will handle the connection , do what we want to do once someone connects 
		print("Someone Connected")
		io = pwn.process("./server")
		self.send(io.recvline().decode())
		self.send(io.recvline().decode())
		self.send(io.recvline().decode())
		self.send(io.recvline().decode())
		self.send(io.recvline().decode())
		self.send(io.recvline().decode())
		self.send(io.recvline().decode())
		self.send(io.recvline().decode())
		self.send(io.recvline().decode())
		self.send(io.recvline().decode())
		self.send(io.recvline().decode())
		self.send(io.recvline().decode())
		self.send(io.recvline().decode())
		self.send(io.recvline().decode())
		self.send(io.recvline().decode())
		self.send(io.recvline().decode())
		entered = self.recieve()
		io.sendline(entered)
		self.send(io.recvline().decode())

	def send(self, string , newline = True):
		if newline: string = string 
		self.request.sendall(bytes(string,'utf-8')) 	# this request object is internal to the base request handler 

	def recieve(self, prompt = ">"):
		self.send(prompt, newline= False)
		return self.request.recv(4096).strip()

class TheadedService(socketserver.ThreadingMixIn , socketserver.TCPServer , socketserver.DatagramRequestHandler):
	#this class doesn't need to anything but we need it to exist to make the threaded service and serve it up
	pass


def main():
	port = 6667			# port to run the challenge
	host = "0.0.0.0"	# visible to LAN

	service = Service

	# server object , using host and port , hosting our service
	server = TheadedService((host,port),service)

	# make the port reusable
	server.allow_reuse_address = True

	# thread the service ! 
	server_thread = threading.Thread(target = server.serve_forever)
	server_thread.start()

	print("Server started on port", port)

	# wait and do nothing
	while True : time.sleep(60)

if __name__ == "__main__":
	main()