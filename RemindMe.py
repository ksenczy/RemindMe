#Assignment:    Remind Me
#Group:         Wesley Blanco, Matt Lake, Minh Nguyen, Kayla Senczyszyn
#Due:           March 4th 2022
#Professor:     Dr. Chao
#
#
#TO DO LIST
#Make the pop ups work
#Attempt to fix the Button sizes on the Menu screen


from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
import os
from datetime import datetime, timedelta

class events:
    def __init__(self, name, date, comments, recurring, notifs, event):
        self.eventName = name
        self.eventDate = date
        self.comments = comments
        self.recurring = recurring
        self.notifs = notifs
        self.eventType = event


#declaring colors
orange = '#FD5000'
brown ='#4F2C1D'
#font
fontSettings = ("Times New Roman", 24)
eventFont = ("Times New Roman", 34)
timeFont = ("Times New Roman", 18)

#declaring the window
window = Tk()
window.title("Remind Me")
window.geometry('1920x1080')
window.configure(bg=brown)

#Important Global Variables
firstRun = True
eventCalendar = []
isFiltered = [False, False, False, False, False, False, False, False]


eventCalendar.append(events("Bryce's Wedding", datetime(2022, 8, 20, 20, 30),"",0,False,4))


#This will be where the window changes from Login to the Home Screen
def clickedLogin():
    #This if so we can show off a failed login
    if(passwordEntry.get() != "p"):
        failureLabel = Label(window,background = brown,foreground = "red", text="(!)Unable to sign in", font = ("Times New Roman", 25)).place(x=800, y=690)
    else:
        Homescreen()

#This function converts eventTime1 into hours, minutes and seconds from
#a passed Time Delta, which holds days, seconds and microseconds
def convertTD(eventTime1):
    days, seconds = eventTime1.days, eventTime1.seconds
    hours = days * 24 + seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = (seconds % 60)
    return hours, minutes, seconds


#This is the function for the home screen
def Homescreen():
    #Setting up the window
    window.destroy()
    homeWindow = Tk()
    homeWindow.title("Remind Me")
    homeWindow.geometry('1920x1080')
    homeWindow.configure(bg=brown)

    #Setting up the generic Labels for the home screen

    #Setting a black bar up
    #there are six labels for this so we dont have to mess with the image size
    blackBar = Image.open(holder + "\Black Bar.png")
    newTemp = ImageTk.PhotoImage(blackBar)
    blackBarLabel1 = Label(homeWindow, image = newTemp, background = brown).place(x=450, y = 25)
    blackBarLabel2 = Label(homeWindow, image = newTemp, background = brown).place(x=580, y = 25)
    blackBarLabel3 = Label(homeWindow, image = newTemp, background = brown).place(x=760, y = 25)
    blackBarLabel4 = Label(homeWindow, image = newTemp, background = brown).place(x=940, y = 25)
    blackBarLabel5 = Label(homeWindow, image = newTemp, background = brown).place(x=1120, y = 25)
    blackBarLabel6 = Label(homeWindow, image = newTemp, background = brown).place(x=1300, y = 25)

    #Setting up words
    agendaLbl = Label(homeWindow, background = orange, text = "Agenda", font = ("Times New Roman", 30), width = 35, anchor = CENTER).place(x=580, y= 50)
    remindMeLbl = Label(homeWindow, background = brown, foreground = "white", text = "Remind Me", font =("Times New Roman", 14)).place(x=1,y=1)

    #Setting New BG Logo
    bgLogo2 = Image.open(holder + "\BG Logo2.png")
    temp = ImageTk.PhotoImage(bgLogo2)
    bgImagelabel2 = Label(homeWindow, image = temp, background = brown).place(x=1550, y=50)

    #New Definitions for how to get events on screen
    agendaFrame(homeWindow)

    #Implimenting Hamburger Button
    hamburger = Image.open(holder + "\HB Button.png")
    hamburg = ImageTk.PhotoImage(hamburger)
    menuButton = Button(image = hamburg, command = lambda: menuExtended(homeWindow)).place(x=50,y=50)
    #These cover labels cover an ugly border that doesnt match the color scheme
    coverLabel1 = Label(text="This is stupid", background = brown, foreground = brown).place(x=50, y=40)
    coverLabel2 = Label(text="This is stupid", background = brown, foreground = brown).place(x=50, y=100)
    coverLabel3 = Label(text= "T", background = brown, foreground = brown, font = eventFont).place(x=100, y=55)
    coverLabel4 = Label(text= "T", background = brown, foreground = brown, font = eventFont).place(x=25, y=55)


    #Matts photo and user stuff
    mattPic = Image.open(holder + "\Matthew.png")
    mattPicAnchor = ImageTk.PhotoImage(mattPic)
    MattLabel1 = Label(image = mattPicAnchor).place(x = 1600, y = 650)
    MattLabel2 = Label(text = "Matthew Lake",background = brown, foreground = "white", font = fontSettings).place(x = 1620, y = 940)
    MattLabel3 = Label(text = "mrlake@bgsu.edu", background = brown, foreground = "white", font = fontSettings).place(x = 1620, y = 980)
    #again, this must be at the bottom of the Homescreen function to
    #make sure that things work
    #notably, photos dont work without this
    homeWindow.mainloop()

def deleteAgendaFrame(homeWindow):
    global agenda
    agenda.destroy()
    agendaFrame(homeWindow)

#This sets up the frame for the Agenda.
def agendaFrame(homeWindow):
    #Declaring the Frame
    s = Style()
    s.configure('My.TFrame', background=brown)
    #Setting up the frame
    global agenda
    agenda =Frame(homeWindow, style='My.TFrame')
    agenda.config()
    agenda.place(x=450,y=150, width = 1050, height = 900)

    #Setting the Global variable up
    global eventCalendar

    sortCalendar(eventCalendar)

    #Setting up info for the event Date
    if(eventCalendar):
        currentDate = eventCalendar[0].eventDate
        dateName = correctDates(currentDate)

        #Setting up color scheme for the events
        if currentDate.day == datetime.now().day and currentDate.month == datetime.now().month and currentDate.year == datetime.now().year:
            colorCheck = "red"
        else:
            colorCheck = "green"

    #this solves an issue regarding the Red green choices
    #And formatting the titles of spaces
    currentDate = currentDate + timedelta(days=1)
    ySetting = -60
    i = 0
    #Setting up a loop to present the events
    while i < 7 and i < len(eventCalendar):

        if isFiltered[eventCalendar[i].eventType] == False:

            #Setting up Date Labels
            if(currentDate.day != eventCalendar[i].eventDate.day or currentDate.month != eventCalendar[i].eventDate.month or currentDate.year != eventCalendar[i].eventDate.year):
                ySetting = ySetting + 60
                currentDate = eventCalendar[i].eventDate
                dateName = correctDates(currentDate)
                dateLabel = Label(agenda, background = brown, foreground = "white", text = dateName, font = fontSettings).place(x=375, y=ySetting)
                timeLeftLbl = Label(agenda, background = brown, foreground = "white", text = "Time Left:", font = fontSettings).place(x=650, y=ySetting)
                colorCheck = "green"
                ySetting = ySetting - 20 #This is for fixing a formating issue with these labels

            #Setting up the actual event label
            ySetting = ySetting + 75

            if currentDate.day == datetime.now().day and currentDate.month == datetime.now().month and currentDate.year == datetime.now().year:
                colorCheck = "red"

            eventLabel = Label(agenda, font = eventFont, text = eventCalendar[i].eventName, width = 35, background = colorCheck).place(x=50, y=ySetting)

            if currentDate.day == datetime.now().day and currentDate.month == datetime.now().month and currentDate.year == datetime.now().year:
                #labeling the time to go
                hMSLabel = Label(agenda, font = timeFont, text= "Hours  Minutes  Seconds",background = "red").place(x=600, y=ySetting+25)

                #Converting time to its correct time until event
                temp = eventCalendar[i].eventDate - datetime.now()
                hours, minutes, seconds = convertTD(temp)

                hoursLabel = Label(agenda, font=timeFont, text= hours, background = "red").place(x=625, y=ySetting)
                minuteLabel = Label(agenda, font=timeFont, text= minutes, background = "red").place(x=700, y=ySetting)
                secondLabel = Label(agenda, font=timeFont, text= seconds, background = "red").place(x=790, y=ySetting)
            #And now for days left
            else:
                temp = eventCalendar[i].eventDate - datetime.now()

                dayLabel = Label(agenda, font = timeFont, text= "Days",background = "green").place(x=695, y=ySetting+25)
                daysLabel = Label(agenda, font=timeFont, text= temp.days, background = "green").place(x=700, y=ySetting)


        i = i + 1
    ySetting = ySetting + 80
    refreshInfo = Button(agenda, text = "Refresh", command = lambda : deleteAgendaFrame(homeWindow)).place(x=425, y = ySetting)

