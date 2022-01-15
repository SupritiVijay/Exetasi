# Exetasi

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

<img src="https://render.githubusercontent.com/render/math?math=%5Ccolor%7Bred%7D%0A%5Cbegin%7Balign*%7D%0Ax%26%3D1%5C%5C%0Ax%2By%26%3D2%5C%5C%0AP%26%3D%5Cbegin%7Bbmatrix%7Dp_1%5C%5Cp_2%5Cend%7Bbmatrix%7D%0A%5Cend%7Balign*%7D">
