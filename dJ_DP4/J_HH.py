f = open("result.txt","r")
Alines = f.readlines()
f.close()
f = open("J_summary.txt","r")
Blines = f.readlines()
f.close()

nc = 0
ratio = []
Hlabel = []
for x in Alines:
    if "conformer" in x:
        nc += 1
        ratio.append(x.split()[4])
    if x.split()[1] == "H":
        Hlabel.append(x.split()[0])
nHatom = len(Hlabel)

Jlist = []
for i in range(nc):
    Jlist.append([])
    for j in range(nHatom):
        Jlist[i].append([])

data = []
for i in range(nc):
    data.append([])

k=-1
for x in Blines:
    if ".out" in x:
        k += 1
    if "E" in x:
        data[k].append(x.split())

for i in range(nc):
    for label1 in Hlabel:
        for label2 in Hlabel:
            if label2 >= label1:
                combined_label2line = []
                for x in data[i]:
                    if x[0] == label2:
                        combined_label2line += x
                combined_label2line=list(dict.fromkeys(combined_label2line))
                Jlist[i][Hlabel.index(label1)].append((combined_label2line)[int(label1)])

for j in range(nHatom):
    for i in range(nc):
        Jlist[i][j][0] = "X"
        while len(Jlist[i][j]) < nHatom:
            Jlist[i][j].insert(0,"X")

avJlist = []
for i in range(nHatom):
    avJlist.append([])
    for j in range(nHatom):
        if i >= j:
            avJlist[i].append("X")
        else:
            avJlist[i].append(0)

for i in range(nc):
    for j in range(nHatom):
        for k in range(nHatom):
            if Jlist[i][j][k] != "X":
                avJlist[j][k] += float(Jlist[i][j][k]) * float(ratio[i])

f = open("J_result.csv","w")
for label in Hlabel:
    f.write("," + label)
f.write("\n")
for i in range(nHatom):
    f.write(Hlabel[i])
    for j in range(nHatom):
        if i < j:
            f.write("," + "%.2f" % avJlist[i][j])
        else:
            f.write("," + avJlist[i][j])
    f.write("\n")
f.close()