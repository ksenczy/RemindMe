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
from datetime import datetime

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

    #Setting up Event Block dates
    marchFifteenth = Label(homeWindow, text= "March 15th 2022", background = brown, foreground = "white", font=fontSettings).place(x=825, y=150)
    marchTwentySecond = Label(homeWindow, text="March 22nd 2022", background = brown, foreground = "white", font=fontSettings).place(x=825, y = 350)
    aprilFourth = Label(homeWindow, text="April 17th 2022", background = brown, foreground = "white", font=fontSettings).place(x=830, y = 700)
    timeLeft1 = Label(homeWindow, text = "Time Left:", background = brown, foreground = "white", font = fontSettings).place(x=1120, y=150)
    timeLeft2 = Label(homeWindow, text = "Time Left:", background = brown, foreground = "white", font = fontSettings).place(x=1120, y=350)
    timeLeft3 = Label(homeWindow, text = "Time Left:", background = brown, foreground = "white", font = fontSettings).place(x=1120, y=700)

    #Setting up Done? and its checkboxes
    doneLabel = Label(homeWindow, text = "Done?", background = brown, foreground = "white", font = fontSettings).place(x=1375, y=150)
    #Declaring vars for the checkboxes to work
    chk1 = IntVar()
    chk2 = IntVar()
    chk3 = IntVar()
    chk4 = IntVar()
    chk5 = IntVar()
    chk6 = IntVar()
    chk7 = IntVar()
    #Actually making the checkbuttons
    doneCheckbox1 = Checkbutton(homeWindow, variable = chk1, offvalue = 0, onvalue = 1).place(x=1400, y=220)
    doneCheckbox2 = Checkbutton(homeWindow, variable = chk2, offvalue = 0, onvalue = 1).place(x=1400, y=290)
    doneCheckbox3 = Checkbutton(homeWindow, variable = chk3, offvalue = 0, onvalue = 1).place(x=1400, y=420)
    doneCheckbox4 = Checkbutton(homeWindow, variable = chk4, offvalue = 0, onvalue = 1).place(x=1400, y=490)
    doneCheckbox5 = Checkbutton(homeWindow, variable = chk5, offvalue = 0, onvalue = 1).place(x=1400, y=570)
    doneCheckbox6 = Checkbutton(homeWindow, variable = chk6, offvalue = 0, onvalue = 1).place(x=1400, y=640)
    doneCheckbox7 = Checkbutton(homeWindow, variable = chk7, offvalue = 0, onvalue = 1).place(x=1400, y=765)


    #Hardcoding Events Here as Labels
    #We are presenting On March 15th, and as such all events will occur on or after that date
    #The first two events will have massively longer sections, as they are working fully for time until event
    currentTime = datetime.now()
    eventTime1 = datetime(2022, 3, 15, 15, 30)
    eventTime2 = datetime(2022, 3, 15, 20, 0)

    #First Event
    eventTime1 = -(currentTime - eventTime1)
    hours, minutes, seconds = convertTD(eventTime1) #converting EventTime into usable info
    if(hours == 1):
        hourFix = "Hour"
    else:
        hourFix = "Hours"
    if(minutes == 1):
        minuteFix = "Minute"
    else:
        minuteFix = "Minutes"
    if(seconds == 1):
        secondFix = "Second"
    else:
        secondFix = "Seconds"
    firstEvent = Label(homeWindow, background = "red", text = "CS 4120", font=eventFont, width = 35).place(x=525, y= 200)
    hourLabel1 = Label(homeWindow, background = "red", text = hours, font = timeFont).place(x=1070, y= 200)
    hourLabel2 = Label(homeWindow, background = "red", text = hourFix, font = timeFont).place(x=1050, y=225)
    minuteLabel1 = Label(homeWindow, background = "red", text = minutes, font=timeFont).place(x=1155, y=200)
    minuteLabel2 = Label(homeWindow, background = "red", text = minuteFix, font = timeFont).place(x=1130, y=225)
    secondLabel1 = Label(homeWindow, background = "red", text = seconds, font=timeFont).place(x=1250, y=200)
    secondLabel2 = Label(homeWindow, background = "red", text = secondFix, font = timeFont).place(x=1225, y=225)


    #Second Event
    eventTime2 = -(currentTime - eventTime2)
    hours, minutes, seconds = convertTD(eventTime2) #converting EventTime into usable info
    if(hours == 1):
        hourFix = "Hour"
    else:
        hourFix = "Hours"
    if(minutes == 1):
        minuteFix = "Minute"
    else:
        minuteFix = "Minutes"
    if(seconds == 1):
        secondFix = "Second"
    else:
        secondFix = "Seconds"
    secondEvent = Label(homeWindow, background = "red", text = "HIST 3014 Essay", font=eventFont, width = 35).place(x=525, y=275)
    secondHourLabel1 = Label(homeWindow, background = "red", text = hours, font = timeFont).place(x=1070, y= 275)
    secondHourLabel2 = Label(homeWindow, background = "red", text = hourFix, font = timeFont).place(x=1050, y=300)
    secondMinuteLabel1 = Label(homeWindow, background = "red", text = minutes, font=timeFont).place(x=1155, y=275)
    secondMinuteLabel2 = Label(homeWindow, background = "red", text = minuteFix, font = timeFont).place(x=1130, y=300)
    secondSecondLabel1 = Label(homeWindow, background = "red", text = seconds, font=timeFont).place(x=1250, y=275)
    secondSecondLabel2 = Label(homeWindow, background = "red", text = secondFix, font = timeFont).place(x=1225, y=300)


    #Third, Fourth, Fifth, and Sixth Events
    thirdEvent = Label(homeWindow, background = "green", text = "CS 4120", font=eventFont, width = 35).place(x=525, y= 400)
    fourthEvent = Label(homeWindow, background = "green", text = "ACM Meeting", font=eventFont, width = 35).place(x=525, y= 475)
    fifthEvent = Label(homeWindow, background = "green", text = "SOC 3170 Exam", font=eventFont, width = 35).place(x=525, y= 550)
    sixthEvent = Label(homeWindow, background = "green", text = "CS 3060", font=eventFont, width = 35).place(x=525, y= 625)

    #Seventh Event
    seventhEvent = Label(homeWindow, background = "green", text = "Easter", font=eventFont, width = 35).place(x=525, y= 750)

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
    createEventBtn = Button(menu, image = createEventImgAnchor, command = lambda : createEvent(False, homeWindow)).place(x=30, y=150)
    deleteEventBtn = Button(menu, image = deleteEventImgAnchor, command = deleteEvent).place(x=30, y=230)
    updateEventBtn = Button(menu, image = updateEventImgAnchor, command = lambda : createEvent(True, homeWindow)).place(x=30, y=310)
    searchEventBtn = Button(menu, image = searchEventImgAnchor, command = searchEvent).place(x=30, y=390)
    shareBtn = Button(menu, image = shareEventImgAnchor, command = shareEvent).place(x=30, y=470)
    sharedWithMeEventBtn = Button(menu, image = sharedWithEventImgAnchor, command = sharedWithMe).place(x=30, y=550)
    organizationsBtn = Button(menu, image = organizationsEventImgAnchor, command = organizations).place(x=30, y=630)
    holidaysBtn = Button(menu, image = holidaysEventImgAnchor, command = holidays).place(x=30, y=710)
    filterBtn = Button(menu, image = filtersEventImgAnchor, command = filters).place(x=30, y=790)
    settingsBtn = Button(menu, image = settingsEventImgAnchor, command = settings).place(x=30, y=870)

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
def createEvent(isUpdateFunction, homeWindow):

    #This is so we only have to use one function for both create and update
    if(isUpdateFunction):
        labelWords = "Update Event"
        searchEvent("U")
    else:
        labelWords = "Create Event"

    #Setting up the popup window
    popUp = Tk()
    popUp.title(labelWords)
    popUp.geometry('800x700')
    popUp.configure(bg=brown)

    #Setting up the top logo
    topLogo = Label(popUp, text = labelWords, font=eventFont, background = orange, width = 20, anchor = CENTER).place(x=180, y=25)

    #Event Name Label and Event Date
    eventNameLbl = Label(popUp, text = "Event Name:", background = brown, foreground = orange, font = fontSettings).place(x=140, y = 90)
    eventNameEntry = Entry(popUp, width = 50).place(x=350, y=100)
    eventDateLbl = Label(popUp, text = "Event Date:", background = brown, foreground = orange, font = fontSettings).place(x=140, y = 140)
    eventDateEntry1 = Entry(popUp, width = 5)
    eventDateEntry1.insert(0, "DD")
    eventDateEntry1.place(x=350, y=150)
    eventDateEntry2 = Entry(popUp, width = 5)
    eventDateEntry2.insert(0, "MM")
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
    daily = IntVar()
    weekly = IntVar()
    dailyCheckbox = Checkbutton(popUp, variable = daily, offvalue = 0, onvalue = 1, text = "Daily").place(x=350, y=370)
    weeklyCheckbox = Checkbutton(popUp, variable = weekly, offvalue = 0, onvalue = 1, text = "Weekly").place(x=450, y=370)
    eventNotifsLbl = Label(popUp, text = "Notifications:", background = brown, foreground = orange, font = fontSettings).place(x=140, y = 410)
    notifs = IntVar()
    notifsCheckbox = Checkbutton(popUp, variable = notifs, offvalue = 0, onvalue = 1, text = "On").place(x=350, y=420)

    #Event Type Boxes
    eventTimeLbl = Label(popUp, text = "Event Type:", background = brown, foreground = orange, font = fontSettings).place(x=140, y = 460)
    classBtn = IntVar()
    orgs = IntVar()
    hmwrk = IntVar()
    quiz = IntVar()
    personal = IntVar()
    holiday = IntVar()
    other = IntVar()
    classCheckbox = Checkbutton(popUp, variable = classBtn, offvalue = 0, onvalue = 1, text = "Class").place(x=350, y=470)
    orgsCheckbox = Checkbutton(popUp, variable = orgs, offvalue = 0, onvalue = 1, text = "Organization").place(x=450, y=470)
    hmwrkCheckbox = Checkbutton(popUp, variable = hmwrk, offvalue = 0, onvalue = 1, text = "Homework").place(x=350, y=500)
    quizCheckbox = Checkbutton(popUp, variable = quiz, offvalue = 0, onvalue = 1, text = "Quizzes & Exams").place(x=450, y=500)
    personalCheckbox = Checkbutton(popUp, variable = personal, offvalue = 0, onvalue = 1, text = "Personal").place(x=350, y=530)
    holidayCheckbox = Checkbutton(popUp, variable = holiday, offvalue = 0, onvalue = 1, text = "Holiday").place(x=450, y=530)
    otherCheckbox = Checkbutton(popUp, variable = other, offvalue = 0, onvalue = 1, text = "Other").place(x=400, y=560)

    #Add Event Button
    finalBtn = Button(popUp, text= labelWords, command= lambda : addDestroyer(isUpdateFunction, homeWindow, popUp),width = 20).place(x = 350, y = 650)

    buttonImage = Image.open(holder + "\Press Button.png")
    buttonImageAnchor = ImageTk.PhotoImage(buttonImage)


    popUp.mainloop()