#Function takes a datetime variable
#Function returns a string that states the date in words
def correctDates(currentDate):
    #Dictionary for months
    monthsOfYear = {1:'January',2:'February',3:'March',4:'April',
		5:'May',6:'June',7:'July',8:'August', 9:'September',
        10:'October',11:'November',12:'December'}

    dateName = str(monthsOfYear[currentDate.month])
    dateName = dateName + " " + str(currentDate.day) + " " + str(currentDate.year)

    return dateName

#This function sorts the list of events in the calendar.
#It also removes events that are past due
#This is bubble sort
def sortCalendar(eventCalendar):

    n = len(eventCalendar)

    #sorting by Bubble Sort
    for i in range(n-1):
        for j in range(0, n-i-1):
            if eventCalendar[j].eventDate > eventCalendar[j+1].eventDate:
                eventCalendar[j], eventCalendar[j + 1] = eventCalendar[j + 1], eventCalendar[j]

    #Removing expired dates
    for i in range(n-1):
        if eventCalendar[i].eventDate < datetime.now():
            del eventCalendar[i]

#This function builds the menu window, right into the side of the Home Screen
def menuExtended(homeWindow):
    #Setting Frame Style so that it can take a bg color
    s = Style()
    s.configure('My.TFrame', background=brown)

    #Setting up the frame
    menu=Frame(homeWindow, style='My.TFrame')
    menu.config()
    menu.place(x=0,y=0, width = 400, height = 1080)


    #Setting up Button images
    createEventImg = Image.open(holder + "\Create EventBtn.png")
    createEventImgAnchor = ImageTk.PhotoImage(createEventImg)
    deleteEventImg = Image.open(holder + "\Delete Event.png")
    deleteEventImgAnchor = ImageTk.PhotoImage(deleteEventImg)
    updateEventImg = Image.open(holder + "\TUpdate Event.png")
    updateEventImgAnchor = ImageTk.PhotoImage(updateEventImg)
    searchEventImg = Image.open(holder + "\Search Event.png")
    searchEventImgAnchor = ImageTk.PhotoImage(searchEventImg)
    shareEventImg = Image.open(holder + "\Share Event.png")
    shareEventImgAnchor = ImageTk.PhotoImage(shareEventImg)
    sharedWithEventImg = Image.open(holder + "\Shared With Me.png")
    sharedWithEventImgAnchor = ImageTk.PhotoImage(sharedWithEventImg)
    organizationsEventImg = Image.open(holder + "\Organizations.png")
    organizationsEventImgAnchor = ImageTk.PhotoImage(organizationsEventImg)
    holidaysEventImg = Image.open(holder + "\Holidays.png")
    holidaysEventImgAnchor = ImageTk.PhotoImage(holidaysEventImg)
    filtersEventImg = Image.open(holder + "\Filter.png")
    filtersEventImgAnchor = ImageTk.PhotoImage(filtersEventImg)
    settingsEventImg = Image.open(holder + "\Settings.png")
    settingsEventImgAnchor = ImageTk.PhotoImage(settingsEventImg)

    #Adding Buttons to the Frame for each menu option
    createEventBtn = Button(menu, image = createEventImgAnchor, command = lambda : createEvent(homeWindow)).place(x=30, y=150)
    deleteEventBtn = Button(menu, image = deleteEventImgAnchor, command = lambda : deleteEvent(True, homeWindow)).place(x=30, y=230)
    updateEventBtn = Button(menu, image = updateEventImgAnchor, command = lambda : deleteEvent(False, homeWindow)).place(x=30, y=310)
    searchEventBtn = Button(menu, image = searchEventImgAnchor, command = lambda : searchEventPopUp(False)).place(x=30, y=390)
    shareBtn = Button(menu, image = shareEventImgAnchor, command = lambda : searchEventPopUp(True)).place(x=30, y=470)
    sharedWithMeEventBtn = Button(menu, image = sharedWithEventImgAnchor, command = lambda : sharedWithMe(homeWindow)).place(x=30, y=550)
    organizationsBtn = Button(menu, image = organizationsEventImgAnchor, command = lambda : organizations(homeWindow)).place(x=30, y=630)
    holidaysBtn = Button(menu, image = holidaysEventImgAnchor, command = lambda : holidays(homeWindow)).place(x=30, y=710)
    filterBtn = Button(menu, image = filtersEventImgAnchor, command = lambda : filters(homeWindow)).place(x=30, y=790)
    settingsBtn = Button(menu, image = settingsEventImgAnchor, command = settings).place(x=30, y=870)


    #Setting up cover ups to hide the button outlines
    coveringIt1 = Label(menu, text="This is stupidfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff", background = brown, foreground = brown).place(x=30, y=140)
    coveringIt2 = Label(menu, text="This is stupidfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff", background = brown, foreground = brown).place(x=30, y=220)
    coveringIt3 = Label(menu, text="This is stupidfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff", background = brown, foreground = brown).place(x=30, y=300)
    coveringIt4 = Label(menu, text="This is stupidfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff", background = brown, foreground = brown).place(x=30, y=380)
    coveringIt5 = Label(menu, text="This is stupidfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff", background = brown, foreground = brown).place(x=30, y=460)
    coveringIt6 = Label(menu, text="This is stupidfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff", background = brown, foreground = brown).place(x=30, y=540)
    coveringIt7 = Label(menu, text="This is stupidfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff", background = brown, foreground = brown).place(x=30, y=620)
    coveringIt8 = Label(menu, text="This is stupidfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff", background = brown, foreground = brown).place(x=30, y=700)
    coveringIt9 = Label(menu, text="This is stupidfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff", background = brown, foreground = brown).place(x=30, y=780)
    coveringIt10 = Label(menu, text="This is stupidfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff", background = brown, foreground = brown).place(x=30, y=860)

    coveringIt11 = Label(menu, text="This is stupidfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff", background = brown, foreground = brown).place(x=30, y=213)
    coveringIt11 = Label(menu, text="This is stupidfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff", background = brown, foreground = brown).place(x=30, y=290)
    coveringIt11 = Label(menu, text="This is stupidfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff", background = brown, foreground = brown).place(x=30, y=369)
    coveringIt11 = Label(menu, text="This is stupidfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff", background = brown, foreground = brown).place(x=30, y=451)
    coveringIt11 = Label(menu, text="This is stupidfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff", background = brown, foreground = brown).place(x=30, y=530)
    coveringIt11 = Label(menu, text="This is stupidfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff", background = brown, foreground = brown).place(x=30, y=610)
    coveringIt11 = Label(menu, text="This is stupidfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff", background = brown, foreground = brown).place(x=30, y=690)
    coveringIt11 = Label(menu, text="This is stupidfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff", background = brown, foreground = brown).place(x=30, y=771)
    coveringIt11 = Label(menu, text="This is stupidfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff", background = brown, foreground = brown).place(x=30, y=851)
    coveringIt11 = Label(menu, text="This is stupidfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff", background = brown, foreground = brown).place(x=30, y=932)

    coveringIt11 = Label(menu, text="F", background = brown, foreground = brown, font = ("Times New Romans", 40)).place(x=10, y=150)
    coveringIt11 = Label(menu, text="F", background = brown, foreground = brown, font = ("Times New Romans", 40)).place(x=10, y=230)
    coveringIt11 = Label(menu, text="F", background = brown, foreground = brown, font = ("Times New Romans", 40)).place(x=10, y=310)
    coveringIt11 = Label(menu, text="F", background = brown, foreground = brown, font = ("Times New Romans", 40)).place(x=10, y=390)
    coveringIt11 = Label(menu, text="F", background = brown, foreground = brown, font = ("Times New Romans", 40)).place(x=10, y=470)
    coveringIt11 = Label(menu, text="F", background = brown, foreground = brown, font = ("Times New Romans", 40)).place(x=10, y=550)
    coveringIt11 = Label(menu, text="F", background = brown, foreground = brown, font = ("Times New Romans", 40)).place(x=10, y=630)
    coveringIt11 = Label(menu, text="F", background = brown, foreground = brown, font = ("Times New Romans", 40)).place(x=10, y=710)
    coveringIt11 = Label(menu, text="F", background = brown, foreground = brown, font = ("Times New Romans", 40)).place(x=10, y=790)
    coveringIt11 = Label(menu, text="F", background = brown, foreground = brown, font = ("Times New Romans", 40)).place(x=10, y=870)


    coveringIt11 = Label(menu, text="F", background = brown, foreground = brown, font = ("Times New Romans", 40)).place(x=325, y=150)
    coveringIt11 = Label(menu, text="F", background = brown, foreground = brown, font = ("Times New Romans", 40)).place(x=325, y=230)
    coveringIt11 = Label(menu, text="F", background = brown, foreground = brown, font = ("Times New Romans", 40)).place(x=325, y=310)
    coveringIt11 = Label(menu, text="F", background = brown, foreground = brown, font = ("Times New Romans", 40)).place(x=325, y=390)
    coveringIt11 = Label(menu, text="F", background = brown, foreground = brown, font = ("Times New Romans", 40)).place(x=325, y=470)
    coveringIt11 = Label(menu, text="F", background = brown, foreground = brown, font = ("Times New Romans", 40)).place(x=325, y=550)
    coveringIt11 = Label(menu, text="F", background = brown, foreground = brown, font = ("Times New Romans", 40)).place(x=325, y=630)
    coveringIt11 = Label(menu, text="F", background = brown, foreground = brown, font = ("Times New Romans", 40)).place(x=325, y=710)
    coveringIt11 = Label(menu, text="F", background = brown, foreground = brown, font = ("Times New Romans", 40)).place(x=325, y=790)
    coveringIt11 = Label(menu, text="F", background = brown, foreground = brown, font = ("Times New Romans", 40)).place(x=325, y=870)


    #Rebuilding the hamburger Button, clicking the hamburger button again destroys the frame and its contents
    hamburger = Image.open(holder + "\HB Button.png")
    hamburg = ImageTk.PhotoImage(hamburger)
    framedMenuButton = Button(menu, image = hamburg, command = lambda: menu.destroy()).place(x=50,y=50)
    #These cover labels cover an ugly border that doesnt match the color scheme
    coverLabel1 = Label(menu, text="This is stupid", background = brown, foreground = brown).place(x=50, y=40)
    coverLabel2 = Label(menu, text="This is stupid", background = brown, foreground = brown).place(x=50, y=100)
    coverLabel3 = Label(menu, text= "T", background = brown, foreground = brown, font = eventFont).place(x=100, y=55)
    coverLabel4 = Label(menu, text= "T", background = brown, foreground = brown, font = eventFont).place(x=25, y=55)

    #Once again, this has to be at the end of the function for
    #Image purposes
    homeWindow.mainloop()

