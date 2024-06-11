import ncepbufr,sys

# dump contents of bufr file to stdout or to a text file.
# Warning: resulting output may be HUGE.

bufr = ncepbufr.open(sys.argv[1])
hdstr="SAID"
satids = []
while bufr.advance() == 0: # loop over messages.
    while bufr.load_subset() == 0: # loop over subsets in message.
       hdr = bufr.read_subset(hdstr) #parse header string
       satids.append(int(hdr[0][0]))
satids_uniq = list(set(satids))
for sat in satids_uniq:
    print(sat, satids.count(sat))
bufr.close()
