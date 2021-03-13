import socket

#   public ip
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
print(s.getsockname()[0])
s.close()

#   Not so easily done on MacOS?
#   local ip
hostname = socket.gethostname()

#   Error
#local_ip = socket.gethostbyname(hostname)
#print(local_ip)

#   0.0.0.0
#local_ip = socket.gethostbyname("")
#print(local_ip)

#host = socket.gethostbyname(socket.gethostname()) # or socket.getfqdn() if the former doesn't work
host = socket.getfqdn(socket.gethostname()) # or socket.getfqdn() if the former doesn't work
print(host)
#local_ip = socket.gethostbyname(hostname)
#print(local_ip)

### importing socket module
#import socket
### getting the hostname by socket.gethostname() method
#hostname = socket.gethostname()
### getting the IP address using socket.gethostbyname() method
#ip_address = socket.gethostbyname(hostname)
### printing the hostname and ip_address
#print(f"Hostname: {hostname}")
#print(f"IP Address: {ip_address}")


