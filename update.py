import pandas as pd
import numpy as np

def update_recommender(original_words, selected_words):
	word_confusion = pd.read_csv('./data/word_confusion_matrix.csv')
	word_confusion = word_confusion.values
	words = word_confusion.T[0]

	fre_mistaken_words = pd.read_csv('./data/frequently_mistaken_words.csv')
	fre_mistaken_words = fre_mistaken_words.values

	unused_word = pd.read_csv('./data/unused_words.csv')
	unused_word = unused_word.values

	for i in range(len(original_words)):
		original_word_index = np.argwhere(words==original_words[i])[0][0]
		if(original_words[i]!=selected_words[i]):
			# print(original_word_index)
			fre_mistaken_words[original_word_index]+=1
			selected_word_index = np.argwhere(words==selected_words[i])[0][0]
			word_confusion[original_word_index][selected_word_index+1]+=1
			word_confusion[selected_word_index][original_word_index+1]+=1

		unused_word[original_word_index]+=1

	uw = pd.DataFrame(unused_word, columns=["Unused_Words_Frequency"])
	uw.to_csv("./data/unused_words.csv",index = False)

	fre_mw = pd.DataFrame(fre_mistaken_words, columns=["Frequently Mistaken Words Frequency"])
	fre_mw.to_csv("./data/frequently_mistaken_words.csv", index = False)

	word_con = pd.DataFrame(word_confusion, columns=["Word"]+[i for i in words])
	word_con.to_csv("./data/word_confusion_matrix.csv", index = False)


if __name__ == '__main__':
	update_recommender(['Abrasive','Bickering','Blight','Cloying','Construe','Culmination'], ['Abrasive','Cloying','Construe','Bickering','Blight','Culmination'])