#Function definition for Create Event pop up or Update Event
def createEvent(homeWindow):

    #Setting up the popup window
    popUp = Tk()
    popUp.title("Create Event")
    popUp.geometry('800x700')
    popUp.configure(bg=brown)

    #Setting up the top logo
    topLogo = Label(popUp, text = "Create Event", font=eventFont, background = orange, width = 20, anchor = CENTER).place(x=180, y=25)

    #Event Name Label and Event Date
    eventNameLbl = Label(popUp, text = "Event Name:", background = brown, foreground = orange, font = fontSettings).place(x=140, y = 90)
    eventNameEntry = Entry(popUp, width = 50)
    eventNameEntry.place(x=350, y=100)
    eventDateLbl = Label(popUp, text = "Event Date:", background = brown, foreground = orange, font = fontSettings).place(x=140, y = 140)
    eventDateEntry1 = Entry(popUp, width = 5)
    eventDateEntry1.insert(0, "MM")
    eventDateEntry1.place(x=350, y=150)
    eventDateEntry2 = Entry(popUp, width = 5)
    eventDateEntry2.insert(0, "DD")
    eventDateEntry2.place(x=415, y=150)
    eventDateEntry3 = Entry(popUp, width = 10)
    eventDateEntry3.insert(0, "YYYY")
    eventDateEntry3.place(x=480, y=150)
    slashLine1 = Label(popUp, font = fontSettings, background = brown, foreground = "black", text = "/").place(x=395,y=145)
    slashLine2 = Label(popUp, font = fontSettings, background = brown, foreground = "black", text = "/").place(x=460,y=145)

    #Event Time and Comments
    eventTimeLbl = Label(popUp, text = "Event Time:", background = brown, foreground = orange, font = fontSettings).place(x=140, y = 190)
    eventTimeEntry1 = Entry(popUp, width = 5)
    eventTimeEntry1.insert(0, "HH")
    eventTimeEntry1.place(x=350, y=200)
    eventTimeEntry2 = Entry(popUp, width = 5)
    eventTimeEntry2.insert(0, "MM")
    eventTimeEntry2.place(x=415, y=200)
    eventTimeEntry3 = Combobox(popUp, width = 7)
    eventTimeEntry3['values'] = ('AM', 'PM')
    eventTimeEntry3.current(0)
    eventTimeEntry3.place(x=480, y=200)
    slashLine1 = Label(popUp, font = fontSettings, background = brown, foreground = "black", text = ":").place(x=395,y=190)
    eventCommentsLbl = Label(popUp, text = "Comments:", background = brown, foreground = orange, font = fontSettings).place(x=140, y = 240)
    eventCommentsEntry = Entry(popUp)
    eventCommentsEntry.grid(padx = 350, pady = 250, ipadx = 50, ipady = 40)


    #Recurring boxes and Notification Boxes
    eventTimeLbl = Label(popUp, text = "Recurring:", background = brown, foreground = orange, font = fontSettings).place(x=140, y = 360)
    daily = IntVar(popUp)
    weekly = IntVar(popUp)
    dailyCheckbox = Checkbutton(popUp, variable = daily, offvalue = 0, onvalue = 1, text = "Daily").place(x=350, y=370)
    weeklyCheckbox = Checkbutton(popUp, variable = weekly, offvalue = 0, onvalue = 1, text = "Weekly").place(x=450, y=370)
    eventNotifsLbl = Label(popUp, text = "Notifications:", background = brown, foreground = orange, font = fontSettings).place(x=140, y = 410)
    notifs = IntVar(popUp)
    notifsCheckbox = Checkbutton(popUp, variable = notifs, offvalue = 0, onvalue = 1, text = "On").place(x=350, y=420)

    #Event Type Boxes
    eventTimeLbl = Label(popUp, text = "Event Type:", background = brown, foreground = orange, font = fontSettings).place(x=140, y = 460)
    classBtn = IntVar(popUp)
    orgs = IntVar(popUp)
    hmwrk = IntVar(popUp)
    quiz = IntVar(popUp)
    personal = IntVar(popUp)
    holiday = IntVar(popUp)
    other = IntVar(popUp)
    classCheckbox = Checkbutton(popUp, variable = classBtn, offvalue = 0, onvalue = 1, text = "Class").place(x=350, y=470)
    orgsCheckbox = Checkbutton(popUp, variable = orgs, offvalue = 0, onvalue = 1, text = "Organization").place(x=450, y=470)
    hmwrkCheckbox = Checkbutton(popUp, variable = hmwrk, offvalue = 0, onvalue = 1, text = "Homework").place(x=350, y=500)
    quizCheckbox = Checkbutton(popUp, variable = quiz, offvalue = 0, onvalue = 1, text = "Quizzes & Exams").place(x=450, y=500)
    personalCheckbox = Checkbutton(popUp, variable = personal, offvalue = 0, onvalue = 1, text = "Personal").place(x=350, y=530)
    holidayCheckbox = Checkbutton(popUp, variable = holiday, offvalue = 0, onvalue = 1, text = "Holiday").place(x=450, y=530)
    otherCheckbox = Checkbutton(popUp, variable = other, offvalue = 0, onvalue = 1, text = "Other").place(x=400, y=560)

    #Adding Event Button
    finalBtn = Button(popUp, text= "Create Event", command= lambda : eventAdder(homeWindow, popUp, \
    eventNameEntry.get(), datetime(int(eventDateEntry3.get()), int(eventDateEntry1.get()), int(eventDateEntry2.get()), int(eventTimeEntry1.get()), int(eventTimeEntry2.get())), eventTimeEntry3.get(), \
    eventCommentsEntry.get(), weekly.get(), daily.get(), notifs.get(), classBtn.get(), orgs.get(), hmwrk.get(), quiz.get(), personal.get(),holiday.get(),other.get()) \
    ,width = 20).place(x = 350, y = 650)

    popUp.mainloop()

def eventAdder(homeWindow, popUp, name, givenDate, AMPM, comments, weekly, daily, notifs, classEve, orgs, hmwrk, quiz, personal,holiday,other):
    global eventCalendar
    global agenda

    #Fixing PM issues
    if AMPM == "PM":
        givenDate = givenDate + timedelta(hours=12)

    #Setting up weekly VS Daily
    if daily == 1:
        recurring = 1
    elif weekly == 1:
        recurring = 2
    else:
        recurring = 0

    #Setting up Notifs
    if notifs == 1:
        fixer = True
    else:
        fixer = False

    #Event Type
    if classEve == 1:
        eventType = 0
    elif orgs == 1:
        eventType = 1
    elif hmwrk == 1:
        eventType = 2
    elif quiz == 1:
        eventType = 3
    elif personal == 1:
        eventType = 4
    elif holiday == 1:
        eventType = 5
    elif other == 1:
        eventType = 6
    else:
        eventType = 7


    eventCalendar.append(events(name, givenDate, comments, recurring,fixer, eventType))
    popUp.destroy()
    deleteAgendaFrame(homeWindow)


