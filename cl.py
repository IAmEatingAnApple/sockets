import socket

sip = "0.0.0.0"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((sip, 30000))
sock.send("adjbakdadk")

sock.close()
