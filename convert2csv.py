import pandas as pd
import numpy as np

with open("Manhattan_GRE_words.txt", 'r') as f:
	words = [i[i.index('.')+1:].replace("\n", "").strip() for i in f.readlines()]

df = []
for row in words:
	word = row[:row.index(":")].strip()
	meaning = row[row.index(":")+1:].replace(";", "; ").strip()
	try:
		meaning_only = meaning[:meaning.index("Ex:")]
	except:
		try:
			meaning_only = meaning[:meaning.index("ex:")]
		except:
			meaning_only = meaning
	df.append([word[0].upper()+word[1:], meaning, meaning_only])
df = pd.DataFrame(np.array(df))
df.columns = ['Word', 'Meaning', 'Meaning Only']
df.to_csv("GREWordList.csv", index=False)