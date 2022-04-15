# raspberypi0rubberducky
Rubber ducky raspberry pi 0 reverse shell 

This project executes a reverse shell on a windows 10 computer.
The file payload.ps1 needs to be on a computer which is port forwarded, 
this attacker computer then also runs netcat using nc -lnvp <port> and also has a php server running using php -s 0.0.0.0:80. 
The rubber ducky then executes payload.txt using payload.py, disabling windows defender and then giving the attacker a reverse shell.
The payload is in a loop with a try catch statement, meaning that when the victim loses connection it will try and connect to the attacker until it gets a connection.
Currently this can be stopped by simply closing the powershell process in task manager or by turning off the computer, to work around these I would have
to create some sort of executable that runs the scripts on startup and is undetectable by windows defender or turns off windows defender.
