import spacy 
nlp = spacy.load("en_core_web_sm")

doc = nlp("NASA awarded Elon Musk’s SpaceX a $2.9 billion contract to build the lunar lander.")
for token in doc:
    print(token.text, token.ent_iob_, token.ent_type_)
