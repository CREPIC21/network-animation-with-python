s1 = 'abc'
b1 = s1.encode('utf-8')
print(type(s1))
print(type(b1))
print(b1)
for b in b1:
    print(b)

s2 = 'ハッキング' # japanese for hacking
b2 = s2.encode()
print(b2)
for b in b2:
    print(b)

s2_decoded = b2.decode()
print(s2_decoded)

