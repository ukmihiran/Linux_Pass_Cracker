#!/usr/bin/python
# -*- coding: utf-8 -*-

import os,sys
import crypt
import codecs
from datetime import datetime,timedelta
import argparse
today = datetime.today()

def testPass(cryptPass,user):               #testPass function for parse the password part to determine the type of hash, the salt and the password

    pwdList = open ('/home/ukmihiran/Desktop/passlist.txt','r')    #Path to password List
    ctype = cryptPass.split("$")[1]                 #split out ID from the encrypted Password

    if ctype == '6':                                #ID in the encrypted Password field
        print "[+] Hash type SHA-512 detected..."
        print "[+] Cracking Password..."
        salt = cryptPass.split("$")[2]                 #split out salt value from the encrypted encrypted Password
        insalt = "$" +ctype+ "$" +salt+ "$"             # ID and salt in crypt function format
        for word in pwdList.readlines():
            word = word.strip('\n')
            cryptWord = crypt.crypt(word,insalt)        #Encrypting all the word in wordList file
            if (cryptWord == cryptPass):
                time = time = str(datetime.today() - today)     #time for Cracking Password
                print "[+] Found Password for user: " +user+ " as ========> " +word+ " Time: " +time+"\n"
                return
            else:
                print "Nothing Found, Trying With other password..."
                exit

def main():

    parse = argparse.ArgumentParser(description='A simple Linux Password cracker.')
    parse.add_argument('-f', action='store', dest='path', help='Path to shadow file, example: \'/etc/shadow\'')         #add argument for /etc/shadow file
    argus = parse.parse_args()
    if argus.path == None:
        parse.print_help()
        exit
    else:
        hashList = open (argus.path,'r')                    #Load List of hashes from /etc/shadow file
        for line in hashList.readlines():
            line = line.replace("\n","").split(":")
            if not line[1] in ['x', '*', '!' ]:             #exclude the password with ‘x’. ‘*’,’!’, characters
                user = line[0]
                cryptPass = line[1]
                testPass(cryptPass,user)

if __name__ == "__main__":
    main()