#Function def for delete event pop up
def deleteEvent(isDelete, homeWindow):

    if isDelete:
        labelWords = "Delete"
    else:
        labelWords = "Update"
    popUp = Tk()
    popUp.title(labelWords + " Event")
    popUp.geometry('700x450')
    popUp.configure(bg=brown)

    #Setting the top labels
    topLbl = Label(popUp, text = labelWords + " Events", font=eventFont, background = orange, width = 20, anchor = CENTER).place(x=130, y=20)
    explain = Label(popUp, text = "Enter an Event Name or Date", foreground = orange, background=brown, font=timeFont).place(x=180, y=80)
    searchLbl = Label(popUp, text = "Event Name:", foreground = orange, background=brown, font=timeFont).place(x=100, y=145)
    searchLbl = Label(popUp, text = "Event Date:", foreground = orange, background=brown, font=timeFont).place(x=100, y=195)
    #Setting up the entry boxes
    nameSearchEntry = Entry(popUp, width = 40)
    nameSearchEntry.insert(0, "Event Name...")
    nameSearchEntry.place(x=250, y=150)
    dateSearchEntry1 = Entry(popUp, width = 5)
    dateSearchEntry1.insert(0,"MM")
    dateSearchEntry1.place(x=250, y=200)
    dateSearchEntry2 = Entry(popUp, width = 5)
    dateSearchEntry2.insert(0,"DD")
    dateSearchEntry2.place(x=325, y=200)
    dateSearchEntry3 = Entry(popUp, width = 10)
    dateSearchEntry3.insert(0,"YYYY")
    dateSearchEntry3.place(x=400, y=200)
    #Slash lines to make it look good
    slashLine1 = Label(popUp, font = fontSettings, background = brown, foreground = "black", text = "/").place(x=300,y=190)
    slashLine2 = Label(popUp, font = fontSettings, background = brown, foreground = "black", text = "/").place(x=380,y=190)

    finalBtn = Button(popUp, text= "Find Event", command = lambda : deleteHunt(homeWindow, isDelete, popUp, nameSearchEntry.get(), dateSearchEntry3.get(), dateSearchEntry1.get(), dateSearchEntry2.get()), width = 15).place(x=300, y =250)

    popUp.mainloop()

def deleteHunt(homeWindow, isDelete, popUp, nameToFind, year, month, day):

    #Setting Frame Style so that it can take a bg color
    s = Style()
    s.configure('My.TFrame', background=brown)
    #Setting up the frame
    coverUp=Frame(popUp, style='My.TFrame')
    coverUp.config()
    coverUp.place(x=0,y=0, width = 700, height = 450)


    global eventCalendar
    sortCalendar(eventCalendar)

    if isDelete:
        labelWords = "Delete"
    else:
        labelWords = "Update"

    #This is used to cover the frame with brown
    coverLbl = Label(coverUp, text = "NICE", font = ("Times New Roman", 1000), foreground = brown, background = brown).place(x=0,y=0)


    temp = []
    #Find name Matches
    if nameToFind != "Event Name...":
        for ele in eventCalendar:
            if ele.eventName == nameToFind:
                temp.append(events(ele.eventName, ele.eventDate, ele.comments, ele.recurring, ele.notifs, ele.eventType))
    #Finding Date Matches
    if year != "YYYY" and month != "MM" and day != "DD":
        if year.isdigit() and month.isdigit() and day.isdigit:
            dtHolder = datetime(int(year), int(month), int(day))
            for ele in eventCalendar:
                if ele.eventDate.year == dtHolder.year and ele.eventDate.month == dtHolder.month and ele.eventDate.day == dtHolder.day:
                    temp.append(events(ele.eventName, ele.eventDate, ele.comments, ele.recurring, ele.notifs, ele.eventType))

    topLbl = Label(coverUp, text = labelWords + " Events", font=eventFont, background = orange, width = 20, anchor = CENTER).place(x=130, y=20)

    #Event Does exist in list
    if(temp):
        explain = Label(coverUp, text = "Event Found!", foreground = orange, background=brown, font=timeFont).place(x=300, y=80)

        chk1 = IntVar(coverUp)
        chk2 = IntVar(coverUp)
        chk4 = IntVar(coverUp)

        i = 0
        ySetting = 120
        while i < 3 and i < len(temp):
            dateFixed = correctDates(temp[i].eventDate)
            showEvent = Label(coverUp, font = eventFont, text = temp[i].eventName, width = 35, background = "green").place(x=0, y=ySetting)
            eventDate = Label(coverUp, font = timeFont, text = dateFixed, background = "green").place(x=475, y=ySetting+20)


            ySetting = ySetting + 15
            if(i == 0):
                chkbtn1 = Checkbutton(coverUp, offvalue = 0, onvalue = 1, variable = chk1)
                chkbtn1.place(x=675, y=ySetting)
            elif(i == 1):
                chkbtn2 = Checkbutton(coverUp, offvalue = 0, onvalue = 1, variable = chk2)
                chkbtn2.place(x=675, y=ySetting)
            elif(i == 2):
                chkbtn4 = Checkbutton(coverUp, offvalue = 0, onvalue = 1, variable = chk4)
                chkbtn4.place(x=675, y=ySetting)
            ySetting = ySetting + 60

            i = i + 1

            if(isDelete == False):
                if(chk1.get() == 1):
                    chk2.set(0)
                    chk4.set(0)
                if(chk2.get() == 1):
                    chk1.set(0)
                    chk4.set(0)
                if(chk4.get == 1):
                    chk1.set(0)
                    chk2.set(0)


        if(isDelete): #Deletion
            ySetting = ySetting + 30
            giveUp = Button(coverUp, text = "Delete Event", command = lambda : actualEventDeletion(homeWindow, popUp, temp, chk1.get(), chk2.get(), chk4.get()), width = 15).place(x=225, y=ySetting)
            finalBtn = Button(coverUp, text= "Search Again", command = lambda : deleteFrames(coverUp), width = 15).place(x=375, y =ySetting)
        else: #update
            giveUp = Button(coverUp, text = "Update Event", command = lambda : updateEvent(homeWindow, popUp, temp, chk1.get(), chk2.get(), chk4.get()), width = 15).place(x=375, y=ySetting)
            finalBtn = Button(coverUp, text= "Search Again", command = lambda : deleteFrames(coverUp), width = 15).place(x=225, y =ySetting)

    #Event does not exist in list
    else:
        explain = Label(coverUp, text = "Event Not Found!", foreground = "red", background=brown, font=timeFont).place(x=275, y=80)
        searchLbl = Label(popUp, text = "Event Name:", foreground = orange, background=brown, font=timeFont).place(x=100, y=145)
        searchLbl = Label(popUp, text = "Event Date:", foreground = orange, background=brown, font=timeFont).place(x=100, y=195)
        nameSearchEntry = Entry(coverUp, width = 40)
        nameSearchEntry.insert(0, "Event Name...")
        nameSearchEntry.place(x=250, y=150)
        dateSearchEntry1 = Entry(coverUp, width = 5)
        dateSearchEntry1.insert(0,"MM")
        dateSearchEntry1.place(x=250, y=200)
        dateSearchEntry2 = Entry(coverUp, width = 5)
        dateSearchEntry2.insert(0,"DD")
        dateSearchEntry2.place(x=325, y=200)
        dateSearchEntry3 = Entry(coverUp, width = 10)
        dateSearchEntry3.insert(0,"YYYY")
        dateSearchEntry3.place(x=400, y=200)
        #Slash lines to make it look good
        slashLine1 = Label(coverUp, font = fontSettings, background = brown, foreground = "black", text = "/").place(x=300,y=190)
        slashLine2 = Label(coverUp, font = fontSettings, background = brown, foreground = "black", text = "/").place(x=380,y=190)

        #give up ends search, final button causes recursion
        giveUp = Button(coverUp, text = "Cancel Search", command = lambda : deletePopUp(popUp), width = 15).place(x=375, y=250)
        finalBtn = Button(coverUp, text= "Try Again", command = lambda : deleteHunt(homeWindow, isDelete, popUp, nameSearchEntry.get(), dateSearchEntry3.get(), dateSearchEntry1.get(), dateSearchEntry2.get()), width = 15).place(x=225, y =250)


    coverUp.mainloop()

def actualEventDeletion(homeWindow, popUp, temp, event1, event2, event3):

    global eventCalendar
    #Checking the first Check box
    if event1 == 1:
        i = 0
        while i < len(eventCalendar):
            if eventCalendar[i].eventName == temp[0].eventName and eventCalendar[i].eventDate == temp[0].eventDate:
                del eventCalendar[i]
            i = i + 1

    #checking the second checkbox
    if event2 == 1:
        i = 0
        while i < len(eventCalendar):
            if eventCalendar[i].eventName == temp[1].eventName and eventCalendar[i].eventDate == temp[1].eventDate:
                del eventCalendar[i]
            i = i + 1

    #checking the third checkbox
    if event3 == 1:
        i = 0
        while i < len(eventCalendar):
            if eventCalendar[i].eventName == temp[2].eventName and eventCalendar[i].eventDate == temp[2].eventDate:
                del eventCalendar[i]
            i = i + 1

    deletePopUp(popUp)
    deleteAgendaFrame(homeWindow)



