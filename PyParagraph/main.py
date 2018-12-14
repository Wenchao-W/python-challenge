# Modules
import os
import re
# Open file
txtpath = os.path.join('raw_data','paragraph_3.txt')
with open(txtpath, "r") as txtfile:
    # Count the goals
    paragraph=txtfile.read()
    word=re.split(" ", paragraph)
    wordcount=len(word)
    Avg_Lettercount=sum([len(i) for i in word])/wordcount
    sentence=re.split("(?<=[.!?]) +", paragraph)
    sentencecount=len(sentence)
    Avg_sentencelength=sum([len(j.split(" ")) for j in sentence])/sentencecount
# Print out
print('Paragraph Analysis')
print('-----------------')
print(f'Approximate Word Count: {wordcount}')
print(f'Approximate Sentence Count: {sentencecount}')
print(f'Average Letter Count: {"{:.2}".format(Avg_Lettercount)}')
print(f'Average Sentence Length: {Avg_sentencelength}')