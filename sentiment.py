from polyglot.text import Text
import csv

csvfile = 'Ile-de-France.csv'

with open(csvfile, 'r') as fin, open('2_'+csvfile, 'w') as fout:
	reader = csv.reader(fin, lineterminator='\n')
	writer = csv.writer(fout, lineterminator='\n')

	for row in reader:
		column=1
		text = Text((row[column]), hint_language_code='fr')
		total_pol = 0.0
		count=0
		pol=0.0

		for w in text.words: 
			if(w.polarity!=0):
				total_pol += w.polarity
				count+=1
		if count!=0:
			pol = float(total_pol)/float(count)
		
		rounded_pol="0"
		if pol<0:
			rounded_pol = "0"
		elif pol == 0:
			rounded_pol = "Nan"
		else:
			rounded_pol = "1"
		writer.writerow(row + [str(pol)] + [rounded_pol])