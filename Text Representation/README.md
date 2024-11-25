# Text Representation
Feature extraction is an important step for any machine learning problem. No matter how good a modeling algorithm we use if we feed in poor features we will get poor results.

This is often called as `**garbage in garbage out**`.

# Vector Space Models
Text representation in terms of vector of numbers.

The most common way to calculate similarity between two text represented in **VSM** is by using `cosine similarity` or `distance`.


$$\text{cosine similarity} = \frac{\sum_{i=1}^n A_i B_i}{\sqrt{\sum_{i=1}^n A_i^2} \cdot \sqrt{\sum_{i=1}^n B_i^2}}$$

---

$$\text{Euclidean Distance} = \sqrt{\sum_{i=1}^n (A_i - B_i)^2}$$


# Vectorization approaches
Different vectorization approaches in categories.

### Distributional representations
Distributional representations use high dimensional vectors to represent words.

#### One Hot Encoding
```
text = ["I love NLP"]
I =    [1 0 0]
Love = [0 1 0]
NLP =  [0 0 1]
```
#### Bag of Words
- create vocabulary
- from each document how many times each particular word repeats.

```
text1 = "I Love programming."
text2 = "I Love coding and programming."

vocabulary = ["I","Love", "programming", "and", "coding"]

text1_vectorized = [1 1 1 0 0 ]
"I"=1 "Love"=1 "programming"=1 "coding"=0 "and"=0

text2_vectorized = [1 1 1 1 1]
"I"=1 "Love"=1 "programming"=1 "coding"=1 "and"=1
```
#### N grams
It is a contiguous collection of n words and can help capture some context.

- 2 word contiguous : Bi-gram
- 3 word contiguous : Tri-gram
- n word contiguous : n-gram

```
text_a= "dog loves to eat meat"
text_b = "cat loves to eat milk"
bi-gram = ["dog loves", "loves to", "to eat", "eat meat", "cat loves", "eat milk"] // 6 dim vector
text_a_vectorized = [1 1 1 1 0 0]
text_b_vectorized = [0 1 1 0 1 1]
```
#### TfIDF

**TF-IDF** is a statistical measure used in text mining and natural language processing (NLP) to evaluate the importance of a word in a document relative to a collection of documents (corpus). It combines two metrics:

1. **TF (Term Frequency)**: Measures how frequently a term appears in a document.
2. **IDF (Inverse Document Frequency)**: Measures how unique or rare a term is across all documents.

The TF-IDF of a term \( t \) in a document \( d \) is calculated as:

$$\text{TF-IDF}(t, d) = \text{TF}(t, d) \cdot \text{IDF}(t)$$

Where:

**Term Frequency (TF):**

$$\text{TF}(t, d) = \frac{\text{Count of } t \text{ in } d}{\text{Total terms in } d}$$

**Inverse Document Frequency (IDF):**

$$\text{IDF}(t) = \log \left( \frac{\text{Total number of documents}}{\text{Number of documents containing } t} \right)$$

---

### Distributed representations
The vectors in distributional representation are very high dimensional and sparse which makes computationally inefficient and hampers learning.

To overcome the limitations of basic vector methods, methods to learn low dimensional representations were devised.

These methods use neural networks to create `**dense**`, `**low - dimensional representations**` of words and text.

#### Word Embeddings
 - C-BOW
 - Skip gram

 ---
 
### Universal Text Representation
The idea for universal text representation is for the **contextual word representation**. In the modern NLP, model uses **Attention Mechanisms** to achieve contextual word representation.