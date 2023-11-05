message = ('ППррииввеетт!! ККаакк ддееллаа?? ССееггоодднняя ттааккааяя ххоорроошшааяя ппооггооддаа, ммоожжеетт '
           'ппооггуулляяеемм??')
message2 = ''
for i in range(len(message)):
    if i == len(message) - 1 or message[i] != message[i+1]:
        message2 += message[i]
        print(message2)
