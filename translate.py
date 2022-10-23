from textblob import TextBlob
word = TextBlob("Comment vas-tu?")
print(word.detect_language())
print(word.translate(to='es'))
print(word.translate(to='en'))
print(word.translate(to='zh'))