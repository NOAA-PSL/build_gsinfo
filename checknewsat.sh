# create global_satinfo file for a given date
date=$1
# loop over satellites
cd build_gsinfo-fix/satinfo
newsats=0
for sat in $(cat satellites); do
    # find matching date, check for use flag=1
    newsat=0
    for f in $sat/*; do
        if [ $f != "$sat/readme" ]; then # skip readme file
           datex=`basename $f`
	   if [ $date -eq $datex ]; then
              useflags=`awk '{print $3}' $f`
	      for flag in $useflags; do
                 if [ $flag -gt 0 ]; then
                    newsat=1
		    ((newsats+=1))
                 fi
              done
           fi
        fi
    done
    if [ $newsat -eq 1 ]; then
       echo "$sat is new"
    fi
done
if [ $newsats -eq 0 ]; then
   echo "no new sats"
fi
exit $newsats
