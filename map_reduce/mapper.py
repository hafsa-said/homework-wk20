#!/usr/bin/env python
import sys
import re

for line in sys.stdin:
    line= line.strip() #strip white space
    words= line.split() #split lines

    for word in words:
        #find punctuation
        word = re.findall(r"[\w]+|[^\s\w]", word)
        for word in word:
            if word == '':
                pass
            else:
                print(word.lower() + "\t" + '1')
        
