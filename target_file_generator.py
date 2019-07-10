#!/usr/bin/python
_author_ = 'tarah'
#Simple script to generate target text files with IPv4 address ranges. Commonly used for nmap, unicorn, onetwopunch, and other offensive security enumeration tools.
#Complain to me on Twitter at @tarah or at tarah.org. Or don't. Whichever. 
#Help others by improving this script (my god, error handling ***IS*** a thing!) at @tarahmarie on Github. 

import ipaddress
import sys
import argparse

parser = argparse.ArgumentParser(description='This script generates a custom text file of 256 IPv4 addresses for use as target files for nmap, onetwopunch, and other iterators and enumerators.')

def readOctetFromUser(query):
    try:
        userInput = raw_input(query)
        verifiedInput = False
        while not verifiedInput:
            if userInput.isdigit():
                userInputInt = int(userInput)
                if userInputInt >= 0 and userInputInt < 256:
                    verifiedInput = True

            if not verifiedInput:
                print ('\'%s\' is not a valid octet. Please try again: (Or press Ctrl-C to quit' % userInput)
                userInput = raw_input()

        return userInput
    except KeyboardInterrupt:
        quit(1)

userInput1 = readOctetFromUser('Input the first octet of the address: ')
userInput2 = readOctetFromUser('Input the second octet of the address: ')
userInput3 = readOctetFromUser('Input the third octet of the address: ')
userInput4 = str(raw_input('What do you want the text file to be named?: '))
print userInput4

print ("First octet is: %s" % userInput1 )
print ("Second octet is: %s" % userInput2 )
print ("Third octet is: %s" % userInput3 )

preface = str(userInput1) + "." + str(userInput2) + "." + str(userInput3) + "."

print preface

address = preface + "0/24"

uni = unicode(address, "utf-8")

filename = userInput4
print filename

with open(filename, "w+") as f:
    for ip in ipaddress.IPv4Network(uni):
        f.write(str(ip) + '\n')

print "Successfully created a file named " + filename + " here, with 256 IP addresses and your specified octets."
