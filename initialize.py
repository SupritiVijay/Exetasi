import numpy ad np
import pandas as pd

words = pd.read_csv('GREWordList.csv')
n = len(words.Word)
unused_words = [0]*n
fre_mistaken_words = [0]*n
l1 = [0]*n
word_confusion = []

for i in n:
	word_confusion = word_confusion.append(l1)

uw = pd.Dataframe(unused_words, ["Unused_Words_Frequency"])
uw.to_csv("unused_words.csv",index = False)

fre_mw = pd.Dataframe(fre_mistaken_words, ["Frequently Mistaken Words Frequency"])
fre_mw.to_csv("frequently_mistaken_words.csv", index = False)

word_con = pd.Dataframe(word_confusion, words.Word)
word_con.to_csv("word_confusion_matrix.csv", index = False)