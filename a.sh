#!/bin/sh

for f in *.ann

do
	if cat $(echo "$f") | grep "Negative";then
		echo "0" >> "$f".bien
	elif cat $(echo "$f") | grep "Positive";then
		echo "1" > "$f".bien
	else
		echo "Nan" > "$f".bien
	fi

done
