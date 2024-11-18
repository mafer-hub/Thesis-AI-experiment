#now that we know how to analyse the sentiment of our text, perhaps you want to see the sentiment of other sentences - maybe even in another language!
#unfortunately,textblob was created using the english language. Even when supporting other languages, these tools might be less precise
#luckily, there are some solutions!

					#SOLUTION 1: use a translator

#DeepL is an extremely good translator; otherwise there are of course many other options, from Google Translate to ChatGPT

from textblob import TextBlob

text = "This originally was a text in another language that was translated in English. The words used are super positive and convey feelings of joy"

blob = TextBlob(text)

sentiment = blob.sentiment

print("sentiment:", sentiment)

					#SOLUTION 2: use another library

#another possibility is downloading another library which was trained with the language you want to use. you can find more information on the internet
#for example, as an Italian native speaker, I can use Hugging Face Transformers
#we can use python to install it - search for cmd, and there write: pip install transformers
#however, you might need to install other things (for example Rust) for it to run properly
