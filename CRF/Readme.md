# Conditional Random Field

A Conditional Random Field is a type of probabilistic graphical model often used in Natural Language Processing for **Sequence Labeling** task like `POS Tagging` or `Named Entity Recognition (NER)`.

It is a variant of a **Markov Random Field (MRF)**.

CRFs are used for sequence labeling task where the goal is to predict a structured output based on a set of input features. They are trained using **Maximum Likelihood Estimation** which involves optimizing the parameters of the model to maximize the probability of the correct output sequence given the input features. This optimization problem is typically solved using iterative algorithms like gradient descent or `L-BFGS`.

- [Basic CRF with Sklearn CRF_Suite](./CRF_basic.ipynb)