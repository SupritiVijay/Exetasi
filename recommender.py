import pandas as pd
import numpy as np

class Recommender:
	def __init__(self, N=20, path='GREWordList.csv'):
		self.N = N
		self.path = path
		self.data = self.read_data()

	def read_data(self):
		df = pd.read_csv(self.path)
		df = df.values
		return df

	def recommend(self):
		np.random.shuffle(self.data)
		return self.data[:self.N]