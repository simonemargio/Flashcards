# Flashcards game

## Index
1. [What is](#What-is)
2. [Dependencies](#Dependencies)
3. [Run](#Run)


### What is
To improve your skills you can practice with a series of any questions or items you need to answer.  
In this case there are the 100 most used words in English and you have to find the correspondence in Italian. You can adapt the program for whatever you want to repeat or improve.

### Dependencies
Pandas is used to read the CSV files.
```
pip3 install pandas
```
### Run
In main.py:  
- *file_words*: put the path of the file containing the questions/objects to learn.  
- *file_learn*: put the path of the file where you want to save the wrong elements and that you have to repeat better.
- *time* is the time you have (in milliseconds) to respond.
- *text_card & text_card_flip*: title you want to give to the front and back card.
```
python3 main.py
```