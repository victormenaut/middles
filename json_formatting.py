from stanfordcorenlp import StanfordCoreNLP
import json

def main():
    nlp = StanfordCoreNLP('http://localhost', port = 9000, memory='8g')
    with open('initial_output_test.txt', 'r+') as outfile:
        with open('input.txt', 'r', encoding='utf-8') as f:
            # set up core NLP to output json
            data="".join(line.rstrip() for line in f)
            # other stuff: 'tokenize, ssplit, pos'
            props = {'annotators': 'parse', 'pipelineLanguage': 'en', 'outputFormat': 'json'}

            # put the nlp stuff in a json
            json.dump(nlp.annotate(data, properties = props), outfile)
        # data2 = json.load(outfile)

        # for p in data2:
        #     print('Sentences: ' + p['sentences'])
        


main()