def updateEvent(homeWindow, popUp, temp, event1, event2, event3):
    #Setting up the popup window
    popUp.destroy()
    popUp = Tk()
    popUp.title("Update Event")
    popUp.geometry('800x700')
    popUp.configure(bg=brown)

    if(event1 == 1):
        name = temp[0].eventName
        date = temp[0].eventDate
        comments = temp[0].comments
        recurring = temp[0].recurring
        notifsGiven = temp[0].notifs
        eventType = temp[0].eventType
    elif(event2 == 1):
        name = temp[1].eventName
        date = temp[1].eventDate
        comments = temp[1].comments
        recurring = temp[1].recurring
        notifsGiven = temp[1].notifs
        eventType = temp[1].eventType
    elif(event3 == 1):
        name = temp[2].eventName
        date = temp[2].eventDate
        comments = temp[2].comments
        recurring = temp[2].recurring
        notifsGiven = temp[2].notifs
        eventType = temp[2].eventType
    else:
        deletePopUp(popUp)

    global eventCalendar
    #Checking the first Check box
    if event1 == 1:
        i = 0
        while i < len(eventCalendar):
            if eventCalendar[i].eventName == temp[0].eventName and eventCalendar[i].eventDate == temp[0].eventDate:
                del eventCalendar[i]
            i = i + 1

    #checking the second checkbox
    if event2 == 1:
        i = 0
        while i < len(eventCalendar):
            if eventCalendar[i].eventName == temp[1].eventName and eventCalendar[i].eventDate == temp[1].eventDate:
                del eventCalendar[i]
            i = i + 1

    #checking the third checkbox
    if event3 == 1:
        i = 0
        while i < len(eventCalendar):
            if eventCalendar[i].eventName == temp[2].eventName and eventCalendar[i].eventDate == temp[2].eventDate:
                del eventCalendar[i]
            i = i + 1

    #Setting up the top logo
    topLogo = Label(popUp, text = "Create Event", font=eventFont, background = orange, width = 20, anchor = CENTER).place(x=180, y=25)

    #Event Name Label and Event Date
    eventNameLbl = Label(popUp, text = "Event Name:", background = brown, foreground = orange, font = fontSettings).place(x=140, y = 90)
    eventNameEntry = Entry(popUp, width = 50)
    eventNameEntry.insert(0, name)
    eventNameEntry.place(x=350, y=100)
    eventDateLbl = Label(popUp, text = "Event Date:", background = brown, foreground = orange, font = fontSettings).place(x=140, y = 140)
    eventDateEntry1 = Entry(popUp, width = 5)
    eventDateEntry1.insert(0, date.month)
    eventDateEntry1.place(x=350, y=150)
    eventDateEntry2 = Entry(popUp, width = 5)
    eventDateEntry2.insert(0, date.day)
    eventDateEntry2.place(x=415, y=150)
    eventDateEntry3 = Entry(popUp, width = 10)
    eventDateEntry3.insert(0, date.year)
    eventDateEntry3.place(x=480, y=150)
    slashLine1 = Label(popUp, font = fontSettings, background = brown, foreground = "black", text = "/").place(x=395,y=145)
    slashLine2 = Label(popUp, font = fontSettings, background = brown, foreground = "black", text = "/").place(x=460,y=145)

    #Dealing with the AM/PM drop box
    fixer = False
    superTemp = date.hour
    if superTemp > 12:
        fixer = True
        superTemp = superTemp - 12

    #Event Time and Comments
    eventTimeLbl = Label(popUp, text = "Event Time:", background = brown, foreground = orange, font = fontSettings).place(x=140, y = 190)
    eventTimeEntry1 = Entry(popUp, width = 5)
    eventTimeEntry1.insert(0, superTemp)
    eventTimeEntry1.place(x=350, y=200)
    eventTimeEntry2 = Entry(popUp, width = 5)
    eventTimeEntry2.insert(0, date.minute)
    eventTimeEntry2.place(x=415, y=200)
    eventTimeEntry3 = Combobox(popUp, width = 7)
    eventTimeEntry3['values'] = ('AM', 'PM')
    if fixer == False:
        eventTimeEntry3.current(0)
    else:
        eventTimeEntry3.current(1)
    eventTimeEntry3.place(x=480, y=200)
    slashLine1 = Label(popUp, font = fontSettings, background = brown, foreground = "black", text = ":").place(x=395,y=190)
    eventCommentsLbl = Label(popUp, text = "Comments:", background = brown, foreground = orange, font = fontSettings).place(x=140, y = 240)
    eventCommentsEntry = Entry(popUp)
    eventCommentsEntry.insert(0, comments)
    eventCommentsEntry.grid(padx = 350, pady = 250, ipadx = 50, ipady = 40)


    #Recurring boxes and Notification Boxes
    eventTimeLbl = Label(popUp, text = "Recurring:", background = brown, foreground = orange, font = fontSettings).place(x=140, y = 360)
    daily = IntVar(popUp)
    weekly = IntVar(popUp)
    if recurring == 1:
        daily.set(1)
    elif recurring == 2:
        weekly.set(2)
    dailyCheckbox = Checkbutton(popUp, variable = daily, offvalue = 0, onvalue = 1, text = "Daily").place(x=350, y=370)
    weeklyCheckbox = Checkbutton(popUp, variable = weekly, offvalue = 0, onvalue = 1, text = "Weekly").place(x=450, y=370)
    eventNotifsLbl = Label(popUp, text = "Notifications:", background = brown, foreground = orange, font = fontSettings).place(x=140, y = 410)
    notifs = IntVar(popUp)
    if notifsGiven == 1:
        notifs.set(1)
    notifsCheckbox = Checkbutton(popUp, variable = notifs, offvalue = 0, onvalue = 1, text = "On").place(x=350, y=420)

    #Event Type Boxes
    eventTimeLbl = Label(popUp, text = "Event Type:", background = brown, foreground = orange, font = fontSettings).place(x=140, y = 460)
    classBtn = IntVar(popUp)
    orgs = IntVar(popUp)
    hmwrk = IntVar(popUp)
    quiz = IntVar(popUp)
    personal = IntVar(popUp)
    holiday = IntVar(popUp)
    other = IntVar(popUp)
    if eventType == 0:
        classBtn.set(1)
    if eventType == 1:
        orgs.set(1)
    if eventType == 2:
        hmwrk.set(1)
    if eventType == 3:
        quiz.set(1)
    if eventType == 4:
        personal.set(1)
    if eventType == 5:
        holiday.set(1)
    if eventType == 6:
        other.set(1)
    classCheckbox = Checkbutton(popUp, variable = classBtn, offvalue = 0, onvalue = 1, text = "Class").place(x=350, y=470)
    orgsCheckbox = Checkbutton(popUp, variable = orgs, offvalue = 0, onvalue = 1, text = "Organization").place(x=450, y=470)
    hmwrkCheckbox = Checkbutton(popUp, variable = hmwrk, offvalue = 0, onvalue = 1, text = "Homework").place(x=350, y=500)
    quizCheckbox = Checkbutton(popUp, variable = quiz, offvalue = 0, onvalue = 1, text = "Quizzes & Exams").place(x=450, y=500)
    personalCheckbox = Checkbutton(popUp, variable = personal, offvalue = 0, onvalue = 1, text = "Personal").place(x=350, y=530)
    holidayCheckbox = Checkbutton(popUp, variable = holiday, offvalue = 0, onvalue = 1, text = "Holiday").place(x=450, y=530)
    otherCheckbox = Checkbutton(popUp, variable = other, offvalue = 0, onvalue = 1, text = "Other").place(x=400, y=560)

    #Adding Event Button
    finalBtn = Button(popUp, text= "Update Event", command= lambda : eventAdder(homeWindow, popUp, \
    eventNameEntry.get(), datetime(int(eventDateEntry3.get()), int(eventDateEntry1.get()), int(eventDateEntry2.get()), int(eventTimeEntry1.get()), int(eventTimeEntry2.get())), eventTimeEntry3.get(), \
    eventCommentsEntry.get(), weekly.get(), daily.get(), notifs.get(), classBtn.get(), orgs.get(), hmwrk.get(), quiz.get(), personal.get(),holiday.get(),other.get()) \
    ,width = 20).place(x = 350, y = 650)

    popUp.mainloop()

#function def for searching for an event
def searchEventPopUp(isShare):
    if isShare:
        labelWords = "Share"
    else:
        labelWords = "Search"
    popUp = Tk()
    popUp.title(labelWords + " Event")
    popUp.geometry('700x450')
    popUp.configure(bg=brown)

    #Setting the top labels
    topLbl = Label(popUp, text = labelWords + " Events", font=eventFont, background = orange, width = 20, anchor = CENTER).place(x=130, y=20)
    explain = Label(popUp, text = "Enter an Event Name or Date", foreground = orange, background=brown, font=timeFont).place(x=180, y=80)
    searchLbl = Label(popUp, text = "Event Name:", foreground = orange, background=brown, font=timeFont).place(x=100, y=145)
    searchLbl = Label(popUp, text = "Event Date:", foreground = orange, background=brown, font=timeFont).place(x=100, y=195)
    #Setting up the entry boxes
    nameSearchEntry = Entry(popUp, width = 40)
    nameSearchEntry.insert(0, "Event Name...")
    nameSearchEntry.place(x=250, y=150)
    dateSearchEntry1 = Entry(popUp, width = 5)
    dateSearchEntry1.insert(0,"MM")
    dateSearchEntry1.place(x=250, y=200)
    dateSearchEntry2 = Entry(popUp, width = 5)
    dateSearchEntry2.insert(0,"DD")
    dateSearchEntry2.place(x=325, y=200)
    dateSearchEntry3 = Entry(popUp, width = 10)
    dateSearchEntry3.insert(0,"YYYY")
    dateSearchEntry3.place(x=400, y=200)
    #Slash lines to make it look good
    slashLine1 = Label(popUp, font = fontSettings, background = brown, foreground = "black", text = "/").place(x=300,y=190)
    slashLine2 = Label(popUp, font = fontSettings, background = brown, foreground = "black", text = "/").place(x=380,y=190)

    finalBtn = Button(popUp, text= labelWords + " Event", command = lambda : searchEvent(isShare, popUp, nameSearchEntry.get(), dateSearchEntry3.get(), dateSearchEntry1.get(), dateSearchEntry2.get()), width = 15).place(x=300, y =250)

    popUp.mainloop()

