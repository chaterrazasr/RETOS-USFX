sharedPrime = 231   # p (Fault in implementation, this is not a Prime number ;)
sharedBase = 5      # g

aliceSecret = 6     # a 
bobSecret = 15      # b (Value between 1 and 10000)


print("Publicly Shared Variables:")
print("> Shared Prime: " , sharedPrime)
print("> Shared Base:  " , sharedBase)

# Alice Sends Bob A = g^a mod p
A = (sharedBase**aliceSecret) % sharedPrime
print("Alice Sends Over Public Chanel: " , A)

# Bob Sends Alice B = g^b mod p
B = (sharedBase ** bobSecret) % sharedPrime
print("Bob Sends Over Public Chanel: ", B)

print("------------")
print("Privately Calculated Shared Secret:")
# Alice Computes Shared Secret: s = B^a mod p
aliceSharedSecret = (B ** aliceSecret) % sharedPrime
print("> Alice Shared Secret: ", aliceSharedSecret )

# Bob Computes Shared Secret: s = A^b mod p
bobSharedSecret = (A**bobSecret) % sharedPrime
print("> Bob Shared Secret: ", bobSharedSecret)

