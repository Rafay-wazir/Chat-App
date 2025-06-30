import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("172.20.10.6", 9999))

done = False

try:
    while not done:
        message = input("\033[1;34mClient's message:\033[0m ")
        client.send(message.encode('utf-8'))
        if message == "quit":
            done = True
        else:
            response = client.recv(1024).decode('utf-8')
            print(f"\033[1;32mServer's message:\033[0m {response}")
            
except KeyboardInterrupt:
    print("Client interrupted.")
finally:
    client.close()
