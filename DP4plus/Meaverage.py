def unique_sublists(input_list):
    seen = set()
    result = []
    for sublist in input_list:
        sorted_tuple = tuple(sorted(sublist))
        if sorted_tuple not in seen:
            seen.add(sorted_tuple)
            result.append(list(sorted_tuple))
    return result

import math
f = open("result.txt","r")
Alines = f.readlines()
f.close()
f = open("anmr_nucinfo","r")
Blines = f.readlines()
f.close()

MeH = []
for x in Blines:
    if len(x.split()) == 3:
        MeH.append(x.split())
MeH = unique_sublists(MeH)

f = open("result.txt","a")
for labellist in MeH:
    for y in Alines:
        if y.split()[0] in labellist:
            labellist.append(y.split()[2])
    sigmaav = (float(labellist[3]) + float(labellist[4]) + float(labellist[5])) / 3
    f.write(labellist[0] + "/" + labellist[1] + "/" + labellist[2] + "\tMe\t" + str(sigmaav) + "\n")
f.close()