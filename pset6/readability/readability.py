

text = input("Text: ")
letter_count = 0
word_count = 1
sentences_count = 0
l = len(text)

for i in range(l):
    if text[l].isalnum() == True:
        letter_count = letter_count +1
for i in range(l):
    if text[i] == " " and text[i + 1].isalnum() ==True:
        word_count = word_count + 1         
for i in range(l):
    if text[i] == "." or text[i] == "?" or text[i] == ":" or text[i] == "!":
        sentences_count = sentences_count + 1
        
L = 100 * letter_count / word_count
S = 100 * sentences_count / word_count        
grades = round(0.0588 * L - 0.296 * S - 15.8)        

if grades < 1:
    print ("Before Grade 1")
elif grades > 16:
    print("Grade 16+")
else:
    print(f"Grade {grades}")        