#Function Definition for searching for an event
#This also Does Sharing Events!
def searchEvent(isShare, popUp, nameToFind, year, month, day):
    #Setting Frame Style so that it can take a bg color
    s = Style()
    s.configure('My.TFrame', background=brown)
    #Setting up the frame
    coverUp=Frame(popUp, style='My.TFrame')
    coverUp.config()
    coverUp.place(x=0,y=0, width = 700, height = 450)


    if isShare:
        labelWords = "Share"
    else:
        labelWords = "Search"

    #This is used to cover the frame with brown
    coverLbl = Label(coverUp, text = "NICE", font = ("Times New Roman", 1000), foreground = brown, background = brown).place(x=0,y=0)

    global eventCalendar
    temp = []
    #Find name Matches
    if nameToFind != "Event Name...":
        for ele in eventCalendar:
            if ele.eventName == nameToFind:
                temp.append(events(ele.eventName, ele.eventDate, ele.comments, ele.recurring, ele.notifs, ele.eventType))
    #Finding Date Matches
    if year != "YYYY" and month != "MM" and day != "DD":
        if year.isdigit() and month.isdigit() and day.isdigit:
            dtHolder = datetime(int(year), int(month), int(day))
            for ele in eventCalendar:
                if ele.eventDate.year == dtHolder.year and ele.eventDate.month == dtHolder.month and ele.eventDate.day == dtHolder.day:
                    temp.append(events(ele.eventName, ele.eventDate, ele.comments, ele.recurring, ele.notifs, ele.eventType))


    topLbl = Label(coverUp, text = labelWords + " Events", font=eventFont, background = orange, width = 20, anchor = CENTER).place(x=130, y=20)

    #Event Does exist in list
    if(temp):
        explain = Label(coverUp, text = "Event Found!", foreground = orange, background=brown, font=timeFont).place(x=300, y=80)

        chk1 = IntVar(coverUp)
        chk2 = IntVar(coverUp)
        chk4 = IntVar(coverUp)

        i = 0
        ySetting = 120
        while i < 3 and i < len(temp):
            dateFixed = correctDates(temp[i].eventDate)
            showEvent = Label(coverUp, font = eventFont, text = temp[i].eventName, width = 35, background = "green").place(x=0, y=ySetting)
            eventDate = Label(coverUp, font = timeFont, text = dateFixed, background = "green").place(x=475, y=ySetting+20)


            ySetting = ySetting + 15
            if(isShare and i == 0):
                chkbtn1 = Checkbutton(coverUp, offvalue = 0, onvalue = 1, variable = chk1).place(x=675, y=ySetting)
            elif(isShare and i == 1):
                chkbtn2 = Checkbutton(coverUp, offvalue = 0, onvalue = 1, variable = chk2).place(x=675, y=ySetting)
            elif(isShare and i == 2):
                chkbtn4 = Checkbutton(coverUp, offvalue = 0, onvalue = 1, variable = chk4).place(x=675, y=ySetting)
            ySetting = ySetting + 60

            i = i + 1


        if(isShare):
            emailBait = Entry(coverUp, width = 30)
            emailBait.insert(0, "Email To Share To")
            emailBait.place(x=260, y=ySetting)
            ySetting = ySetting + 30
            giveUp = Button(coverUp, text = "Share Event", command = lambda : deletePopUp(popUp), width = 15).place(x=375, y=ySetting)
            finalBtn = Button(coverUp, text= "Search Again", command = lambda : deleteFrames(coverUp), width = 15).place(x=225, y =ySetting)
        else:
            giveUp = Button(coverUp, text = "End Search", command = lambda : deletePopUp(popUp), width = 15).place(x=375, y=ySetting)
            finalBtn = Button(coverUp, text= "Search Again", command = lambda : deleteFrames(coverUp), width = 15).place(x=225, y =ySetting)



    #Event does not exist in list
    else:
        explain = Label(coverUp, text = "Event Not Found!", foreground = "red", background=brown, font=timeFont).place(x=275, y=80)
        searchLbl = Label(popUp, text = "Event Name:", foreground = orange, background=brown, font=timeFont).place(x=100, y=145)
        searchLbl = Label(popUp, text = "Event Date:", foreground = orange, background=brown, font=timeFont).place(x=100, y=195)
        nameSearchEntry = Entry(coverUp, width = 40)
        nameSearchEntry.insert(0, "Event Name...")
        nameSearchEntry.place(x=250, y=150)
        dateSearchEntry1 = Entry(coverUp, width = 5)
        dateSearchEntry1.insert(0,"MM")
        dateSearchEntry1.place(x=250, y=200)
        dateSearchEntry2 = Entry(coverUp, width = 5)
        dateSearchEntry2.insert(0,"DD")
        dateSearchEntry2.place(x=325, y=200)
        dateSearchEntry3 = Entry(coverUp, width = 10)
        dateSearchEntry3.insert(0,"YYYY")
        dateSearchEntry3.place(x=400, y=200)
        #Slash lines to make it look good
        slashLine1 = Label(coverUp, font = fontSettings, background = brown, foreground = "black", text = "/").place(x=300,y=190)
        slashLine2 = Label(coverUp, font = fontSettings, background = brown, foreground = "black", text = "/").place(x=380,y=190)

        #give up ends search, final button causes recursion
        giveUp = Button(coverUp, text = "Cancel Search", command = lambda : deletePopUp(popUp), width = 15).place(x=375, y=250)
        finalBtn = Button(coverUp, text= "Try Again", command = lambda : searchEvent(isShare, popUp, nameSearchEntry.get(), dateSearchEntry3.get(), dateSearchEntry1.get(), dateSearchEntry2.get()), width = 15).place(x=225, y =250)

#function def for shared with me events
def sharedWithMe(homeWindow):
    popUp = Tk()
    popUp.title("Organization Search")
    popUp.geometry('500x400')
    popUp.configure(bg=brown)

    global firstRun
    global eventCalendar
    topLogo = Label(popUp, text = "Shared With Me", font=eventFont, background = orange, width = 20, anchor = CENTER).place(x=20, y=20)
    if(firstRun):
        explain = Label(popUp, text = "Wesley Blanco has sent you the event:", foreground = orange, background=brown, font=timeFont).place(x=45, y=80)
        fakeEvent = Label(popUp, text = "Group Meeting", font = eventFont, width = 40, background = "green").place(x=0, y=120)
        fakeDate = Label(popUp, text = "March 29 2022", font = timeFont, background = "green").place(x=350, y=120)
        fakeTime = Label(popUp, text = "9:30 PM", font = timeFont, background = "green").place(x=380, y=145)

        acceptBtn = Button(popUp, text = "Accept Event", command = lambda : eventAdder(homeWindow, popUp, "Group Meeting", datetime(2022, 3, 29, 9, 30), "PM", "", 0, 0, 0, 0, 0, 1, 0, 0, 0,0)).place(x=175, y=200)
        denyBtn = Button(popUp, text = "Deny Event", command = lambda : deletePopUp(popUp)).place(x=275, y=200)

        firstRun = False
    else:
        explain = Label(popUp, text = "No Events Shared with you right now", foreground = orange, background=brown, font=timeFont).place(x=60, y=80)
        leaveBtn = Button(popUp, text = "Exit", command = lambda : deletePopUp(popUp)).place(x=210, y=200)

    popUp.mainloop()

#function def for Organizations search
def organizations(homeWindow):
    popUp = Tk()
    popUp.title("Organization Search")
    popUp.geometry('500x400')
    popUp.configure(bg=brown)

    #Setting up the Top logo
    topOrg = Label(popUp, text = "Find Organization", font=eventFont, background = orange, width = 20, anchor = CENTER).place(x=20, y=20)
    explain = Label(popUp, text = "Enter an Organization to get events for them", foreground = orange, background=brown, font=timeFont).place(x=35, y=80)
    orgLbl = Entry(popUp, width = 50)
    orgLbl.place(x=100, y=150)

    #Button building
    orgsButton = Button(popUp, text="Search", command= lambda : orgSearchFrame(homeWindow, popUp, orgLbl.get()),width = 20).place(x = 185, y = 200)

    popUp.mainloop()

