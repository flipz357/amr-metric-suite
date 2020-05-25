#!/bin/bash

# Evaluation script. Run as: ./evaluation.sh <parsed_data> <gold_data>


VECS="../vectors/glove.6B.100d.txt"
SF="cosine"
TAU="0.5"
DIFFSENSE="0.5"

# Evaluation script. Run as: ./evaluation.sh <parsed_data> <gold_data>
out=`python2 smatch/s2match.py --pr -f "$1" "$2" -vectors $VECS -similarityfunction $SF -cutoff $TAU -diffsense $DIFFSENSE`
out=($out)
echo 'S2match -> P: '${out[1]}', R: '${out[3]}', F: '${out[6]} | sed 's/.$//'

python unlabel.py "$1"  > 1.tmp
python unlabel.py "$2"  > 2.tmp
out=`python2 smatch/s2match.py --pr -f 1.tmp 2.tmp -vectors $VECS -similarityfunction $SF -cutoff $TAU -diffsense $DIFFSENSE`
out=($out)
echo 'Unlabeled -> P: '${out[1]}', R: '${out[3]}', F: '${out[6]} | sed 's/.$//'

cat "$1" | perl -ne 's/(\/ [a-zA-Z0-9\-][a-zA-Z0-9\-]*)-[0-9][0-9]*/\1-01/g; print;' > 1.tmp
cat "$2" | perl -ne 's/(\/ [a-zA-Z0-9\-][a-zA-Z0-9\-]*)-[0-9][0-9]*/\1-01/g; print;' > 2.tmp
out=`python2 smatch/s2match.py --pr -f 1.tmp 2.tmp -vectors $VECS -similarityfunction $SF -cutoff $TAU -diffsense $DIFFSENSE`
out=($out)
echo 'No WSD -> P: '${out[1]}', R: '${out[3]}', F: '${out[6]} | sed 's/.$//'

cat "$1" | perl -ne 's/^#.*\n//g; print;' | tr '\t' ' ' | tr -s ' ' > 1.tmp
cat "$2" | perl -ne 's/^#.*\n//g; print;' | tr '\t' ' ' | tr -s ' ' > 2.tmp
python2 scores-enhanced-s2align.py "1.tmp" "2.tmp" $VECS $SF $TAU $DIFFSENSE

rm 1.tmp
rm 2.tmp
