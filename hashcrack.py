# md5 hash cracker offline
# author - gospel chukwunonso
#!/bin/python3
import hashlib
import time
import os
from cfonts import render
import random
import sys
from colorama import Fore

if os.name == 'nt':
   os.system('cls')
else:
   os.system('clear')

print(render('hashcrack',colors=['blue','yellow']))

if len(sys.argv) == 3:
   pass
else:
   print(Fore.YELLOW+'\n[+] Usage - python hashcrack.py -h "md5"\n')
   exit(1)

if '-h' in sys.argv:
   pass
else:
   print(Fore.RED+'\n[+] An Error Occured!\n'+Fore.WHITE)
   exit(1)

md5_hash = sys.argv[2]
wordlist = 'rockyou.txt'
wordlist1 = 'rockyou_1.txt'
wordlist2 = 'rockyou_2.txt'
wordlist3 = 'names.txt'

def hashcrack():
    global md5_hash
    global wordlist
    global wordlist1
    global wordlist2
    global wordlist3

    print(Fore.BLUE+f'\n[+] Md5 Hash - {md5_hash}')
    print(Fore.WHITE+f'\n[+] Wordlists - [wordlist, wordlist-1, wordlist-2, wordlist-3]\n')
    print(Fore.YELLOW+'[!] Cracking Hash...\n')
    time.sleep(1.5)
    openrd = open(wordlist, 'r')
    openrd1 = open(wordlist1, 'r')
    openrd2 = open(wordlist2, 'r')
    openrd3 = open(wordlist3, 'r')
    for word in openrd:
        hash_all = hashlib.md5(word.strip('\n').encode()).hexdigest()
        if md5_hash == hash_all:
           time.sleep(random.uniform(1.1, 1.0))
           print(Fore.GREEN+f'[*] [-Wordlist-] Hash String Found - {word}')
           break
        else:
           for word in openrd3:
               hash_all = hashlib.md5(word.strip('\n').encode()).hexdigest()
               if md5_hash == hash_all:
                  time.sleep(random.uniform(1.1, 1.0))
                  print(Fore.GREEN+f'[*] [-Wordlist-3-] Hash String Found - {word}')
                  break
               else:
                  for word in openrd2:
                      hash_all = hashlib.md5(word.strip('\n').encode()).hexdigest()
                      if md5_hash == hash_all:
                         time.sleep(random.uniform(1.1, 1.0))
                         print(Fore.GREEN+f'[*] [-Wordlist-2-] Hash String Found - {word}')
                         break
                      else:
                         for word in openrd1:
                             hash_all = hashlib.md5(word.strip('\n').encode()).hexdigest()
                             if md5_hash == hash_all:
                                time.sleep(random.uniform(1.1, 1.0))
                                print(Fore.GREEN+f'[*] [-Wordlist-1-] Hash String Found - {word}'+Fore.WHITE)
                                break



hashcrack()
