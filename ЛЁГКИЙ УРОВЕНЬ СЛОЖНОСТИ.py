f = open ('17.1.txt')

M = []
k = 0

for x in f.readlines ():
    M.append (int (x))


for i in range (1, len (M)):
    C1, C2 = M [i - 1], M [i]

    if C1 % 7 == 0 or C2 % 7 == 0:

        k += 1

print (k)