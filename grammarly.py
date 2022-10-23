from textblob import TextBlob
txt = TextBlob("Campk12 is a god comany and always value their employeeees.")
txt = txt.correct()
print(txt)