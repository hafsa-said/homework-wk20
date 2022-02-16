# homework-wk20

The mapper.py and reducer.py file with the code is attached in repo

*How to run the program*
- We use git bash or Visual Studio Code to run the program
- Since we are using a file not a string, we used 'cat' to concatenate
- Next we run the file we want
- Then we insert a pipe, which allows in to pipe in first our mapper.py program and then the reducer.py program
- We can use sort in the middle with a pipe as well
- Finally we resort everything by count
- The -g at the end allows us to sort anything that "looks like a number" as a number

*Running the program*
- First we saved the mapper.py program in VSC
- Ran the file through git bash using following code:
 "cat ../cats_txt.txt|./mapper.py|sort"
 -The following results were seen
 
 
 ![Mapper program](https://github.com/hafsa-said/homework-wk20/blob/main/mapperss.jpg)
 
 - Ran program through both mapper and reducer using:
   "cat ../cats_txt.txt|./mapper.py|sort|./reducer.py|sort -g "
 - The following results were seen


 ![Mapper and Reducer program](https://github.com/hafsa-said/homework-wk20/blob/main/reducerss.jpg)
 ![Mapper and Reducer program](https://github.com/hafsa-said/homework-wk20/blob/main/reducer2ndss.jpg)
 
 **Briefly discuss why this kind of exercise might be helpful for NLP**
 
 When we have a large number of text, or mixed type of data, it can be essential to strip words of punctuation and capitalization. This allows us to more easily count word frequencies and/or later compute higher level analyses.
