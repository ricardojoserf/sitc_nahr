#!/bin/sh

for f in *.txt
do
	coma=","
	comilla="'"
	NAME=`echo "$f" | cut -d'.' -f1`
	txt=$(cat $NAME.txt)
	bien=$(cat $NAME.ann.bien)
	todo=$comilla$txt$comilla$coma$bien
	echo $todo >> results.csv

done
