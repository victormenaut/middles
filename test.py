from stanfordcorenlp import StanfordCoreNLP
import json



#to run sudo python3 file.py
def main():
	nlp = StanfordCoreNLP('/Users/victormena/Development/DPLP/corenlp/', memory='8g')
	file = open('/Users/victormena/Development/middles/xml_to_text/A/A00.xml.txt', 'r')
	a = []
	print('{	', '"sentence"', ': [')
	for line in file:
		props={ 'annotators': 'tokenize, ssplit, pos, parse, depparse'}
		output = nlp.annotate(line, properties=props)

		sem = nlp.semgrex( line, pattern= '{tag: VB}')
		a.append(sem)
	print(']}')
	nlp.close()
	print(len(a))


main()

