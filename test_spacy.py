import spacy
nlp=spacy.load('en_core_web_sm')
from timeit import Timer
print('It should take about 10 s.')
test = ['this is a full sentence.'] * 1000
t = Timer(lambda: list(nlp.pipe(test)))
print(t.timeit(number=10))

