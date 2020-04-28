import random

def LeftSequence():
    #generating a random number
    num_list = ['1','2','3','4','5','6','7','8']
    left_list = []
    train_len = 20
    
    for i in range(train_len):
        x1 = random.choice(num_list)
        left_list.append(x1)
    return left_list

def RightSequence():
    #generating a random number
    num_list = ['1','2','3','4','5','6','7','8']
    right_list = []
    train_len = 20
    
    for j in range(train_len):
        x2 = random.choice(num_list)
        right_list.append(x2)
    return right_list

def OddSequence():
    #generating a random odd number
    odd_list = []
    num_list = ['1','3','5','7']
    train_len = 12
    
    for i in range(train_len):
        x3 = random.choice(num_list)
        odd_list.append(x3)
    return odd_list

def EvenSequence():
    #generating a random even number
    even_list = []
    num_list = ['2','4','6','8']
    train_len = 12
    
    for i in range(train_len):
        x4 = random.choice(num_list)
        even_list.append(x4)
    return even_list



LeftSequence()
RightSequence()
OddSequence()
EvenSequence()
