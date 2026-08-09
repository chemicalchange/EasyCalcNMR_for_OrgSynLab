#By Qidong Xia 2026.5.2
import math
f = open("E_summary.txt","r")
Alines = f.readlines()
f.close()
f = open("iso_summary.txt","r")
Blines = f.readlines()
f.close()
nc = len(Alines)

data = []
for i in range(nc):
    data.append([])

k = -1
for x in Alines:
    k += 1
    data[k].append("E")
    data[k].append(x.split()[4])
k = -1
for x in Blines:
    if ".out" in x:
        k += 1
    if "C    Isotropic" in x:
        data[k].append(x.split()[0] + "\t" + "C")
        data[k].append(x.split()[4])

for i in range(nc):
    deltaG = (float(data[i][1])-float(data[0][1]))*2625.5*1000
    ratio = math.exp(-deltaG/(298.15*8.3145))
    data[i].append(ratio)
sum = 0
for i in range(nc):
    sum += data[i][-1]
for i in range(nc):
    data[i][-1] /= sum

f = open("result.txt","w")
for i in range(nc):
    f.write("contribution of conformer %d: %.2f\n" % (i + 1,data[i][-1]))
for j in range (len(data[0])):
    sigmaav = 0
    if "C" in str(data[0][j]):
        f.write(data[0][j] + "\t")
    elif (j > 1) and (j < len(data[0]) - 1):
        for i in range(nc):
            sigmaav += float(data[i][j]) * data[i][-1]
        f.write(str(sigmaav) + '\n')
f.close()