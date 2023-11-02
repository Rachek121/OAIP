b = int(input(">>>"))
a = int(input(">>>"))
c = b % a
if c != 0:
    print(">>>", b // a + 1)
else:
    print(">>>", b // a)
