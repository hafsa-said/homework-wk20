#!/usr/bin/env python
import sys

current_word = None
current_count = 0
word = None
#take all the words from the mapper and count them

#lines passed from the mapper.py program
for line in sys.stdin:
    line = line.strip()

    word, count = line.split("\t",1) #splits the words and gives them a count of 1

    count = int(count)
    if current_word == word:
        current_count += count

    else:
        #if there is a current word and its not None
        if current_word:
            print(str(current_count) + "\t" + current_word)
        
        current_count = count
        current_word = word
        
        
if current_word == word:
    print(str(current_count) + "\t" + current_word)