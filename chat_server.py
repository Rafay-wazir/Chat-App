import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("172.20.10.6", 9999))
server.listen()

client, addr = server.accept()

done = False

try:
    while not done: 
        msg = client.recv(1024).decode('utf-8')
        if msg == 'quit':
            done = True
        else:
            print(f"\033[1;32mClient's message:\033[0m {msg}")
            response = input("\033[1;34mServer's message:\033[0m ")
            client.send(response.encode('utf-8'))
except KeyboardInterrupt:
    print("Server interrupted.")
finally:
    server.close()