#This is for responding to the search from Organizations definition
def orgSearchFrame(homeWindow, popUp, searchTerm):
    #Setting up the frame
    coverUp= Frame(popUp)
    coverUp.config()
    coverUp.place(x=0,y=0, width = 500, height = 400)
    #I couldnt color the background properly so this next line does it
    #in a very, uh, less than ideal way
    backgroundColor = Label(coverUp, font=("Times New Roman", 900), text="Hidden Text", background = brown, foreground = brown).place(x=0,y=0)

    orgs = {'CS': ['ACM', 'WIC'], 'Sports': ['Hockey', 'Gymnastics'], 'Music': ['String Club', 'A Cappella Choir']}

    isIncluded = False

    foundLabel = Label(coverUp, text = "Find Organization", font=eventFont, background = orange, width = 20, anchor = CENTER).place(x=20, y=20)

    for key in orgs:
        if key == searchTerm:
            isIncluded = True
            orgFound = Label(coverUp, text = "We Found the following Organizations!", foreground = orange, background=brown, font=timeFont).place(x=35, y=80)
            yourSearch = Label(coverUp, text="Your Search : " + searchTerm, foreground = orange, background = brown, font=timeFont).place(x=20, y=120)
            myList = orgs[key]
            firstOrg = Label(coverUp, background = "green", text = myList[0], font=eventFont, width = 15).place(x=0, y= 175)
            secondOrg = Label(coverUp, background = "green", text = myList[1], font=eventFont, width = 15).place(x=0, y= 240)
            chk1 = IntVar(coverUp)
            chk2 = IntVar(coverUp)
            cb1 = Checkbutton(coverUp, onvalue = 1, offvalue = 0, variable = chk1)
            cb1.place(x=400,y=190)
            cb2 = Checkbutton(coverUp, onvalue = 1, offvalue = 0, variable = chk2)
            cb2.place(x=400,y=255)
            addOrganizations = Button(coverUp, text = "Add Organizations", command = lambda : addOrg(homeWindow, int(chk1.get()), int(chk2.get()), searchTerm, popUp)).place(x=50, y=350)
            tryAgainButton = Button(coverUp, text = "Search Again", command = lambda : deleteFrames(coverUp)).place(x=350, y=350)

    if isIncluded != True:
        failedSearchLbl = Label(coverUp, text = "No Organizations found!", foreground = orange, background=brown, font=timeFont).place(x=35, y=80)
        tryAgainButton = Button(coverUp, text = "Search Again", command = lambda : deleteFrames(coverUp)).place(x=35, y=300)
        cancelButton = Button(coverUp, text = "Add Organizations", command = lambda : deletePopUp(popUp)).place(x=350, y=350)


    popUp.mainloop()

def addOrg(homeWindow, org1, org2, searchTerm, popUp):
    print(org1)
    if org1 == 1:
        if searchTerm == 'CS':
            eventAdder(homeWindow, popUp, "ACM Meeting", datetime(2022, 4, 15, 4, 30), "PM", "", 0, 0, 0, 0, 1, 0, 0, 0, 0, 0)
        if searchTerm == 'Sports':
            eventAdder(homeWindow, popUp, "Hockey Practice", datetime(2022, 5, 11, 6, 0), "PM", "", 0, 0, 0, 0, 1, 0, 0, 0, 0, 0)
        if searchTerm == 'Music':
            eventAdder(homeWindow, popUp, "String Concert", datetime(2022, 3, 15, 7, 0), "PM", "", 0, 0, 0, 0, 1, 0, 0, 0, 0, 0)
    elif org2 == 1:
        if searchTerm == 'CS':
            eventAdder(homeWindow, popUp, "WIC Meeting", datetime(2022, 5, 20, 2, 30), "PM", "", 0, 0, 0, 0, 1, 0, 0, 0, 0, 0)
        if searchTerm == 'Sports':
            eventAdder(homeWindow, popUp, "Gymnastics Tournament", datetime(2022, 6, 15, 12, 30), "PM", "", 0, 0, 0, 0, 1, 0, 0, 0, 0, 0)
        if searchTerm == 'Music':
            eventAdder(homeWindow, popUp, "Choir Concert", datetime(2022, 3, 17, 4, 30), "PM", "", 0, 0, 0, 0, 1, 0, 0, 0, 0, 0)
    else:
        deletePopUp(popUp)


#This function deletes frames
def deleteFrames(frameName):
    frameName.destroy()

#this function deletes popups
def deletePopUp(popUp):
    popUp.destroy()

#function Def for holiday settings
def holidays(homeWindow):
    popUp = Tk()
    popUp.title("Holidays")
    popUp.geometry('500x400')
    popUp.configure(bg=brown)

    #Setting up the Vars
    chk1 = IntVar(popUp)
    chk2 = IntVar(popUp)
    chk3 = IntVar(popUp)
    chk4 = IntVar(popUp)
    chk5 = IntVar(popUp)
    chk6 = IntVar(popUp)
    chk7 = IntVar(popUp)
    chk8 = IntVar(popUp)
    chk9 = IntVar(popUp)
    chk10 = IntVar(popUp)
    chk11 = IntVar(popUp)
    chk12 = IntVar(popUp)
    chk13 = IntVar(popUp)
    chk14 = IntVar(popUp)

    #Setting Up the top bar
    holidayLabel = Label(popUp, text = "Holidays", font=eventFont, background = orange, width = 15, anchor = CENTER).place(x=75, y=20)

    #Religions
    christian = Checkbutton(popUp, variable = chk1, offvalue = 0, onvalue = 1, text = "Christianity")
    christian.place(x=100, y=100)
    hinduisim = Checkbutton(popUp, variable = chk2, offvalue = 0, onvalue = 1, text = "Hinduism")
    hinduisim.place(x=100, y=135)
    taoism = Checkbutton(popUp, variable = chk3, offvalue = 0, onvalue = 1, text = "Taoism")
    taoism.place(x=100, y=170)
    islam = Checkbutton(popUp, variable = chk4, offvalue = 0, onvalue = 1, text = "Islam")
    islam.place(x=100, y=205)
    judism = Checkbutton(popUp, variable = chk5, offvalue = 0, onvalue = 1, text = "Judaism")
    judism.place(x=100, y=240)
    buddhism = Checkbutton(popUp, variable = chk6, offvalue = 0, onvalue = 1, text = "Buddhism")
    buddhism.place(x=100, y=275)
    sikhism = Checkbutton(popUp, variable = chk7, offvalue = 0, onvalue = 1, text = "Sikhism")
    sikhism.place(x=100, y=310)

    #Countries
    usa = Checkbutton(popUp, variable = chk8, offvalue = 0, onvalue = 1, text = "United States")
    usa.place(x=300, y=100)
    india = Checkbutton(popUp, variable = chk9, offvalue = 0, onvalue = 1, text = "India")
    india.place(x=300, y=135)
    china = Checkbutton(popUp, variable = chk10, offvalue = 0, onvalue = 1, text = "China")
    china.place(x=300, y=170)
    saudiArabia = Checkbutton(popUp, variable = chk11, offvalue = 0, onvalue = 1, text = "Saudi Arabia")
    saudiArabia.place(x=300, y=205)
    canada = Checkbutton(popUp, variable = chk12, offvalue = 0, onvalue = 1, text = "Canada")
    canada.place(x=300, y=240)
    mexico = Checkbutton(popUp, variable = chk13, offvalue = 0, onvalue = 1, text = "Mexico")
    mexico.place(x=300, y=275)
    uK = Checkbutton(popUp, variable = chk14, offvalue = 0, onvalue = 1, text = "United Kingdom")
    uK.place(x=300, y=310)


    #Deletion Button
    addHolidays = Button(popUp, text = "Save Changes", command = lambda : holidayAdd(homeWindow, popUp, chk1.get(), chk2.get(), chk3.get(), \
    chk4.get(), chk5.get(), chk6.get(), chk7.get(), chk8.get(), chk9.get(), chk10.get(), chk11.get(), chk12.get(), chk13.get(), chk14.get())).place(x=125, y=350)
    cancelIt = Button(popUp, text = "Cancel", command = lambda : deletePopUp(popUp)).place(x=300, y=350)

    #Loop dec
    popUp.mainloop()

