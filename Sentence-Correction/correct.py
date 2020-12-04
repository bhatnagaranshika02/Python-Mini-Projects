from textblob import TextBlob

a=input()
text = TextBlob(a)

print(text.correct())
