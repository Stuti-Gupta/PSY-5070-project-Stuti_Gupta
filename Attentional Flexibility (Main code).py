from psychopy import visual, event, core, misc
from psychopy.hardware import keyboard

import numpy

import random

import sequence

window = None           #defining the screen on which stimulus will occur
base_circle = None      #defining a circle
center = None           #defining the point of initial focus
ast = None              #defining the new focus point as asterisk
a_pos = None            #defining position of asterisk
left_vis = None         #defining the left visual train
right_vis = None        #defining the right visual train
letter = None           #defining the letter stimulus
char_l = None           #chosen letter at random from l_list
choice_prompt = None    #ongoing instruction for keyboard input
kb = None               #defining the keyboard variable
task_start_time = None  #variable to find the start of a task
numtype = []            #empty array for odd and even trains
log_file = None         #creating an empty csv file
numtype_idx = None      #index of the numtype array, which has the array of odd and even lists

#-------------------------------------------trains imported from sequence.py-----------------------------------------------------

left_char = sequence.LeftSequence()     #left train of numbers
right_char = sequence.RightSequence()   #right train of numbers
odd_char = sequence.OddSequence()       #odd train of numbers
even_char = sequence.EvenSequence()     #even train of numbers


#----------------------------defining all stimuli of the trial sequence and selecting 'a_pos'------------------------------------

def StimulusSequence():
    global ast
    global a_pos
    global left_vis
    global right_vis
    global letter
    global char_l
    global numtype
    global odd_char
    global even_char
    
    #----------------defining position of asterisk-------------------------
    
    x = [-1.5, 1.5]             #positions of asterisk
    a_pos = random.choice(x)    #choosing a position at random
    #-----------------creating asterisk stimulus---------------------------
    ast = visual.TextStim(window, color = 'black', pos = (a_pos,-0.15))
    ast.text = '*'
    
    #----------stimulus for train of numbers on left and right-------------
    
    left_vis = visual.TextStim(window, color = 'black', pos = (-1.5,0))
    right_vis = visual.TextStim(window, color = 'black', pos = (1.5,0))
    
    #-------------defining letter stimulus and choice----------------------
    
    l_list = ['A','K']              #letter choices
    char_l = random.choice(l_list)  #letter chosen at random from the list
    #----------------creating the letter stimulus--------------------------
    letter = visual.TextStim(window, color = 'black', pos = (a_pos,0))
    letter.text = char_l
    
    #---------------even and odd trains of numbers-------------------------
    
    numtype = [odd_char, even_char]


#-----------------------------defining the test phase of the task, presenting odd/even stimuli-----------------------------------

def OddEven():
    global base_circle
    global center
    global choice_prompt
    global left_vis
    global right_vis
    global letter
    global char_l
    global numtype
    global odd_char
    global even_char
    global numtype_idx
    
    #-----------------------------choosing either odd or even train--------------------------------
    
    n = [0,1]
    numtype_idx = random.choice(n)
    
    #---------------------------displaying the odd or even trains----------------------------------
    
    if char_l == 'A':                   #if 'A', maintain attention to same side, so test train on same side
        num = numtype[numtype_idx]      #assigning the odd/even train to a new list
        i = -1
        j = -1
        if a_pos == -1.5:               #if A in left position, even or odd train on left, normal train on right
            while i < len(num)-1 and j < len(right_char)-1:     #loops till the last element of the num array
                i = i+1
                j = j+1
                base_circle.draw()
                center.draw()
                choice_prompt.draw()
                left_vis.setText(num[i])
                left_vis.draw()
                right_vis.setText(right_char[j])
                right_vis.draw()
                window.flip()
                core.wait(0.25)
        elif a_pos == 1.5:              #if A in right position, even or odd train on right, normal train on left
            while i < len(num)-1 and j < len(left_char)-1:      #loops till the last element of the num array
                i = i+1
                j = j+1
                base_circle.draw()
                center.draw()
                choice_prompt.draw()
                right_vis.setText(num[i])
                right_vis.draw()
                left_vis.setText(left_char[j])
                left_vis.draw()
                window.flip()
                core.wait(0.25)
    if char_l == 'K':                   #if 'K', shift attention to other side, so test train on other side
        num = numtype[numtype_idx]      #assigning the odd/even train to a new list
        i = -1
        j = -1
        if a_pos == -1.5:               #if K in left position, even or odd train on right, normal train on left
            while i < len(num)-1 and j < len(left_char)-1:      #loops till the last element of the num array
                i = i+1
                j = j+1
                base_circle.draw()
                center.draw()
                choice_prompt.draw()
                right_vis.setText(num[i])
                right_vis.draw()
                left_vis.setText(left_char[j])
                left_vis.draw()
                window.flip()
                core.wait(0.25)
        elif a_pos == 1.5:              #if K in right position, even or odd train on left, normal train on right
            while i < len(num)-1 and j < len(right_char)-1:     #loops till the last element of the num array
                i = i+1
                j = j+1
                base_circle.draw()
                center.draw()
                choice_prompt.draw()
                left_vis.setText(num[i])
                left_vis.draw()
                right_vis.setText(right_char[j])
                right_vis.draw()
                window.flip()
                core.wait(0.25)