#This function adds the correct holiday to the event calendar
def holidayAdd(homeWindow, popUp, christian, hindu, taoist, islam, judaism, buddhism, sikhism, usa, india, china, saudiArabia, canada, mexico, uk):
    if christian == 1:
        eventCalendar.append(events("Easter", datetime(2022, 4, 17, 4, 30), "", 0, False, 6))
    if hindu == 1:
        eventCalendar.append(events("Diwali", datetime(2022, 10, 24, 4, 30), "", 0, False, 6))
    if taoist == 1:
        eventCalendar.append(events("Chinese New Year", datetime(2023, 1, 22, 4, 30), "", 0, False, 6))
    if islam == 1:
        eventCalendar.append(events("Ramadan Begins", datetime(2022, 4, 23, 4, 30), "", 0, False, 6))
    if judaism == 1:
        eventCalendar.append(events("Passover", datetime(2022, 4, 15, 4, 30), "", 0, False, 6))
    if buddhism == 1:
        eventCalendar.append(events("Vesak", datetime(2022, 5, 6, 4, 30), "", 0, False, 6))
    if sikhism == 1:
        eventCalendar.append(events("Vaisakhi", datetime(2022, 4, 14, 4, 30), "", 0, False, 6))
    if usa == 1:
        eventCalendar.append(events("Thanksgiving", datetime(2022, 11, 24, 4, 30), "", 0, False, 6))
    if india == 1:
        eventCalendar.append(events("Holi", datetime(2022, 3, 18, 4, 30), "", 0, False, 6))
    if china == 1:
        eventCalendar.append(events("Lantern Festival", datetime(2023, 2, 5, 4, 30), "", 0, False, 6))
    if saudiArabia == 1:
        eventCalendar.append(events("Eid al-Fitr", datetime(2022, 5, 2, 4, 30), "", 0, False, 6))
    if canada == 1:
        eventCalendar.append(events("Boxing Day", datetime(2022, 12, 26, 4, 30), "", 0, False, 6))
    if mexico == 1:
        eventCalendar.append(events("Dia de la Independence", datetime(2022, 9, 16, 4, 30), "", 0, False, 6))
    if uk == 1:
        eventCalendar.append(events("The Queen's Birthday", datetime(2022, 6, 11, 4, 30), "", 0, False, 6))


    deletePopUp(popUp)
    deleteAgendaFrame(homeWindow)

#function def for Filter settings
def filters(homeWindow):
    popUp = Tk()
    popUp.title("Settings")
    popUp.geometry('500x300')
    popUp.configure(bg=brown)

    holidayLabel = Label(popUp, text = "Filters", font=eventFont, background = orange, width = 15, anchor = CENTER).place(x=75, y=20)

    #Setting up the Vars
    chk1 = IntVar(popUp)
    chk2 = IntVar(popUp)
    chk3 = IntVar(popUp)
    chk4 = IntVar(popUp)
    chk5 = IntVar(popUp)
    chk6 = IntVar(popUp)
    chk7 = IntVar(popUp)

    global isFiltered

    #Setting buttons based on current Filters
    if isFiltered[0] == False:
        chk1.set(1)
    if isFiltered[1] == False:
        chk2.set(1)
    if isFiltered[2] == False:
        chk3.set(1)
    if isFiltered[3] == False:
        chk4.set(1)
    if isFiltered[4] == False:
        chk5.set(1)
    if isFiltered[5] == False:
        chk6.set(1)
    if isFiltered[6] == False:
        chk7.set(1)

    #Religions
    classes = Checkbutton(popUp, variable = chk1, offvalue = 0, onvalue = 1, text = "Classes")
    classes.place(x=140, y=100)
    organizations = Checkbutton(popUp, variable = chk2, offvalue = 0, onvalue = 1, text = "Organizations")
    organizations.place(x=260, y=100)
    hmwk = Checkbutton(popUp, variable = chk3, offvalue = 0, onvalue = 1, text = "Homework")
    hmwk.place(x=140, y=125)
    quiz = Checkbutton(popUp, variable = chk4, offvalue = 0, onvalue = 1, text = "Quizzes & Exams")
    quiz.place(x=260, y=125)
    personal = Checkbutton(popUp, variable = chk5, offvalue = 0, onvalue = 1, text = "Personal")
    personal.place(x=140, y=150)
    holiday = Checkbutton(popUp, variable = chk6, offvalue = 0, onvalue = 1, text = "Holiday")
    holiday.place(x=260, y=150)
    other = Checkbutton(popUp, variable = chk7, offvalue = 0, onvalue = 1, text = "Other")
    other.place(x=220, y=175)

    addFilters = Button(popUp, text = "Save Changes", command = lambda : filterAdd(homeWindow, popUp, chk1.get(), chk2.get(), chk3.get(), chk4.get(), chk5.get(), chk6.get(), chk7.get())).place(x=130, y=220)
    cancelIt = Button(popUp, text = "Cancel", command = lambda : deletePopUp(popUp)).place(x=275, y=220)

    popUp.mainloop()

def filterAdd(homeWindow, popUp, classes, orgs, hmwk, quiz, personal, holiday, other):

    global isFiltered

    if classes == 0:
        isFiltered[0] = True
    if orgs == 0:
        isFiltered[1] = True
    if hmwk == 0:
        isFiltered[2] = True
    if quiz == 0:
        isFiltered[3] = True
    if personal == 0:
        isFiltered[4] = True
    if holiday == 0:
        isFiltered[5] = True
    if other == 0:
        isFiltered[6] = True

    if classes == 1:
        isFiltered[0] = False
    if orgs == 1:
        isFiltered[1] = False
    if hmwk == 1:
        isFiltered[2] = False
    if quiz == 1:
        isFiltered[3] = False
    if personal == 1:
        isFiltered[4] = False
    if holiday == 1:
        isFiltered[5] = False
    if other == 1:
        isFiltered[6] = False

    deletePopUp(popUp)
    deleteAgendaFrame(homeWindow)

#Function def for Settings pop up
#No settings Functionality actually works, just a pop up
def settings():
    popUp = Tk()
    popUp.title("Settings")
    popUp.geometry('500x400')
    popUp.configure(bg=brown)

    #Setting Up the top bar
    holidayLabel = Label(popUp, text = "Settings", font=eventFont, background = orange, width = 15, anchor = CENTER).place(x=75, y=20)

    chk1 = IntVar(popUp)
    darkMode = Checkbutton(popUp, text = "Dark Mode", offvalue = 0, onvalue = 1, variable = chk1)
    darkMode.place(x=225, y=100)

    explain = Label(popUp, text = "When Do you want Notifications to Occur?", font = timeFont, background = brown, foreground = orange).place(x=40, y=150)

    chk2 = IntVar(popUp)
    chk3 = IntVar(popUp)
    chk4 = IntVar(popUp)
    chk5 = IntVar(popUp)
    chk6 = IntVar(popUp)
    chk7 = IntVar(popUp)
    chk8 = IntVar(popUp)
    chk9 = IntVar(popUp)

    btn1 = Checkbutton(popUp, text = "Thirty Minutes Before", offvalue = 0, onvalue = 1, variable = chk2)
    btn1.place(x=125, y=200)
    btn2 = Checkbutton(popUp, text = "One Hour Before", offvalue = 0, onvalue = 1, variable = chk3)
    btn2.place(x=300, y=200)
    btn3 = Checkbutton(popUp, text = "Two Hours Before", offvalue = 0, onvalue = 1, variable = chk4)
    btn3.place(x=125, y=225)
    btn4 = Checkbutton(popUp, text = "Twelve Hours Before", offvalue = 0, onvalue = 1, variable = chk5)
    btn4.place(x=300, y=225)
    btn5 = Checkbutton(popUp, text = "A Day Before", offvalue = 0, onvalue = 1, variable = chk6)
    btn5.place(x=125, y=250)
    btn6 = Checkbutton(popUp, text = "Three Days Before", offvalue = 0, onvalue = 1, variable = chk7)
    btn6.place(x=300, y=250)
    btn7 = Checkbutton(popUp, text = "Five Days Before", offvalue = 0, onvalue = 1, variable = chk8)
    btn7.place(x=125, y=275)
    btn8 = Checkbutton(popUp, text = "A Week Before", offvalue = 0, onvalue = 1, variable = chk9)
    btn8.place(x=300, y=275)


    apply = Button(popUp, text = "Apply Changes", command = lambda : deletePopUp(popUp)).place(x=100, y= 350)
    cancel = Button(popUp, text = "Cancel", command = lambda : deletePopUp(popUp)).place(x=325, y=350)


    popUp.mainloop()


#Setting up the login Screen
#Image
holder = os.getcwd()
bgLogo1 = Image.open(holder + "\BG Logo.png")
idk = ImageTk.PhotoImage(bgLogo1)
bgImagelabel = Label(image = idk, background = brown).place(x=475,y=-220)

#Remind Me Text
RemindMe = Label(window,background = brown,foreground = orange,text="Remind Me", font = ("Times New Roman", 100)).place(x=650, y=500)

#Username and Password Text and Buttons
userNameLabel = Label(window,background = brown,foreground = orange, text="Username:", font = fontSettings).place(x=800, y=750)
passwordLabel = Label(window,background = brown,foreground = orange, text="Password:", font = fontSettings).place(x=800, y=800)
userNameEntry = Entry(window).place(x=950, y=761)
passwordEntry = Entry(window, show="*")
passwordEntry.place(x=950, y=811)

#Login Button
loginBtnCell = Button(window, text="Login", command=clickedLogin,width = 20).place(x = 875, y = 900)

#Version Text
Version = Label(window,background = brown,foreground = orange,text="Version 1.0.0", font = ("Times New Roman", 14)).place(x=1800, y=1052)


#This keeps the window open for the application
#must always be at the bottom of the file
window.mainloop()
