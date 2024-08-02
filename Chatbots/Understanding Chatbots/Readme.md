# Chatbots:
A **chatterbot** or **chatbot** is a software application used to conduct an on-line chat conversation via text or text-to-speech, in lieu of providing direct contact with a live human agent.

- The first chatbot was **Eliza** created in 1966
ELIZA's key method of operation involves the recognition of clue words or phrases in the input, and the output of the corresponding pre-prepared or pre-programmed responses that can move the conversation forward in an apparently meaningful way.

What Eliza did was copied by chatbot designers ever since.

# Need of ChatBots
The applications of AI is Infinite and so is for Chatbots
- Messaging Apps
- Customer Service
- Company internal use

# Types of ChatBots
- **Simple Chatbots**: have limited capabilities and are usually called rule based bots. They are task-specific.
- **Smart Chatbots***: AI-enabled smart chatbots are designed to simulate near-human interactions with customers.
- **Hybrid Chatbots**: They are a combination of simple and smart chatbots.
- **Social Messaging Chatbots**
- **Menu based chatbots**: First ai and then after understanding user query pass to the human chat.

## Differences between Rule-Based Chatbots and Self-Learning Chatbots

> `Rule based technique` uses statistical technique (cosine similarities, tfidf, regex) to understand.
> `Self-Learning chatbots` are artificially intelligent.


| Aspect                       | Rule-based Chatbots                                         | Self-Learning Chatbots                                         |
|------------------------------|-------------------------------------------------------------|----------------------------------------------------------------|
| **Response Generation**      | Bot uses sets of questions and answers initially entered by the programmer to respond to requests in later usage. | Bots use machine learning algorithms to learn how to provide suitable answers to unexpected questions. |
| **Interaction Basis**        | Chatbots react to questions or statements that match their database with appropriate answers or actions. | By learning from past interactions, the bot will gradually grow in scope. |
| **Data Integration**         | Depending on the context a chatbot is used in, it can be enhanced by additional access to external data such as customer relationship management (CRM) or enterprise resource planning (ERP) systems. | It can then answer not only questions it was previously trained with but also unexpected questions. |
| **Capability and Effort**    | The more resources are made available, the more capable the system becomes. | This method leads to far more capable and sophisticated chatbots, but also requires much more programming effort. |


# How a ChatBot works:

```
            Entity Resolution -> Entities
UserMessage->                               ->AI-Brain->Response
            Intent Classification->Intent
```

# Another Chatbot: Retrieval Based Chatbot
Steps involved in building Chatbot with NLTK
- Reading Text Corpus
- PreProcessing (stop words removal, lower case conversion, etc)
- Tokenization, Stemming and Lemmatization
- Bag of Words
- One hot encoding