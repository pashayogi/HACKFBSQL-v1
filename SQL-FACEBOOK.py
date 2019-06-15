#!/bin/usr/python

"""
	Hack FACBOOK SQL

"""

import os
import sys
from time import sleep

def ketik(s):
	for ASU in s + '\n':
		sys.stdout.write(ASU)
		sys.stdout.flush()
		sleep(50. / 1000)

os.system('clear')
print ("""\033[1;31m
         WELCOME TO HACK FACEBOOK SQL
\033[1;31m   ██__________██
___█▒█________█▒█
__█▒███____███▒█
__█▒████████▒▒█
__█▒████▒▒█▒▒██
__████▒▒▒▒▒████
___█▒▒▒▒▒▒▒████
__█▒▒▒▒▒▒▒▒████______█                            _██▒█▒▒▒▒▒█▒▒████__█▒█
_█▒█●█▒▒▒█●█▒▒███_█▒▒█
_█▒▒█▒▒▒▒▒█▒▒▒██_█▒▒█
__█▒▒▒=▲=▒▒▒▒███_██▒█
__██▒▒█♥█▒▒▒▒███__██▒█
____███▒▒▒▒████____█▒█
______██████________███
_______█▒▒████______██
_______█▒▒▒▒▒████__██
_______█▒██▒██████▒█     MR.K7C8NG
_______█▒███▒▒▒█████
_____█▒████▒▒▒▒████
______█▒███▒██████__

""")

a = input("\033[1;33mUsername target/ID: ")
os.system('clear')
print ("\033[1;36m Server SQL: OKE ")
sleep(0.5)
print ("\033[1;36m Cek FACEBOOK VULN. ")
sleep(2)
print ("\033[1;36m Status VULN: Oke!.... ")
print (' ')
print (' ')
print ("\033[1;32m Memulai SQL TARGET..... ")
print (' ')
ketik ("\033[1;32m Mengambil Data SQL....")
sleep(0.5)
ketik ("\033[1;32m Menggunakan SQL FACEBOOK...")
sleep(0.5)
ketik ("\033[1;32m Baypass Access LOG-IN...")
sleep(0.5)
print ("\033[1;32m Baypass Sukses! ")
sleep(1)
print (' ')

ketik ("\033[1;32m Mencari Password SQL... ")
sleep(2)
ketik ("\033[1;32m Mendapatkan Password SQL...")
sleep(0.5)
ketik ("\033[1;32m Baypass LOG-IN SQL ")
sleep(2)
print ("\033[1;32m Baypass LOG-IN SQL Sukses! ")
print (' ')

print ("\033[1;32m Sedang Login FACEBOOK TARGET...")
sleep(3)
print (' ')
print ("\033[1;33m Username : %s" % (a))
print ("\033[1;33m Password : BISA DI UBAH SESUKA HATI KALIAN ")
sleep(3)
print (' ')
print ("\033[1;32m Login Sukses! ")
print (' ')
print ("\033[1;32m Mengubah HALAMAN LOG-IN ")
sleep(2)
print ("\033[1;31m   Sukses! ")
print (' ')
print ("\033[1;32m Menghapus LOG-IN SQL ")
sleep(2)
print ("\033[1;31m   Sukses! ")
print (' ')
sleep(0.5)
print ("""\033[1;35m
Note : Username dan password udah sukses
""")
print (' ')
ketik ("\033[1;33m terimakasih bro 👍 ")

z = open("pass.txt","w")

pesan= """
---------------------
Username: %s" % (a)) 
Password: bisa di ubah
---------------------
	"""
z.write(pesan)
z.close()

os.system('mkdir /sdcard/Hasil')
os.system('mv pass.txt /sdcard/Hasil')
