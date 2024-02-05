import sys
satinfo1 = open(sys.argv[1]) # satinfo file built by create_satinfo.sh
satinfo2 = open(sys.argv[2]) # reference satinfo file
satinfo_dict1={}
for line in satinfo1:
    if not line.startswith('#'):
        linesplit = line.split()
        key = linesplit[0]+' '+linesplit[1]
        satinfo_dict1[key]=line[:-1]
satinfo_dict2={}
for line in satinfo2:
    if not line.startswith('#'):
        linesplit = line.split()
        key = linesplit[0]+' '+linesplit[1]
        satinfo_dict2[key]=line[:-1]
k1 = sorted(satinfo_dict1)
k2 = sorted(satinfo_dict2)
for k in k1:
    if k in k2:
        if satinfo_dict1[k] != satinfo_dict2[k]:
            print(k)
            print('satinfo1:',satinfo_dict1[k])
            print('satinfo2:',satinfo_dict2[k])
    else:
        if satinfo_dict1[k].split()[2] != '-1':
            print(k)
            print('satinfo1:',satinfo_dict1[k])
            print('satinfo2:','**missing**')
for k in k2:
    if k not in k1:
        if satinfo_dict2[k].split()[2] != '-1':
            print(k)
            print('satinfo1:','**missing**')
            print('satinfo2:',satinfo_dict2[k])

