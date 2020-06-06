
from nltk.corpus import wordnet
from nltk import word_tokenize, pos_tag

# Generate english synonyms
synonyms = []
antonyms = []

#synset = wordnet.synset("on")
#print("original synset: ", synset)

#for syn in wordnet.synsets("buy", "v"): #filter by type
for syn in wordnet.synsets("buy"):
    print("Syns: ", syn)
    for l in syn.lemmas():

        print("Lemma: ", l)
        print("Words: ", l.name())

        synonyms.append(l.name())
        if l.antonyms():
                antonyms.append(l.antonyms()[0].name())

print("> English")
print("Synonyms: ", set(synonyms))
print("Antonyms: ", set(antonyms))


# Generate spanish synonyms
synonyms = []
antonyms = []

for syn in wordnet.synsets("comprar", lang="spa"):
    for l in syn.lemmas("spa"):
        synonyms.append(l.name())
        if l.antonyms():
            print("antonim ", l.antonyms()[0])
            antonyms.append(l.antonyms()[0].name())

print("> Spanish")
print("Synonyms: ", set(synonyms))
print("Antonyms: ", set(antonyms))

# tagg the types in a phrase
text = word_tokenize("And now for something completely different")
print(pos_tag(text)[0][1][0].lower())