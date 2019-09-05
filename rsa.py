#!/usr/bin/python3
import binascii,sys
def viewmenu():
	print("""
		Welcome to my RSA simulation (even tho it's kinda shit)
		You have several different options
		To start type in genkey""")
	printhelp()
	while True:
		ui = input("> ")
		if(ui == "genkey"):
			privatekeygen()
		if(ui == "privkeydetails"):
			print("Modulo: %d\nPrivate exponent: %d\nPublic exponent: %d\nPrime1 (p): %d\nPrime2 (q): %d\n\n" % (n, d, e, p, q))
		if(ui == "pubkeydetails"):
			print("Modulo: %d\nPublic exponent: %d" % (n, e))
		if(ui == "use"):
			message = int(input("Enter number: "))
			c = enc(message)
			print("Encrypted number: %d" % c)
			m = dec(c)
			print("Decrypted number: %d" % m)

def printhelp():
	print("""
		genkey: generate private key
		privkeydetails: view private key details
		pubkeydetails: view public key details
		use: encrypt a number and subsequently get it back
		""")

def privatekeygen():
	global n,p,q,e,d
	p = int(input("Enter prime number p: "))
	q = int(input("Enter prime number q: "))

	n = p*q
	l = lcm(p-1, q-1)

	list_of_coprimes = []

	for i in range(0, l):
		if(gcd(i, l) == 1):
			list_of_coprimes.append(i)

	print("\n\n\n" + ' '.join(str(e) for e in list_of_coprimes))
	e = int(input("Select an exponent from this list of coprimes: "))
	d = modinv(e, l)
def enc(m):
	return m**e % n

def dec(c):
	return c**d % n

def gcd(p,q):
    while q > 0:
        p, q = q, p % q
    return p

def modinv(a, m):
	a = a%m
	x = 0
	while True:
		if((a*x) % m == 1):
			return x
		else:
			x += 1

def lcm(p, q):
    return p * q // gcd(p, q)

def modinv(e, m):
	e = e%m
	for x in range(1, 1000000):
		if((e * x) % m == 1):
			return x
			break;

viewmenu()