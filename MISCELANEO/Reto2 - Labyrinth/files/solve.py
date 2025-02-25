from pwn import *

le_time = int(time.time())
log.info("Current time: %d" % le_time)

r = remote("localhost", 5000)

#print(r.recvline())

r.recvuntil(b"> ")
r.sendline(b"newgame")

r.recvuntil(b"> ")

randnums = []

for i in range(25):
	r.sendline(b"left")
	r.recvuntil(b"-- GOING LEFT --")
	r.recvline()
	
	result = r.recvline()
	if b"Oh no..." in result:
		randnums.append(1)
	elif b"right direction" in result:
		randnums.append(0)
	
	r.recvuntil(b"> ")
	r.sendline(b"newgame")
	r.recvuntil(b"> ")
	
prediction_string = "".join(map(str, randnums))
log.info("Prediction string: " + prediction_string)


genseeds = """
2000000 times [ 
	
	%d 1000000 * i^ +
	
	say "Seed: " 
	dup echo
	cr 

	initrandom
	25 times [
		2 random echo
	]
	cr
] 
""" % le_time

open("genrandom.qky", "w").write(genseeds)

log.info("Execute following command to get the seed: pypy3 quackery.py genrandom.qky | grep -B 1 %s | head -1" % prediction_string)

found_seed = input("Enter the seed it found: ").strip()

direction_genstring = """
%s initrandom
25 times [ 2 random drop ]
35 times [ 2 random echo ]
cr
""" % found_seed

open("gendirectionstring.qky", "w").write(direction_genstring)

bitstring = os.popen("pypy3 quackery.py gendirectionstring.qky").read().strip()

log.info("Direction bitstring: %s" % bitstring)

for c in bitstring:
	xx = b""
	
	if c == "0":
		r.sendline(b"left")
		xx = r.recvuntil(b"> ")
	elif c == "1":
		r.sendline(b"right")
		xx = r.recvuntil(b"> ")
		
	if b"CTF" in xx:
		print(xx)
		
r.interactive()
