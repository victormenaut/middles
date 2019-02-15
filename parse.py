import pandas as pd
import ijson
import requests 
import nltk
def main():

	#nlp = StanfordCoreNLP('/Users/victormena/Development/DPLP/corenlp/', memory='8g')
	file = input('Type file ')

	with open(file, 'r') as f:
		objects = ijson.items(f, 'sentence.item')
		columns = list(objects)
		print(columns)

	phrase = []
	dependencies = []
	tokens = []
	for k in range(len(columns)):					# extracts data we need
		for i in columns[k]:						 
			for j in columns[k][i]:
				sent = j['parse']
				dep = j['basicDependencies']
				token = j['tokens']
				phrase.append(sent)
				dependencies.append(dep)
				tokens.append(token)

	for i in tokens:							#removes some stuff to only get part of speech 
		for j in i:
			j.pop('index')
			j.pop('originalText')
			j.pop('characterOffsetBegin')
			j.pop('characterOffsetEnd')
			j.pop('before')
			j.pop('after')


	dep = []
	for i in range(len(dependencies)):			# finds the type of verbs we are looking for 
		for j in dependencies[i]:
			if j['dep'] == 'ROOT':
				verb = j['dependentGloss']
				words = []
				
			if j['governorGloss'] == verb:
				if j['dep'] == 'nsubj':
							noun = j['dependentGloss']
							words.append(noun)
							words.append(verb)
				if j['dep'] == 'advmod':
							adv = j['dependentGloss']
							words.append(adv)
		words.append(i)
		dep.append(words)

	a = []
	for i in range(len(dep)):
		if len(dep[i]) >= 4 :
			a.append(dep[i])

	b = []
	for i in a:								#removes bad data 
		for j in tokens[i[-1]]:
			if j['word'] == i[1]:
				if j['pos'] == 'VB' or j['pos'] == 'VBZ' or j['pos'] == 'VBP':
					b.append(i[-1])
	for i in b:
		for j in tokens[i]:
			print(j['word'], end = ' ')
			if j['word'] == '.':
				print('\n')






main()