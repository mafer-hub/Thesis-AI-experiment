#now you need to install textblob
#this operation isn't your usual installation: you have to open the cmd of your computer and install it from there. Python can help us here!
#you can search for "cmd", open it, and write: pip install textblob
#pip is Python's management system
#now you can use textblob! remember to write at the beginning:

from textblob import TextBlob

#now, let's move on to the text. You need to write your text like this so the program recognizes it:

text = "Inside here is your text, for example: this is the best text ever!"

# now create an object with the text, so that textblob can analyse it. they're usually called blobs, so:

blob = TextBlob(text)

# to analyse the sentiment, let's ask it to see the sentiment of the blob (aka our text)

sentiment = blob.sentiment

print("sentiment:", sentiment)

#now run it (ctrl + b): you should see the polarity and the subjectivity below!




#in short, you should have:

from textblob import TextBlob

text = "your text is here"

blob = TextBlob(text)

sentiment = blob.sentiment

print("sentiment:", sentiment)

#to know more about textblob, see here: https://textblob.readthedocs.io/en/dev/