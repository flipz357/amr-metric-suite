#!/usr/bin/env bash

#input A (if parser vs gold: parser)
A=$1

#input B (if parser vs gold: gold)
B=$2

cd py2-Smatch-and-S2match
echo "calculating smatch and sub-task metrics based on smatch alignment"
echo "------------------------------------------"
./evaluation-fixed-smatch.sh ../$A ../$B
echo "------------------------------------------"
echo "------------------------------------------"
echo "calculating s2match and subtask metrics based on s2match alignment; params: vectors = glove 100d, sim = cosim, threshold = 0.5"
echo "------------------------------------------"
./evaluation-fixed-s2match.sh ../$A ../$B
echo "------------------------------------------"
echo "------------------------------------------"
cd ..
echo "graph structure error"
echo "------------------------------------------"
python graph-structure-error/graph_structure_error.py -f $A $B
echo "------------------------------------------"
echo "EVALUATION COMPLETE"
echo "------------------------------------------"
