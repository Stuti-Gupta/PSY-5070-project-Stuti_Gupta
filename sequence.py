import random

def LeftSequence():         #generating a random number
    
    num_list = ['1','2','3','4','5','6','7','8']
    left_list = []  #array to be used as left stimulus train
    train_len = 20  #20 = 5sec/0.25msec
    
    for i in range(train_len):  #at every iteration, a random number is selected from the number list and appended to the train
        x1 = random.choice(num_list)
        left_list.append(x1)
    return left_list

def RightSequence():        #generating a random number
    
    num_list = ['1','2','3','4','5','6','7','8']
    right_list = [] #array to be used as right stimulus train
    train_len = 20  #20 = 5sec/0.25msec
    
    for j in range(train_len):  #at every iteration, a random number is selected from the number list and appended to the train
        x2 = random.choice(num_list)
        right_list.append(x2)
    return right_list

def OddSequence():          #generating a random odd number
    
    num_list = ['1','3','5','7']
    odd_list = []   #array to be used as odd stimulus train
    train_len = 8   #8 = 2sec/0.25msec
    
    for i in range(train_len):  #at every iteration, a random number is selected from the number list and appended to the train
        x3 = random.choice(num_list)
        odd_list.append(x3)
    return odd_list

def EvenSequence():         #generating a random even number
    
    num_list = ['2','4','6','8']
    even_list = []  #array to be used as even stimulus train
    train_len = 8   #8 = 2sec/0.25msec
    
    for i in range(train_len):  #at every iteration, a random number is selected from the number list and appended to the train
        x4 = random.choice(num_list)
        even_list.append(x4)
    return even_list

#-----------------------------------------------------Calling each of the functions-----------------------------------------------------

LeftSequence()
RightSequence()
OddSequence()
EvenSequence()
