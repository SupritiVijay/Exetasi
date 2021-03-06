# [Exetasi](https://share.streamlit.io/supritivijay/exetasi/main/app.py)
[Link to Project](https://share.streamlit.io/supritivijay/exetasi/main/app.py)

## Origin of Project

This project aims to develop a Life-Long learning Recommendation System for GRE word recommendation. The Graduate Record Examinations (GRE) is a standardized test that is an admissions requirement for many graduate schools in the United States and Canada and few in other countries. Standard Recommendation Systems can be classified into three major categories:
1. User-Based Filtering
2. Item-Based Filtering
3. Stereotypes/Demographics-Based Filtering

The project aims to develop two varieties of filtering systems, primarily:
1. **User-Based Filtering and Item-Based Filtering:** This methodology would better supplement traditional Item-Based Filtering with User-Based Filtering to provide revision schemes for individual/targetted students.
2. **Stereotypes/Demographics-Based Filtering and Item-Based Filtering:** This methodology aims to encapsulate a broad selection of weak words for a larger demographic. This filtering methodology aims to be readily deployable in a public setting, where a large number of people will be accessing and using the project.

## Parameters of Concern:

We aim to utilize the following parameters as base quantifiers for word recommendations for the above algorithms. We will first analyze the Stereotypes/Demographics-Based Filtering and Item-Based Filtering:

1. Unused Words
2. Frequently mistaken words
3. Words that are confusing together

For the User-Based Filtering and Item-Based Filtering, we aim to analyze the following parameters:

1. Unused Words
2. Frequently mistaken words
3. Words that are easily forgotten

## Methodology Implemented:

### Parameters Established:

#### A. Unused Words:

For unused words an empty of array containing count frequency of each of the words can be applied.

#### B. Frequently Mistaken Words:

A count frequency of number of times a word is mistaken can be computed for each recommendation dispensed.

#### C. Algorithm Specific:

##### i. Words that are confusing together:

A matrix of `number_of_words x number_of_words` can be initialized and updated for every selection of 20 words presented. This would allow accurate comparison of words frequently confused between one-another.

##### ii. Words that are easily forgotten:

For easily forgotten words an empty array containing the count frequency of the number of times the words has been incorrect.

## Recommendation Computation:

<!-- <img src="https://render.githubusercontent.com/render/math?math=%5Ccolor%7Bred%7D%0A%5Cbegin%7Balign*%7D%0Aunused%5C_word%5C_metrics%26%5Cleftarrow%20%5Bu_0%2C%20u_1%2C%20u_2%2C%20...%20u_n%5D%5C%5C%0Afrequently%5C_mistaken%5C_words%26%5Cleftarrow%20%5Bm_0%2C%20m_1%2C%20m_2%2C%20...%20m_n%5D%5C%5C%0Aword%5C_confusion%5C_matrix%26%5Cleftarrow%20%5Cbegin%7Bbmatrix%7D%5Bc_00%2C%20c_01%2C%20c_02%2C%20...%20c_%7B0n%7D%5D%5C%5C%5B%5Chspace%7B45px%7D.%5Chspace%7B45px%7D%5D%5C%5C%5B%5Chspace%7B45px%7D.%5Chspace%7B45px%7D%5D%5C%5C%5B%5Chspace%7B45px%7D.%5Chspace%7B45px%7D%5D%5C%5C%5Bc_%7Bn0%7D%2C%20c_%7Bn1%7D%2C%20c_%7Bn2%7D%2C%20...%20c_%7Bnn%7D%5D%5Cend%7Bbmatrix%7D%5C%5C%0Abase%5C_order%26%3Dsort(%5Calpha%20*%20unused%5C_word%5C_metrics%20%2B%20(1-%5Calpha)*frequently%5C_mistaken%5C_words)%5C%5C%0Abase%5C_words%26%3Dbase%5C_order%5B%3AN%5D%5C%5C%0Aother%5C_words%5C_order%26%3Dsort(%5Csum_%7Bword%3D0%7D%5E%7BN%7D%20c_%7Bword%2C%20i%7D)%5C%5C%0Aother%5C_words%26%3Dother%5C_words%5C_order%5B%3AN%5D%5C%5C%0Arecommended%5C_words%26%3Dshuffle(cat(base%5C_words%2C%20other%5C_words))%0A%5Cend%7Balign*%7D"> -->

![Formula](./assets/images/formula.jpg)

The input parameters `N` and `??` determine the randomity and repetition of words, as well as the choice of `N` determines the size of confusion clusters which may be developed. As the matrices, are time dependent variables, a momentum based computation may be used to update the incorrectly selected words. While the confusion matrix and the unused words array will both remain intact, as they do not expect periodic alterations.

## Deployment:

Streamlit

## Tech-Stack:

1. Python
2. Streamlit
3. Twitter-Link-Sharing

## Impact:

The project aims to develop a single unit recommendation system to help practice for GRE Vocabulary! It provides a testing platform for practicing and polishing your vocabulary skills.