#-------------------------------initialising the remaining stimuli and calling Sequence()----------------------------------------

def Initialize():
    global window
    global kb
    global task_start_time
    global center
    global base_circle
    global choice_prompt
    global log_file
    
    #------------------------setting this variable to the core time-----------------------------
    
    task_start_time = core.getTime()
    
    #----------------------------defining the window stimulus-----------------------------------
    
    window = visual.Window([1280, 720], monitor = "testMonitor", units = "deg",
        screen=1, color = 'white')
    
    #--------------------------making the circle and center point-------------------------------
    
    base_circle = visual.Circle(window, radius = 3, lineColor = 'black')
    center = visual.Circle(window, radius = 0.1, fillColor = 'black')
    
    #----------------------------calling the earlier definition---------------------------------
    
    StimulusSequence()
    
    #--------------------------------ongoing instructions---------------------------------------
    
    choice_prompt = visual.TextStim(window, wrapWidth = 30, color = 'black', pos = (0,6))
    choice_prompt.text = 'Press "o" for odd and "e" for even'
    
    #---------------------------------initialise keyboard---------------------------------------
    kb = keyboard.Keyboard()
    
    
    #----------------csv file opened and trails are appended each time--------------------------
    
    log_file = open('D:/Documents/UIowa/Programming for Psychologists/Project/results.csv', 'a')


#---------------------------------------showing the instructions for the experiment----------------------------------------------

def ShowInstructions():
    global window
    
    #creating a visual stimulus to show instructions
    ins = visual.TextStim(window, height = 1, wrapWidth = 35, color = 'black', pos = (0, 0))
    
    ins.text = 'On each trial, you will first see an asterisk appear on the screen, either on the left or right of a circle.\n\
        This will be followed by a series of numbers, on both sides of the circle.\n\
        You will have to focus on the numbers on the side of the asterisk.\n\
        After a few seconds, you will see a letter blink on the side you have been focusing on.\n\n\
        If you see "A", you are to keep looking at the same side.\n\
        If you see "K", you are to look at the other side.\n\
        Your task is to judge what is the nature of number that appears immediately after the letter.\n\
        You have two seconds to press the appropriate key.\n\
        (press "o" for odd and "e" for even on the keyboard)\n\nPress any key to start.'
    
    #the above instructions keep showing till the user presses a key on the keyboard
    while not event.getKeys():
        ins.draw()
        window.flip()


#-------------------------------this is where the magic happens. sequence of stimuli shown---------------------------------------

