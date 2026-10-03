import math
p=7919
q=1009
n=p*q
phi=(p-1)*(q-1)
for e in range(2, phi):
    if math.gcd(e, phi)==1:
        break
for d in range(2, phi):
    if (e*d)%phi==1:
        break
print("Pubic key:", (e, n))
print("Private key:", (d, n))
m=int(input("Enter message(number): "))
c=pow(m,e,n)
print("Encrypted message:", c)
decrypted=pow(c,d,n)
print("Decrypted message:", decrypted)  