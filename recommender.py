import pandas as pd
import numpy as np

class Recommender:
	def __init__(self, N=20, alpha = 0.5):
		self.N = N
		self.data = self.read_data()
		self.alpha = alpha

	def read_data(self):
		df = pd.read_csv('GREWordList.csv')
		df = df.values
		return df

	def recommend(self):
		np.random.shuffle(self.data)

		unused_word = pd.read_csv('./data/unused_words.csv')
		unused_word = unused_word.values
		unused_word = unused_word.flatten()
		un_word_sum = np.sum(unused_word, axis=None)
		if (un_word_sum!=0):
			unused_word = unused_word/un_word_sum
		# print(unused_word)
		unused_word = 1 - unused_word
		# print(unused_word)

		fre_mistaken_words = pd.read_csv('./data/frequently_mistaken_words.csv')
		fre_mistaken_words = fre_mistaken_words.values
		fre_mistaken_words = fre_mistaken_words.flatten()
		fre_mistaken_sum = np.sum(fre_mistaken_words, axis=None)
		if (fre_mistaken_sum!=0):
			fre_mistaken_words = fre_mistaken_words/fre_mistaken_sum
		# print(fre_mistaken_words)
		
		base_array_without_sort = (self.alpha * unused_word) + ((1-self.alpha)*fre_mistaken_words)
		base_order = np.argsort(base_array_without_sort)
		base_words = base_order[:self.N]
		# print(base_words)

		word_confusion = pd.read_csv('./data/word_confusion_matrix.csv')
		word_confusion = word_confusion.values
		words_confused = word_confusion[base_words]
		words_confused = words_confused[:,1:]
		words_confused_sum = np.sum(words_confused, axis = 0)
		# words_confused_sum = np.delete(words_confused_sum, base_words)
		words_confused_sum = np.argsort(words_confused_sum)
		words_confused_sum = np.array([i for i in words_confused_sum if i not in base_words])
		# print(words_confused_sum.shape)
		other_words = words_confused_sum[:self.N]
		# print(other_words)

		base_words = self.data[base_words]
		other_words = self.data[other_words]
		recommended_words = np.concatenate((base_words, other_words), axis=0)
		np.random.shuffle(recommended_words)
		# print(np.unique(recommended_words.T[0]).shape)
		
		return recommended_words

r = Recommender()
r.recommend()