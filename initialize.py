import numpy as np
import pandas as pd

words = pd.read_csv('GREWordList.csv')
n = len(words.Word)
unused_words = [0]*n
fre_mistaken_words = [0]*n
l1 = [0]*n
word_confusion = [l1]*n

uw = pd.DataFrame(unused_words, columns=["Unused_Words_Frequency"])
uw.to_csv("./data/unused_words.csv",index = False)

fre_mw = pd.DataFrame(fre_mistaken_words, columns=["Frequently Mistaken Words Frequency"])
fre_mw.to_csv("./data/frequently_mistaken_words.csv", index = False)

word_con = pd.DataFrame(word_confusion, columns=words.Word, index=words.Word)
word_con.to_csv("./data/word_confusion_matrix.csv")