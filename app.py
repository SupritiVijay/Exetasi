import streamlit as st
from wordcloud import WordCloud
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import time
from stqdm import stqdm
from recommender import Recommender
from update import update_recommender

streamlit_url = "https://github.com/SupritiVijay/Exetasi"

@st.cache
def generate_wordcloud():
	df = pd.read_csv("GREWordList.csv", usecols=['Word'])
	df = df.values
	word_list = df.flatten()
	np.random.shuffle(word_list)
	word_frequency = {i:1 for i in word_list}
	wordcloud = WordCloud(width=900,height=250,background_color='white',max_words=25,relative_scaling=1,normalize_plurals=False).generate_from_frequencies(word_frequency)
	return wordcloud

@st.cache(ttl=60*10)
def get_word_lists(N):
	r = Recommender(N)
	word_list = r.recommend()
	words = np.array([i for i in word_list.T[0]])
	np.random.shuffle(words)
	return word_list, words

def app(N=10):
	st.sidebar.markdown('![img](./assets/images/moving_logo.gif)')
	st.sidebar.markdown("We present to you, **Exétasi**, an app for learning and revising vocabulary for the GRE tests.")
	st.sidebar.write("This project aims to develop a Life-Long learning Recommendation System for GRE word recommendation.")
	wordcloud = generate_wordcloud()
	fig = plt.figure(figsize = (9, 2.5))
	plt.imshow(wordcloud, interpolation='bilinear')
	plt.axis("off")
	st.pyplot(fig)
	word_list, words = get_word_lists(N=N)
	words = [i for i in words]
	_, center, _ = st.columns([1, 1, 1])
	center.markdown("## All Words")
	st.warning(' | '.join(words))
	col1, col2 = st.columns([3, 1])
	with col1:
		st.markdown("### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Definition")
	with col2:
		st.markdown("### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Word")
	with st.form(key="Form"):
		responses = [None for _ in range(N)]
		expanders = [st.expander(' ', expanded=True) for i in range(N)]
		for index, expander in enumerate(expanders):
			with expander:
				col1, col2 = st.columns([3, 1])
				with col1:
					st.info(word_list[index][2])
				with col2:
					responses[index] = st.selectbox("", words, key=str(index))
		submit_button = st.form_submit_button(label="SUBMIT")
		if submit_button:
			update_recommender([i for i in word_list.T[0]], responses)
			performance = [1 if i==j else 0 for i,j in zip(word_list.T[0], responses)]
			performance_p = sum(performance)/len(performance)
			st.success("You got a Score of:\t" +str(round(100*performance_p, 2))+"% Congratulations!")
			link = "https://twitter.com/intent/tweet?text=Exetasi%20Score:%20"+str(sum(performance))+"%20Out%20of%2010%21%0A%0ACheck%20Out%20Exetasi%20below%3A&hashtags=exetasi&url="+streamlit_url
			st.markdown("[Post on Twitter]("+link+")")
			st.markdown("---")
			st.markdown("## Detailed Analysis")
			st.markdown("### Correct Words:")
			st.success(" | ".join([i for i,j in zip(word_list.T[0], responses) if i==j]))
			st.markdown("### Incorrect Words")
			col_definition, col_appropriate, col_chosen = st.columns([3, 1, 1])
			with col_definition:
				st.markdown("#### Definition")
			with col_appropriate:
				st.markdown("#### Correct Response")
			with col_chosen:
				st.markdown("#### Your Response")
			definitions = [word_list[i][2] for i in range(N) if word_list[i][0]!=responses[i]]
			appropriate = [word_list[i][0] for i in range(N) if word_list[i][0]!=responses[i]]
			chosen = [responses[i] for i in range(N) if word_list[i][0]!=responses[i]]
			expenders_details = [st.expander(' ', expanded=True) for i in range(len(chosen))]
			for index_details, expander_details in enumerate(expenders_details):
				col_definition, col_appropriate, col_chosen = st.columns([3, 1, 1])
				with col_definition:
					st.info(definitions[index_details])
				with col_appropriate:
					st.warning(appropriate[index_details])
				with col_chosen:
					st.error(chosen[index_details])


if __name__ == '__main__':
	app()