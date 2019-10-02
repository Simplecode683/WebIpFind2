import socket

host = input("Please input a valid host address. If invalid, the script will crash:")

ip = socket.gethostbyname(host)

print("-" * 80)
print("The Ip You're Looking For Is", ip)
print("-" * 80)
print ("Thanks for using this script, my next project is an updated port scanner (:")