def RunTrial(position = (a_pos,0)):
    global window
    global kb
    global task_start_time
    global ast
    global a_pos
    global left_char
    global right_char
    global left_vis
    global right_vis
    global letter
    global char_l
    global choice_prompt
    global center
    global base_circle
    global numtype_idx
    
    #-------------------------------draw the asterisk for 500msec----------------------------------
    
    base_circle.draw()
    center.draw()
    ast.draw()
    choice_prompt.draw()
    window.flip()
    core.wait(0.5)      #this is 0.5s, so that is 500msec. Similarly 0.25s is 250msec later
    
    #------------draw the initial distractor numbers at 250msec each for 5 secs total--------------
    
    i = -1
    j = -1
    while i < len(left_char)-1 and j < len(right_char)-1:   #loops till all elements of both trains are displayed
        i = i+1
        j = j+1
        base_circle.draw()
        center.draw()
        choice_prompt.draw()
        left_vis.setText(left_char[i])
        left_vis.draw()
        right_vis.setText(right_char[j])
        right_vis.draw()
        window.flip()
        core.wait(0.25)
    
    #-------------------------------draw the letter for 250msec------------------------------------
    
    #random number stimulus created for opposite side of the letter
    randnum = visual.TextStim(window, color = 'black', pos = (-a_pos,0))
    randnum.text = '5'  #'5' set as random number
    
    base_circle.draw()
    center.draw()
    letter.draw()
    randnum.draw()      #random number drawn
    choice_prompt.draw()
    letter_onset = core.getTime() - task_start_time     #defining the point at which letter appears in each trial
    window.flip()
    core.wait(0.25)
    
    #-------------------------keyboard reset to get input from user--------------------------------
    
    kb.clock.reset()
    kb.clearEvents()
    
    #-----------------------calling the function to display odd/even train-------------------------
    
    OddEven()
    
    #---------------------documenting response from user, key pressed and rt-----------------------
    
    ptbKeys = kb.getKeys(['e', 'o'])   #limiting input keys from the keyboard to 'e' and 'o'
    
    response_entry = "numbers: "  #the first part of the string will be the specifying odd or even, and second will be rt
    
    #documenting the stimulus presented
    if numtype_idx == 0:            #zero means odd, so odd is documented
        response_entry += "Stim:, odd, "
    elif numtype_idx == 1:          #one means even, so even is documented
        response_entry += "Stim:, even, "
    
    if ptbKeys != []:                       #when a key is pressed
        if ptbKeys[0].name == 'e':          #'e' is pressed on the keyboard, record even
            response_entry += "User:, even, "
        elif ptbKeys[0].name == 'o':        #'o' is pressed on the keyboard, record odd
            response_entry += "User:, odd, "
        else:                               #for wrong key press, record none
            response_entry += "User:, none, "
        response_entry += f"{ptbKeys[0].rt:.4f}"
    else:                                   #for no response, rt has been assigned as zero
        response_entry += "User:, none, 0"
    
    #-------------------------documenting the characteristics of the letter-------------------------
    
    if a_pos == -1.5:   #document left
        side = "left"
    elif a_pos == 1.5:  #document right
        side = "right"
    
    #first part of string is the letter, second is rt, third is side of the circle the letter was presented
    letter_entry = "letter:, " + char_l + ", " + f"{letter_onset:.4f}, " + str(side)
    
    #---------------------------------entering values into csv file--------------------------------
    
    log_file.write(letter_entry + ", " + response_entry + "\n")
    
    #----------------------intertrial interval of 1250ms with a blank screen-----------------------
    
    base_circle.draw()
    center.draw()
    choice_prompt.draw()
    window.flip()
    core.wait(1.25)
    
    #-------------------------------redefining a_pos for next trial--------------------------------
    
    StimulusSequence()


#-----------------------------------------------definition for running the task--------------------------------------------------

def RunTask():
    runs = 4                #number of runs
    iter = 10               #number of trials per run
    for j in range(runs):       #4 loops
        for i in range(iter):   #10 loops each
            StimulusSequence()
            RunTrial((a_pos,0))


#-----------------------------------------------------terminating the task-------------------------------------------------------

def TerminateTask():
    global window
    global log_file
    
    #closing the csv file, closing the window stimulus and quiting the console
    log_file.close()
    window.close()
    core.quit()


#---------------------------------------------calling each function sequentially-------------------------------------------------

Initialize()
ShowInstructions()
RunTask()
TerminateTask()
