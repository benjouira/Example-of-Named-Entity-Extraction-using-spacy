# Named Entity Recognition
# In the example below we have used “token.text, token.entiob, token.enttype” to printed tokens, token’s entity annotations, and the entity types of the token.

import spacy 
nlp = spacy.load("en_core_web_sm")

doc = nlp("NASA awarded Elon Musk’s SpaceX a $2.9 billion contract to build the lunar lander.")
for token in doc:
    print(token.text, token.ent_iob_, token.ent_type_)
