#to convert cvs file to json
import csv
import json

csvfile = open('faq.csv','r',encoding='utf8')
jsonfile = open('file.json', 'w')

fieldnames = ("Question User says","Other possible phases /training phases","Entity in this line","Text Response")
reader = csv.DictReader( csvfile, fieldnames)
lis=["Question User says","Other possible phases /training phases","Entity in this line","Text Response"]
for row in reader:
	json.dump(row, jsonfile)
	jsonfile.write('\n')	
