#let's move on to our last point: what if the text you want to study is very long?
#As you might already have noticed, the python language uses certain symblos like ' and ", and other common ones like ()
#If these are also found in the text, this might cause an error! The system recognizes them but does not undertsand how they're use in the sentence

#to solve this, you can put a backslash \ before them, so when special characters appear Python knows to ignore them
#of course, this would result in a terribly long (and extremely dull) task - putting backslashes all over the text!
#you can use AI to help you. Fo example, you can ask ChatGPT:
#Can you use backslashes to create escape sequences where special characters appear, so that I can use NLP techniques with Python? This is the text: ...

#Let's try it together - my text can be: This is a text made up of several "direct quotes", 'strange words' and (details). Still, it's very interesting! I want to know more about its sentiment, but "unfortunately, there are too many special symbols" (which I 'cannot' leave)
#let's ask ChatGPT to help us create these "escape sequences" and use the new, corrected text

from textblob import TextBlob 

text = "This is a text made up of several \"direct quotes\", \'strange words\' and (details). Still, it\'s very interesting! I want to know more about its sentiment, but \"unfortunately, there are too many special symbols\" (which I \'cannot\' leave)"

blob = TextBlob(text)

sentiment = blob.sentiment

print("sentiment:", sentiment)

#now run it! Problem solved :)