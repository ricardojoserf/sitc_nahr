import csv, sys

csvfile = sys.argv[1]
count_row = 0

with open(csvfile, 'r') as fin, open('results/'+csvfile, 'w') as fout:
	reader = csv.reader(fin, lineterminator='\n')
	writer = csv.writer(fout, lineterminator='\n')

	for row in reader:
		if count_row == 0:
			writer.writerow([row[0]] + [row[2]] + [row[4]] + [row[5]] + [row[6]] + [row[7]] + [row[8]] + [row[9]]+ [row[10]] + [row[11]] + [row[3]] + ['media_tri'] + ['media_bin'] + ['total'])
			count_row+=1
		else:
			column=1
			total_pol = 0.0
			count=0
			pol=0.0

			tri_1 = float(row[4])
			tri_2 = float(row[5])
			tri_3 = float(row[6])
			tri_sum = (tri_1 + tri_2 + tri_3)/3.0

			bin_1 = float(row[7])
			bin_2 = float(row[8])
			bin_3 = float(row[9])
			bin_sum = (bin_1 + bin_2 + bin_3)/3.0

			tri_val = "init"
			if (tri_sum > 1.5):
				tri_val = "2"
			elif (tri_sum < 0.5):
				tri_val = "0"
			else:
				tri_val = "1"

			bin_val = "init"
			if (bin_sum > 0.5):
				bin_val = "1"
			else:
				bin_val = "0"

			dic_val = str(row[3])

			total = "init"

			if ((tri_val=="2") and (dic_val=="Nan")):
				total = "Neu"
			elif ( (bin_val=="1" and tri_val=="1")
				or (bin_val=="1" and dic_val=="1")
					or (tri_val=="1" and dic_val=="1") ):
						total = "1"
			elif ( (bin_val=="0" and tri_val=="0")
				or (bin_val=="0" and dic_val=="0")
					or (tri_val=="0" and dic_val=="0") ):
						total = "0"
			else:
				total = "Neu"


			writer.writerow([row[0]] + [row[2]] + [row[4]] + [row[5]] + [row[6]] + [row[7]] + [row[8]] + [row[9]]+ [row[10]] + [row[11]] + [row[3]] + [str(tri_val)] + [str(bin_val)] + [str(total)])
