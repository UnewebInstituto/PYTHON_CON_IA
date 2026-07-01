Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
from textblob import TextBlob
wiki = TextBlob("Python is a high-level, general-purpose programming language.")
type(wiki)
<class 'textblob.blob.TextBlob'>
wiki.tags
[('Python', 'NNP'), ('is', 'VBZ'), ('a', 'DT'), ('high-level', 'JJ'), ('general-purpose', 'JJ'), ('programming', 'NN'), ('language', 'NN')]
wiki.noun_phrases
WordList(['python'])
testimonial = TextBlob("Textblob is amazingly simple to use. What great fun!")
testimonial.sentiment
Sentiment(polarity=0.39166666666666666, subjectivity=0.4357142857142857)
testimonial.sentiment.polarity
0.39166666666666666
zen = TextBlob(
    "Beautiful is better than ugly. "
    "Explicit is better than implicit. "
    "Simple is better than complex."
)
zen
TextBlob("Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex.")
zen.words
WordList(['Beautiful', 'is', 'better', 'than', 'ugly', 'Explicit', 'is', 'better', 'than', 'implicit', 'Simple', 'is', 'better', 'than', 'complex'])
zen.sentences
[Sentence("Beautiful is better than ugly."), Sentence("Explicit is better than implicit."), Sentence("Simple is better than complex.")]
for sentence in zen.sentences:
    print(sentence.sentiment)

    
Sentiment(polarity=0.2166666666666667, subjectivity=0.8333333333333334)
Sentiment(polarity=0.5, subjectivity=0.5)
Sentiment(polarity=0.06666666666666667, subjectivity=0.41904761904761906)
sentence = TextBlob("Use 4 spaces per indentation level.")
sentence.words
WordList(['Use', '4', 'spaces', 'per', 'indentation', 'level'])
sentence.words[2].singularize()
'space'
sentence.words[-1].pluralize()
'levels'
from textblob import Word
w = Word("octopi")
w.lemmatize()
'octopus'
w = Word("went")
w.lemmatize("v")  # Pass in WordNet part of speech (verb)
'go'
from textblob import Word
from textblob.wordnet import VERB
word = Word("octopus")
word.synsets
[Synset('octopus.n.01'), Synset('octopus.n.02')]
Word("hack").get_synsets(pos=VERB)
[Synset('chop.v.05'), Synset('hack.v.02'), Synset('hack.v.03'), Synset('hack.v.04'), Synset('hack.v.05'), Synset('hack.v.06'), Synset('hack.v.07'), Synset('hack.v.08')]
Word("octopus").definitions
['tentacles of octopus prepared as food', 'bottom-living cephalopod having a soft oval body with eight long tentacles']
from textblob.wordnet import Synset
octopus = Synset("octopus.n.02")
shrimp = Synset("shrimp.n.03")
octopus.path_similarity(shrimp)
0.1111111111111111
animals = TextBlob("cat dog octopus")
animals.words
WordList(['cat', 'dog', 'octopus'])
animals.words.pluralize()
WordList(['cats', 'dogs', 'octopodes'])
b = TextBlob("I havv goood speling!")
print(b.correct())
I have good spelling!
from textblob import Word
w = Word("falibility")
w.spellcheck()
[('fallibility', 1.0)]
monty = TextBlob("We are no longer the Knights who say Ni. "
                    "We are now the Knights who say Ekki ekki ekki PTANG.")
monty.word_counts['ekki']
3
monty.words.count('ekki')
3
monty.words.count('ekki', case_sensitive=True)
2
wiki.noun_phrases.count('python')
1
b = TextBlob("And now for something completely different.")
print(b.parse())
And/CC/O/O now/RB/B-ADVP/O for/IN/B-PP/B-PNP something/NN/B-NP/I-PNP completely/RB/B-ADJP/O different/JJ/I-ADJP/O ././O/O
zen[0:19]
TextBlob("Beautiful is better")
zen.upper()
TextBlob("BEAUTIFUL IS BETTER THAN UGLY. EXPLICIT IS BETTER THAN IMPLICIT. SIMPLE IS BETTER THAN COMPLEX.")
zen.find("Simple")
65
apple_blob = TextBlob("apples")
banana_blob = TextBlob("bananas")
apple_blob < banana_blob
True
apple_blob == "apples"
True
apple_blob + " and " + banana_blob
TextBlob("apples and bananas")
"{0} and {1}".format(apple_blob, banana_blob)
'apples and bananas'
blob = TextBlob("Now is better than never.")
blob.ngrams(n=3)
[WordList(['Now', 'is', 'better']), WordList(['is', 'better', 'than']), WordList(['better', 'than', 'never'])]
for s in zen.sentences:
    print(s)
    print("---- Starts at index {}, Ends at index {}".format(s.start, s.end))

    
Beautiful is better than ugly.
---- Starts at index 0, Ends at index 30
Explicit is better than implicit.
---- Starts at index 31, Ends at index 64
Simple is better than complex.
---- Starts at index 65, Ends at index 95
