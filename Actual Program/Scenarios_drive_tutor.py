#Comic Sans Coalition
#Scenarios for drive tutor
#Carley, Tsega, Max, Tylen, Liz
#We have followed the academic dishonesty policy

 

def getChoice():     #this code (lines 8-13) was recyled from the choose.py game we did in programming 1.
    return int(input("Enter your choice: "))  
def invalidInput():   #it helps us to be able to have choices chosen and a backup so the code does not break if 
    print("Sorry, invalid input! Please try again!") #an invalid answer is given. 
    getChoice()
def WrongAnswer():
    print("Sorry! That answer wasn't the correct choice! Please try again to continue.")
    
 #for most of the code the functions are written in order from incorrect to correct to make the transition from part to part easy to follow in code.   
def Start():
    print("You have decided today is a good day for a drive.") #starter menu, gives the option of two routes to take city or country
    print("You begin driving, what scenery would you like?")
    print("Enter 1 for City. Enter 2 for Country.")
    choice=getChoice()
    if choice==1:
        City()
    elif choice==2:
        Country()
    else:
        invalidInput()
        
def City():  #city driving option. Has most of the scenarios.
    print(" ")
    print("You picked City driving. Today is a very bright and sunny day.")
    print("You find it increasingly difficult to see because the sun. What should you do?")
    print("Enter 1 for Breaking Immediately. \nEnter 2 for Pull over to the left side of the road. \nEnter 3 to Slow your speed and point your eyes to the right curb of the road.")
    choice=getChoice()
    if choice==1:
        ImmBreak()
    elif choice==2:
        LeftRoad()
    elif choice==3:
        SlowAndRight()
    else:
        invalidInput()
def ImmBreak():
    WrongAnswer()
    City()
def LeftRoad():
    WrongAnswer()
    City()
def SlowAndRight():
    print(" ")
    print("Yes! That is what you should do to continue driving safely. As you are driving you approach a stop sign.")
    print("When you stop another car also stops at the same time at the intersection. Who has the right of way?")
    print("Enter 1 to give the person to the right the right-of-way. Enter 2 to take your turn first.")
    choice=getChoice()
    if choice==1:
        Right_of_Way()
    elif choice==2:
        GoFirst()
    else:
        invalidInput()
def GoFirst():
    WrongAnswer()
    SlowAndRight()
    
def Right_of_Way():
    print(" ")
    print("Yes! That is what you need to do!.")
    print("After the person to your right goes, then you continue through the stop sign.")
    print("You continue driving and come across a school bus letting children off. What do you do?")
    print("Enter 1 to continue driving and be cautious of kids. \nEnter 2 to wait until kids are off the bus and the bus has resumed driving to continue.\nEnter 3 to just keep driving normally.")
    choice=getChoice()
    if choice==1:
        DriveCautious()
    elif choice==2:
        KidsOff()
    elif choice==3:
        DriveNorm()
    else:
        invalidInput()
def DriveCautious():
    WrongAnswer()
    Right_of_Way()
def DriveNorm():
    WrongAnswer()
    Right_of_Way()
def KidsOff():
    print(" ")
    print("Right! You need to stop and wait for all kids to be off the bus and the bus to stop signaling before you can continue.")
    print("It is against the law to not abide by this, and you can be subject to tickets for not following it.")
    print("You continue to drive and get on the highway. You come across a stoplight that is not working. You and other cars come across \nit at the same time. What do you do?")
    print("Enter 1 to treat it as a four-way stop sign. \nEnter 2 to continue driving and ignore the other drivers. \nEnter 3 to panic and slam on your breaks.")
    choice=getChoice()
    if choice==1:
        Four_Way()
    elif choice==2:
        IgnoreOthers()
    elif choice==3:
        Panic()
    else:
        invalidInput()
        
def IgnoreOthers():
    WrongAnswer()
    KidsOff()
def Panic():
    print(" ")
    print("No!!! You never want to panic while driving! This puts you and everyone else in danger!")
    WrongAnswer()
    KidsOff()
def Four_Way():
    print(" ")
    print("You're absolutely correct! You need to treat it as a four-way stop sign. Especially if there is no one there directing traffic.")
    print("This is the safest way to go about the situation, you should also call to report it to DOH once you reach a safe destination.")
    print("You decice to get on the interstate to practice your driving there, things are going smoothly. \nYou come upon an entrance ramp and see a car approaching, what do you do?")
    print("Enter 1 to increase your speed and pass the entrance ramp before the car can get to the interstate. \nEnter 2 to do nothing and keep driving how you were.")
    print("Enter 3 to Turn your blinker on to move to the left lane, when it is safe to merge, merge into the \nleft lane to give the driver trying to enter the space to safely enter the interstate.")
    choice=getChoice()
    if choice==1:
        SpeedUp()
    elif choice==2:
        do_Nothing()
    elif choice==3:
        BlinkandMerge()
    else:
        invalidInput()