#This is the clean up for the Add Event Function
#This Kills the pop up and Adds to the home screen a new event
#Or if its update, it updates the event
def addDestroyer(isUpdate, homeWindow, popUp):
    popUp.destroy()
    if(isUpdate):
        seventhEvent = Label(homeWindow, background = "green", text = "Haircut", font=eventFont, width = 35).place(x=525, y= 870)
    else:
        augustTwenth = Label(homeWindow, text="August 20th 2022", background = brown, foreground = "white", font=fontSettings).place(x=830, y = 820)
        timeLeft4 = Label(homeWindow, text = "Time Left:", background = brown, foreground = "white", font = fontSettings).place(x=1120, y=820)
        seventhEvent = Label(homeWindow, background = "green", text = "Bryce's Wedding", font=eventFont, width = 35).place(x=525, y= 870)


#Function def for delete event pop up
def deleteEvent():
    garbage = 0

#function def for searching for an event
def searchEvent(whatDo):

    #For update event pop up
    if (whatDo == "U"):
        garbage = 0

    garbage = 0

#function def for sharing an event
def shareEvent():
    garbage = 0

#function def for shared with me events
def sharedWithMe():
    garbage = 0

#function def for Organizations search
def organizations():
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
    orgsButton = Button(popUp, text="Search", command= lambda : orgSearchFrame(popUp, orgLbl.get()),width = 20).place(x = 185, y = 200)

    popUp.mainloop()

