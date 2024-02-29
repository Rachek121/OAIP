a = ('Expanding the space available for living').split()
max_len = len(max(a, key=len))
print(*['*'*(max_len-len(d))+d for d in a], sep="\n")