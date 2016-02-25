#!/usr/bin/env python

from crypt import crypt
from spwd import getspnam
from termcolor import colored

username = raw_input("Username : ")
passlist = ["rootd", "toor", "deneme", "merhaba", "nasil", "bulundu"]

enc_pass  = getspnam(username)[1]


for p in passlist:
	password = crypt(p, enc_pass)
	if password == enc_pass:
		print colored("Pass Found ! : "+p, "green") 
	else:
		print "Try : ", p