#This is for responding to the search from Organizations definition
def orgSearchFrame(popUp, searchTerm):
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
            chk1 = IntVar()
            chk2 = IntVar()
            cb1 = Checkbutton(coverUp, onvalue = 1, offvalue = 0, variable = chk1).place(x=400,y=190)
            cb2 = Checkbutton(coverUp, onvalue = 1, offvalue = 0, variable = chk2).place(x=400,y=255)
            addOrganizations = Button(coverUp, text = "Add Organizations", command = lambda : deletePopUp(popUp)).place(x=50, y=350)
            tryAgainButton = Button(coverUp, text = "Search Again", command = lambda : deleteFrames(coverUp)).place(x=350, y=350)

    if isIncluded != True:
        failedSearchLbl = Label(coverUp, text = "No Organizations found!", foreground = orange, background=brown, font=timeFont).place(x=35, y=80)
        tryAgainButton = Button(coverUp, text = "Search Again", command = lambda : deleteFrames(coverUp)).place(x=35, y=300)
        cancelButton = Button(coverUp, text = "Add Organizations", command = lambda : deletePopUp(popUp)).place(x=350, y=350)


    popUp.mainloop()


#This function deletes frames
def deleteFrames(frameName):
    frameName.destroy()

#this function deletes popups
def deletePopUp(popUp):
    popUp.destroy()


