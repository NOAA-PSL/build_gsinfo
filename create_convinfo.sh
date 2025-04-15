# create global_ozinfo file for a given date
date=$1
cd build_gsinfo-fix/convinfo
#usedate=""
#for datex in [1-2]*; do
#   if [ $date -ge $datex ]; then
#      usedate=$datex
#   fi
#done
## cat matching date file, or quit if date not found
#if [ $usedate != "" ]; then
#    cat $usedate
#else
#    echo "date not found for $sat"
#    exit 1
#fi
cat merged_convinfo.txt
