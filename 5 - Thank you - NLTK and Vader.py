#Thank you for reading this!

#Some tips you might want to note down:

		#Always check if the programs you are using are free and open access - especially if you want to have financial gain from your projects!

		#Always remember to save the file as .py - it's a very common mistake, but unless you do this, Python won't work!

		#Don't limit yourself! There are many other things you can do.

#TextBlob works with the library NLKT. You can download it as well
#dFrom the CMD, write: pip install nlkt (and later also) python -m nltk.downloader popular
#this downloads first nltk and later the most popular resources - for example, vader lexicon, another sentiment analyzer for short sentences

import nltk
nltk.download('popular')
from nltk.sentiment import SentimentIntensityAnalyzer

# vader_lexicon and its sentiment analyzer should be automatically downloaded with nltk popular resources - otherwise, you'll have to download it on its own

analyzer = SentimentIntensityAnalyzer()
text = "This is a very interesting text and I want to work more on it"
sentiment = analyzer.polarity_scores(text)
print(sentiment)

#vader expresses the sentiment with a compound score calculated considering the positive, negative and neutral scores
#to know more and cite them properly, see here: https://www.nltk.org/howto.html and https://github.com/cjhutto/vaderSentiment?tab=readme-ov-file#introduction