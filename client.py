import sys
import curses
import socket
import string
from threading import Thread

def connect_server(HOST, PORT, NICK, IDENT, REALNAME, CHANNEL, s):
    s.connect((HOST, PORT))
    s.send("NICK %s\r\n" % NICK)
    s.send("USER %s %s bot: %s\r\n" % (IDENT, HOST, REALNAME))
    s.send("JOIN %s\r\n" % CHANNEL)
    f = s.makefile()
    return f


#This is the function that reads the data coming to us from a socket!
def read_stuff(sock_out):
    data = sock_out.readline().strip()
    privmsg = "PRIVMSG"
    if privmsg in data:
        array_extract = data.split("!")
        print array_extract
        username = array_extract[0][1:]
        if len(array_extract) == 2:
            message_context = array_extract[1].split(privmsg)
            print message_context
            penultimate_context = message_context[1].split(" :")
            print penultimate_context
            print username, ": ", penultimate_context[1]

if __name__=="__main__":
    nick_inp = raw_input('nick: ')
    host_inp = raw_input('host: ')
    port_inp = raw_input('port: ')
    chan_inp = raw_input('channel: ')
    saketh = socket.socket()
    hostname = host_inp
    port = port_inp
    nick = nick_inp
    ident = nick
    realname = nick
    channel = chan_inp
    finalport = int(port)
    sock_out = connect_server(hostname, finalport, nick,ident, realname, channel,saketh)
    while 1:
        read_stuff(sock_out)
 
        
