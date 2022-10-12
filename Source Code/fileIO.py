# fileName = 'inputFile.txt'
# f = open(fileName,'r')
# output1 = "PassFile.txt"
# output2 = "FailFile.txt"
# passFile = open(output1,'w')
# failFile = open(output2, 'w')
# for line in f:
#     line_split = line.split()
#     if line_split[2] == "P":
#         passFile.write(line)
#     # else:
#         failFile.write(line)
# passFile.close()
# failFile.close()

import linecache


f = open('inputFile.txt', 'r')
passFile = open ('PassFile.txt', 'w')
failFile = open('FailFile.txt', 'w')
count = 0
for line in f:
    line_split = line.split()
    if line_split[2] == 'P':
        passFile.write(line)
    else:
        failFile.write(line)       
f.close()
passFile.close()
failFile.close()