#function Def for holiday settings
def holidays():
    popUp = Tk()
    popUp.title("Holidays")
    popUp.geometry('500x400')
    popUp.configure(bg=brown)

    #Setting up the Vars
    chk1 = IntVar()
    chk2 = IntVar()
    chk3 = IntVar()
    chk4 = IntVar()
    chk5 = IntVar()
    chk6 = IntVar()
    chk7 = IntVar()
    chk8 = IntVar()
    chk9 = IntVar()
    chk10 = IntVar()
    chk11 = IntVar()
    chk12 = IntVar()
    chk13 = IntVar()
    chk14 = IntVar()

    #Setting Up the top bar
    holidayLabel = Label(popUp, text = "Holidays", font=eventFont, background = orange, width = 15, anchor = CENTER).place(x=75, y=20)

    #Religions
    christian = Checkbutton(popUp, variable = chk1, offvalue = 0, onvalue = 1, text = "Christianity").place(x=100, y=100)
    hinduisim = Checkbutton(popUp, variable = chk2, offvalue = 0, onvalue = 1, text = "Hinduism").place(x=100, y=135)
    taoism = Checkbutton(popUp, variable = chk3, offvalue = 0, onvalue = 1, text = "Taoism").place(x=100, y=170)
    islam = Checkbutton(popUp, variable = chk4, offvalue = 0, onvalue = 1, text = "Islam").place(x=100, y=205)
    judism = Checkbutton(popUp, variable = chk5, offvalue = 0, onvalue = 1, text = "Judism").place(x=100, y=240)
    buddhism = Checkbutton(popUp, variable = chk6, offvalue = 0, onvalue = 1, text = "Buddhism").place(x=100, y=275)
    sikhism = Checkbutton(popUp, variable = chk7, offvalue = 0, onvalue = 1, text = "Sikhism").place(x=100, y=310)

    #Countries
    usa = Checkbutton(popUp, variable = chk8, offvalue = 0, onvalue = 1, text = "United States").place(x=300, y=100)
    india = Checkbutton(popUp, variable = chk9, offvalue = 0, onvalue = 1, text = "India").place(x=300, y=135)
    china = Checkbutton(popUp, variable = chk10, offvalue = 0, onvalue = 1, text = "China").place(x=300, y=170)
    saudiArabia = Checkbutton(popUp, variable = chk11, offvalue = 0, onvalue = 1, text = "Saudi Arabia").place(x=300, y=205)
    canada = Checkbutton(popUp, variable = chk12, offvalue = 0, onvalue = 1, text = "Canada").place(x=300, y=240)
    mexico = Checkbutton(popUp, variable = chk13, offvalue = 0, onvalue = 1, text = "Mexico").place(x=300, y=275)
    uK = Checkbutton(popUp, variable = chk14, offvalue = 0, onvalue = 1, text = "United Kingdom").place(x=300, y=310)


    #Deletion Button
    addHolidays = Button(popUp, text = "Save Changes", command = lambda : deletePopUp(popUp)).place(x=200, y=350)


    #Loop dec
    popUp.mainloop()

#function def for Filter settings
def filters():
    garbage = 0

#Function def for Settings pop up
def settings():
    garbage = 0

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
