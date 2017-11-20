f = int(input('>>'))
stara = 0
nova = 1
while f > 0:
    print (stara)
    nova = stara + nova
    stara = nova - stara
    f += -1
print()