def SpeedUp():
    WrongAnswer()
    Four_Way()
def do_Nothing():
    WrongAnswer()
    Four_Way()
def BlinkandMerge():
    print(" ")
    print("Exactly! You should give the driver ample time to decide and make a plan for how they are going to enter the interstate.")
    print("The way that they will enter is dependent upon what those on the interstate do, so you giving them the space to merge makes the situation safer.")
    print("You decide to get off the interstate, as it is getting late and you want to get home soon as you are not comfortable with night driving yet.")
    print("As you're driving you begin to hear a scraping noise and the steering wheel is less responsive than normal. What should you do?")
    print("Enter 1 to ignore the sound and continue driving home. \nEnter 2 to pull over once you have a safe place to pull off and inspect the sound.\nEnter 3 to immediately pull off the road and panic.")
    choice=getChoice()
    if choice==1:
        IgnoreSound()
    elif choice==2:
        PullandCheck()
    elif choice==3:
        ImmPull()
def IgnoreSound():
    WrongAnswer()
    BlinkandMerge()
def ImmPull():
    print("No! Do NOT panic!")
    WrongAnswer()
    BlinkandMerge()
def PullandCheck(): #this is the last the city based scenario questions, game will end and option to play again will be displayed as well.
    print(" ")
    print("Right! There could be something wrong with your alternator or your power steering. You need to make sure nothing is broken.")
    print("Once you determine it is safe to continue driving, you make it home and decide you've had enough practice for one day.")
    ThanksForPlaying()
 
 #most of the functions are set up the same way for country driving as well for smoother reading purposes.
def Country(): #country driving, has different scenarios, mostly for rural situations.
    print(" ")
    print("You decide to take a drive through the country side.")
    print("As you are driving, a deer jumps in front of you. What should you do?")
    print("Enter 1 to slam on the breaks and swerve out of the way. \nEnter 2 to ease on the breaks and wait for the deer to safely cross.")
    choice=getChoice()
    if choice==1:
        swerveDeer()
    elif choice==2:
        safeCrossDeer()
    else:
        invalidInput()
def swerveDeer():
    WrongAnswer()
    Country()
def safeCrossDeer():
    print(" ")
    print("Right! You should gently apply breaks to not hit it, and wait for it to cross before continuing on the road.")
    print("As you are driving, it begins to rain relatively hard, visibility is still okay though.")
    print("You come across a a large puddle, and you cannot see the road beneath it, it doesn't seem to have a current. What do you do?")
    print("Enter 1 to try to avoid the side where the puddle seems to have formed and drive towards the middle of the road through it. \nEnter 2 to just drive through it with no worries.")
    choice=getChoice()
    if choice==1:
        safePuddle()
    elif choice==2:
        dangerWater()
    else:
        invalidInput()
def dangerWater():
    WrongAnswer()
    safeCrossDeer()
def safePuddle():
    print(" ")
    print("You are correct! Even if it doesn't seem like a dangerous puddle, you need to be cautious.")
    print("As you keep driving, you see the road has seemed to flood ahead. How do you judge the depth of the water?")
    print("Enter 1 to get a stick and see how deep it is at the deepest point. \nEnter 2 to just guess it isn't too deep and continue driving. \nEnter 3 to watch what other cars do and copy them.")
    choice=getChoice()
    if choice==1:
        SafeStick()
    elif choice==2:
        guessAndgo()
    elif choice ==2:
        copyCat()
    else:
        invalidInput()
def guessAndgo():
    WrongAnswer()
    safePuddle()
def copyCat():
    WrongAnswer()
    safePuddle()
def SafeStick():
    print(" ")
    print("That's right! This is the safest way to judge the depth of the water.")
    print("You determine it is safe to cross the flooded area and continue to drive.")
    print("You see a police officer behind you turn their lights on, it seems you are getting pulled over. What do you do?")
    print("Enter 1 to ignore them and keep driving home. \nEnter 2 to pull over to the side of the road when it is safe to, and wait for them. \nEnter 3 to just swerve off the side of the road immediately.")
    choice=getChoice()
    if choice==1:
        Ignore_home()
    elif choice==2:
        PullOffSafe()
    elif choice==3:
        FastPullOff()
def FastPullOff():
    WrongAnswer()
    SafeStick()
def Ignore_home():
    WrongAnswer()
    SafeStick()
def PullOffSafe(): #Last scenario for country driving. will call ending function. game will end, option to restart appears too.
    print(" ")
    print("Exactly! You need to make sure it is safe to pull off to the side of the road and then wait for the officer to get out and come to you to do anything more.")
    print("She decided to let you off with a warning, as your break lights were out and you did not know.")
    print("You decide it is best to go home and try to practice driving more another day.")
    ThanksForPlaying()
    
def ThanksForPlaying():  #ends the scenarios and gives the option to play again.
    print(" ")
    print("Thank you for playing Drive Tutor. Hope to see you back again soon!")
    #Start()
    
    
          
        
