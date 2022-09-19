import os
from collections import OrderedDict
from itertools import repeat
from spacy.tokenizer import Tokenizer
from spacy.lang.en import English
path = "3"
file_list = os.listdir(path)
file_list.sort()

nlp = English()
tokenizer = Tokenizer(nlp.vocab)
tokens_to_doc = {}
for i in range(len(file_list)):
  f = open("3/" + file_list[i], "r")
  tokens = tokenizer(f.read())
  for token in tokens:
    if str(token) in tokens_to_doc.keys():
        tokens_to_doc[str(token)].append(i)
    else:
      tokens_to_doc[str(token)] = [i]

dgaps = {}
for i in range(1, len(file_list)):
  dgaps[i] = 0
for token in tokens_to_doc.keys():
  tokens_to_doc[token] =  list(OrderedDict(zip(tokens_to_doc[token], repeat(None))))
  for i in range(len(tokens_to_doc[token])-1, 0, -1):
    tokens_to_doc[token][i] = tokens_to_doc[token][i] - tokens_to_doc[token][i-1]
    dgaps[tokens_to_doc[token][i]] += 1


f = open("../result/a1.txt", "w")
for k in dgaps.keys():
  if k != 0:
    if k != len(file_list) - 1:
      f.write(str(dgaps[k]) + "\n")
    else:
      f.write(str(dgaps[k]))


