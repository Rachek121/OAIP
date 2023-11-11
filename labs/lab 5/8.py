a = input('')
le = [*map(bin, map(int, a.split()))]
s = [{'digits': len(w)-2, 'units': w.count('1'), 'zeros': w.count('0')-1}for w in le]
print(s)
