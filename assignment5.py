import requests
from bs4 import BeautifulSoup
from collections import Counter
import spacy


# getResponce = requests.get('https://www.gutenberg.org/files/135/135-0.txt')
#Parse the response of type html 
# soup = BeautifulSoup(getResponce.content, 'html.parser')
# print(soup)

# with open('./Assignment5/events.txt','w') as fd:
    # fd.write(soup.text)
    
file = open('./Assignment5/events.txt', "r+")     
      
# Load English tokenizer, tagger, parser and NER
nlp = spacy.load("en_core_web_lg")
nlp.max_length = 3324221
doc = nlp(file.read())

# Analyze syntax

# 1. How many tokens are in the document?
token_count = 0
for token in doc:
    token_count += 1
print("Number of token in document : " + str(token_count))
# Number of token in document : 747613

# 2. How many verbs are in the document?
verb_count = 0    
for verb in doc:
    if verb.pos_ == "VERB":
        verb_count += 1
print("Number of verbs phrases in document :" + str(verb_count))
# Number of verbs phrases in document :72451

# 3. What is the most frequent named entity?
#remove stopwords and punctuations
words = [token.text for token in doc if token.is_stop != True and token.is_punct != True]
word_freq = Counter(words)
common_words = word_freq.most_common(5)
print(common_words)
# [('\n\n', 39468), ('\n\n\n\n', 8696), ('\n\n\n\n\n\n', 4429), ('man', 1944), ('said', 1792)]
# Word 'man' has repeated 1944 times

# 4. How many sentences are in the document?
print("Number of sectences in document :" + str(len(list(doc.sents))))
# Number of sectences in document :35872

# 5. Of all the sentences in the text that are at least 10 words in length, which two are most similar (but not identical)?
max_similarity = 0.0
most_similar = None, None
for i, sent in enumerate(doc.sents):
    for j, other in enumerate(doc.sents):
        if j <= i:
            continue
        if len(sent) > 10 and len(other) > 10:
            similarity = sent.similarity(other)
            if similarity > max_similarity:
                max_similarity = similarity
                most_similar = sent, other
print("Most similar sentences are:")
print(f"-> '{most_similar[0]}'")
print("and")
print(f"-> '{most_similar[1]}'")
print(f"with a similarity of {max_similarity}")

# -> 'Je n’ai qu’un Dieu, qu’un roi, qu’un liard, et qu’une botte.
# and
# -> 'Je n’ai qu’un Dieu, qu’un roi, qu’un liard, et qu’une botte.'
# with a similarity of 1.0000001192092896

# 6. What is the vector representation of the first word in the 15th sentence in the document?
sent_count = 0  
for sent in doc.sents:
    sent_count += 1
    if sent_count == 15:        
        print("15th sectences in the document :" + str(sent))
        for word in sent:
            print("First word of the sentence: " + str(word.text)," Is it vector representated? " + str(word.has_vector)," Vector representation norm: " + str(word.vector_norm))
            break
# 15th sectences in the document :I—ONE MOTHER MEETS
# First word of the sentence: I  
# Is it vector representated? True  
# Vector representation norm: 112.27491    

