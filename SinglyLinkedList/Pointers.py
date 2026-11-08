# id() - funkcija ispisuje adresu unutar memeorije
# is - operator koji provjerava da li objkti imaju istu adresu u memoriji

# Immutable objects (int)
x = 5
y = x

print("Memory adresa objekta x je: " + str(id(x)))
print("Memory adresa objekta y je: " + str(id(y)))
print("Da li su objekti isti? " + str(str( x is y)))

x += 1
print("Memory adresa objekta x uvećanog za jedan je: " + str(id(x)))


# Mutable object

moja_lista = [1,2,3]
print("Memory adresa objekta moja_lista je: " + str(id(moja_lista)))

moja_lista.append(4)
print("Memory adresa objekta moja_lista nakon dodavanja dodatnog elementa je: " + str(id(moja_lista)))

# PyInterning and pyOptimization

x = 20
y = 19 + 1
print("Da li su objekti isti? " + str(str( x is y)))

s1 = "Python!"
print("Memory adresa objekta s1 je: " + str(id(s1)))
s2 = "Python!"
print("Memory adresa objekta s2 je: " + str(id(s2)))
print("Da li su objekti isti? " + str(str( s1 is s2)))