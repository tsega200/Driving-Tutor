import random

global used_question
global count 
used_question = [ ]
count = 0

##Gets answer and adds the questions that have been used to a list

def get_answer():
    answer = input("Please enter an answer: ")
    answer = int(answer)
    
    if answer > 4:
        answer = input("Please enter a valid number: ")
    else:
        return str(answer)
    
def exclude_question(num):
    used_question.append(num)
    
    
    
  #####All the questions####  
def question_one():
    exclude_question(1)
    print("When you pass another vehicle, before you return to the right lane, you must:")
    print("1. Make sure you can see the front bumper of the vehicle you passed. \n2. Look at your interior rear-view mirror. \n3. Signal. \n4. All of the above ")
    answer = get_answer()
    
    if answer == "4":
        print("Correct!")
        num = random.randint(1,10)
        get_question(num)
        
    else:
        print("Incorrect.")
        num = random.randint(1,10)
        get_question(num)
        
def question_two():
    exclude_question(2)
    print("Speed limit signs are:")
    print("1. Destination (guide) signs. \n2. Service Signs. \n3. Warning signs. \n4. Regulatory signs. ")
    answer = get_answer()
    
    if answer == "4":
        print("Correct!")
        num = random.randint(1,10)
        get_question(num)
        
    else:
        print("Incorrect.")
        num = random.randint(1,10)
        get_question(num)
        
def question_three():
    exclude_question(3)
    print("Where should your hands be positioned on the steering wheel?")
    print("1. 10 and 2 o'clock. \n 2. 9 and 3 o'clock. \n3. 8 and 4 o'clock. \n4. Anywhere comfortable.")
    answer = get_answer()
    
    if answer == "1":
        print("Correct!")
        num = random.randint(1,10)
        get_question(num)
        
    else:
        print("Incorrect.")
        num = random.randint(1,10)
        get_question(num)


def question_four():
    exclude_question(4)
    print("Vehicle inspection is required:")
    print("1. Every six months. \n2. Only for vehicles over five years old. \n3. Every two years. \n4. Every year.")
    answer = get_answer()

    if answer == "4":
        print("Correct!")
        num = random.randint(1,10)
        get_question(num)
        
    else:
        print("Incorrect.")
        num = random.randint(1,10)
        get_question(num)


def question_five():
    exclude_question(5)
    print("The minimum drinking age is:")
    print("1. 21 \n2. 9 \n 3. 18 \n4. 20")
    answer = get_answer()

    if answer == "1":
        print("Correct!")
        num = random.randint(1,10)
        get_question(num)
        
    else:
        print("Incorrect.")
        num = random.randint(1,10)
        get_question(num)
    
    
def question_six():
    exclude_question(6)
    
    print("A road is likely to be most slippery when:")
    print("1. it is icy and the temperature is near freezing. \n2. in cold, dry weather. \n3. when tire marks have been left by other vehicles. \n4. in spring.")
    answer = get_answer()

    if answer == "1":
        print("Correct!")
        num = random.randint(1,10)
        get_question(num)
        
    else:
        print("Incorrect.")
        num = random.randint(1,10)
        get_question(num)
    
    
    
    
def question_seven():
    exclude_question(7)
    
    print("A solid white line indicates:")
    print("1. Two lanes travelling in different directions; passing is permitted \n2. Two lanes travelling in different directions; passing is not permitted \n3. Two lanes travelling in the same direction; passing is permitted \n4. Two lanes travelling in the same direction; passing is not permitted")
    answer = get_answer()

    if answer == "4":
        print("Correct!")
        num = random.randint(1,10)
        get_question(num)
        
    else:
        print("Incorrect.")
        num = random.randint(1,10)
        get_question(num)




def question_eight():
    exclude_question(8)
    
    print("If you are sitting in the passenger seat and are at least 18, you are allowed to not wear a seatbelt:")
    print("1. True \n2. False")
    answer = get_answer()

    if answer == "2":
        print("Correct!")
        num = random.randint(1,10)
        get_question(num)
        
    else:
        print("Incorrect.")
        num = random.randint(1,10)
        get_question(num)
    
    
    
    
def question_nine():
    exclude_question(9)
    
    print("When should you use your turn signal?")
    print("1.   Before changing lanes \n2. To turn at an intersection \n3. To  pull over on the shoulder of the road \n4. All of these")
    answer = get_answer()

    if answer == "4":
        print("Correct!")
        num = random.randint(1,10)
        get_question(num)
        
    else:
        print("Incorrect.")
        num = random.randint(1,10)
        get_question(num)
    
    
def question_ten():
    exclude_question(10)
    
    print("What should you do if a traffic light is flashing red.")
    print("1. Slow down before proceeding \n2. Stop only if there are other cars coming \nC. Stop and proceed when it’s safe to do so by following the right-of-way rules \n4. Stop, but only if the car in front has stopped ")
    answer = get_answer()

    if answer == "3":
        print("Correct!")
        num = random.randint(1,10)
        get_question(num)
        
    else:
        print("Incorrect.")
        num = random.randint(1,10)
        get_question(num)





##Retrieves randomized questions

def get_question(num):
    global used_question
    global count
    
    while count != 10:
        if num == 1 and num not in used_question:
            count = count + 1 
            question_one()
            
            
        elif num == 2 and num not in used_question:
            count = count + 1 
            question_two()
            
            
        elif num == 3 and num not in used_question:
            count = count + 1 
            question_three()
            
            
        elif num == 4 and num not in used_question:
            count = count + 1 
            question_four()
            
            
        elif num == 5 and num not in used_question:
            count = count + 1 
            question_five()
            
            
        elif num == 6 and num not in used_question:
            count = count + 1 
            question_six()
            
            
        elif num == 7 and num not in used_question:
            count = count + 1 
            question_seven()
            
            
        elif num == 8 and num not in used_question:
            count = count + 1 
            question_eight()
            
            
        elif num == 9 and num not in used_question:
            count = count + 1 
            question_nine()
            
            
        elif num == 10 and num not in used_question:
            count = count + 1 
            question_ten()
            
        else:
            num = random.randint(1,10)

def use_quiz():
    question_ten()
    