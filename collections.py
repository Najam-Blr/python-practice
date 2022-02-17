from collections import defaultdict 

#Program to count number of words in a sentence 
sentence = "The red fox jumped over the fence and ran to the zoo for food"
words = sentence.split()

word_dict = {}
for word in words:
    if word in word_dict:
        word_dict[word]= word_dict[word]+1 
    else:
        word_dict[word] = 1
    
print(word_dict)

for w,c in word_dict.items():
    print(f"Word Count: {w} => {c}")

'''
{'The': 1, 'red': 1, 'fox': 1, 'jumped': 1, 'over': 1, 'the': 2, 'fence': 1, 'and': 1, 'ran': 1, 'to': 1, 'zoo': 1, 'for': 1, 'food': 1}
Word Count: The => 1
Word Count: red => 1
Word Count: fox => 1
Word Count: jumped => 1
Word Count: over => 1
Word Count: the => 2
Word Count: fence => 1
Word Count: and => 1
Word Count: ran => 1
Word Count: to => 1
Word Count: zoo => 1
Word Count: for => 1
Word Count: food => 1
'''

#Same problem with default_dict
'''
The defaultdict will automatically assign zero as the value to any key it doesn’t already have in it. 
We add one so it makes more sense and it will also increment if the word appears multiple times in the sentence.
'''
sentence = "The red fox jumped over the fence and ran to the zoo for food"
words = sentence.split()
word_dict = default_dict(int)
for word in words:
  word_dict[word]+= 1 
  
print(word_dict)

'''
defaultdict(<class 'int'>,
            {'The': 1,
             'and': 1,
             'fence': 1,
             'food': 1,
             'for': 2,
             'jumped': 1,
             'over': 1,
             'ran': 1,
             'red': 1,
             'the': 2,
             'to': 1,
             'zoo': 1})
'''


