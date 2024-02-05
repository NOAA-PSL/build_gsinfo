import os
os.chdir("satinfo")
for satname in sorted(os.listdir(".")):
    if satname == 'historical': continue
    if os.path.isdir(satname): 
        os.chdir(satname)
        dates = os.listdir(".")
        dates.sort()
        if "readme" in dates: dates.remove("readme")
        use_string=[]
        for date in dates[1:]:
            channel_use = [int(x.split()[2]) for x in open(date).readlines()]
            used_channels = channel_use.count(1)
            used_channels_nobc = channel_use.count(4)
            use_string.append(' %s %s' % (date,used_channels+used_channels_nobc))
        print('%13s' % satname,*use_string)
        os.chdir("../")
