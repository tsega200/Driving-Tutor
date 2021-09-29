import PySimpleGUI as sg      #imports PySimpleGUI, which is important as you can imagine
import Quiz_Redone as qz      #imports the module Quiz_Redone to run the quiz aspect of our porgram
import Scenarios_drive_tutor as sdt


sg.ChangeLookAndFeel('Topanga')  #Changes the color scheme
def button1():
    print("Goodbye")
    def button3():
        qz.use_quiz()
        print("Done")
        windowb.unhide
    def button4():
        sdt.Start()
        
        print("Finished")
    subMenuLayout = {'Quiz':button3, 'Scenario Problems':button4}
    
    layout = [[sg.Text('Choose you piece', size=(29,1), justification='center')],  #This changes the text at the top    
              [sg.T(' ' * 10),sg.Button('Quiz')], #This changes the first button
              [sg.T(' ' * 10),sg.Button('Scenario Problems')]] #This changes the second button
              #[sg.T(' ' * 10),sg.Button('Study materials')]
    windowb = sg.Window('Comic Sans Coalition', layout)    
    event, values = windowb.Read()
    try:
        functionCall = subMenuLayout[event]
        functionCall()
    except:
        pass
    
    window.Close()
def button2():
    #print("Goodnight")
    layout = [[sg.Text('Welcome to Driving Tutor!', size=(29,1), justification= 'center', font=("Helvetica", 16))],  #This changes the text at the top    
                 [sg.Text('Name:', size=(8, 1)), sg.Input()], #This changes the first button
                 #[sg.Text('Here is some text.... and a place to enter text')]
                 [sg.Radio('Beginner ', "RADIO1", default=True, size=(10,1)), sg.Radio('Intermediate', "RADIO1"), sg.Radio('Expert', "RADIO1")]]
                 #[sg.Button('Submit')]] #This changes the second button
    
    windowc = sg.Window('Comic Sans Coalition', layout)    

    event, values = windowc.Read()
    
    window.Close()
mainMenuLayout = {'Existing User':button1, 'Create User Profile':button2}


layout = [[sg.Text('Driving Tutor!', size=(29,1), justification='center', font=("Helvetica", 16))],  #This changes the text at the top    
                 [sg.T(' ' * 10), sg.Button('Existing User', size=(30,2))], #This changes the first button
                 [sg.T(' ' * 10), sg.Button('Create User Profile', size=(30,2))]]
                  #This changes the second button

windowa = sg.Window('Comic Sans Coalition', layout)    
event, values = windowa.Read()
try:
    functionCall = mainMenuLayout[event]
    functionCall()
except:
    pass

#window.Close()


