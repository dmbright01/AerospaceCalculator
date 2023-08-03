"""
===============================================================================
ENGR 13000 Fall 2021

Program Description: GUI Aerospace Calculator using Tkinter
    

Assignment Information
    Assignment:     Project 4
    Author:     Dominick Bright, dmbright@purdue.edu

    Team ID:        LC#1 - 13

Contributor:    N/A
    My contributor(s) helped me:
    [N/A] understand the assignment expectations without
        telling me how they will approach it.
    [N/A] understand different ways to think about a solution
        without helping me plan my solution.
    [N/A] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor here as well.
    
ACADEMIC INTEGRITY STATEMENT
I have not used source code obtained from any other unauthorized
source, either modified or unmodified. Neither have I provided
access to my code to another. The project I am submitting
is my own original work.
===============================================================================
"""

import tkinter as tk #Used for GUI implementation
import math #Used for advanced math implementation
import os #Used for file opening 

def dragCalc():
    """Calculates drag force given user input and writes inputs and result to user history"""
    dragBox.delete(0.0, tk.END) #Deletes previous text from results box in the calculation window
    cdString = cdEntry.get() #Reads entry from text box in calculation window
    roString = roEntry.get() #Reads entry from text box in calculation window
    vString = vEntry.get() #Reads entry from text box in calculation window
    aString = aEntry.get() #Reads entry from text box in calculation window
    #Verifying user entry
    try:
        cd = float(cdEntry.get()) #Converts text entry from string to float
    except:
        #If string is not numerical, will populate input box with 0
        cd = 0
        cdEntry.insert(tk.END, cd) #Inserts 0 into textbox
    #Verifying user entry
    try:
        ro = float(roEntry.get()) #Converts text entry from string to float
    except:
        #If string is not numerical, will populate input box with 0
        ro = 0
        roEntry.insert(tk.END, ro) #Inserts 0 into textbox
    #Verifying user entry
    try:
        v = float(vEntry.get()) #Converts text entry from string to float
    except:
        #If string is not numerical, will populate input box with 0
        v = 0
        vEntry.insert(tk.END, v) #Inserts 0 into textbox
    #Verifying user entry
    try:
        a = float(aEntry.get()) #Converts text entry from string to float
    except:
        #If string is not numerical, will populate input box with 0
        a = 0
        aEntry.insert(tk.END, a) #Inserts 0 into textbox
    drag = cd * ((ro * (v ** 2)) / 2) * a #Calulating drag force
    text = str(drag) #Converting result to string
    #Verifying user entry
    if(cd < 0):
        #If input is negative, presents error message to user
        text = "ERROR: Drag Coefficient must be >= 0!"
    elif(ro < 0):
        #If input is negative, presents error message to user
        text = "ERROR: Density must be >= 0!"
    elif(a < 0):
        #If input is negative, presents error message to user
        text = "ERROR: Area must be >= 0!"
    dragBox.insert(tk.END, text) #Inserts result string ("text" variable) into results text box
    
    #Adding calculation to history
    title = ' Drag Calculator ' #Initializing title for history
    inputs = {'Coefficient of Drag: ': cdString,
              'Fluid Density: ': roString,
              'Velocity: ': vString,
              'Reference Area: ': aString}
    #Initializing dictionary for formatted output
    
    with open("history.txt", 'a') as file:
        #Opening history document for appending
        titleOffset = 78 #Initializing variable for title character spacing
        file.write(f"{title:*^{titleOffset}}\n\n") #Writes formatted title to history
        for k in inputs.keys():
            #Iterating through dictionary for writing inputs to history
            offset = 30 - len(k) #Initializing variable for input character spacing
            tempString = f'\t{k}{inputs[k]:>{offset}}\n'
            file.write(tempString) #Writes formatted input to history
        offset = 30 - len('RESULT: ')
        file.write(f'\tRESULT: {text:>{offset}}\n\n') #Writes formatted result to history


def liftCalc():
    """Calculates lift force given user input and writes inputs and result to user history"""
    liftBox.delete(0.0, tk.END) #Deletes previous text from results box in the calculation window
    clString = clEntry.get() #Reads entry from text box in calculation window
    roString = roEntry.get() #Reads entry from text box in calculation window
    vString = vEntry.get() #Reads entry from text box in calculation window
    aString = aEntry.get() #Reads entry from text box in calculation window
    #Verifying user entry
    try:
        cl = float(clEntry.get()) #Converts text entry from string to float
    except:
        #If string is not numerical, will populate input box with 0
        cl = 0
        clEntry.insert(tk.END, cl) #Inserts 0 into textbox
    #Verifying user entry
    try:
        ro = float(roEntry.get()) #Converts text entry from string to float
    except:
        #If string is not numerical, will populate input box with 0
        ro = 0
        roEntry.insert(tk.END, ro) #Inserts 0 into textbox
    #Verifying user entry
    try:
        v = float(vEntry.get()) #Converts text entry from string to float
    except:
        #If string is not numerical, will populate input box with 0
        v = 0
        vEntry.insert(tk.END, v) #Inserts 0 into textbox
    #Verifying user entry
    try:
        a = float(aEntry.get()) #Converts text entry from string to float
    except:
        #If string is not numerical, will populate input box with 0
        a = 0
        aEntry.insert(tk.END, a) #Inserts 0 into textbox
    lift = cl * ((ro * (v ** 2)) / 2) * a #Calulating lift force
    text = str(lift) #Converting result to string
    #Verifying user entry
    if(ro < 0):
        #If input is negative, presents error message to user
        text = "ERROR: Density must be >= 0!"
    elif(a < 0):
        #If input is negative, presents error message to user
        text = "ERROR: Area must be >= 0!"
    liftBox.insert(tk.END, text) #Inserts result string ("text" variable) into results text box
    
    #Adding calculation to history
    title = ' Lift Calculator ' #Initializing title for history
    inputs = {'Coefficient of Lift: ': clString,
              'Fluid Density: ': roString,
              'Velocity: ': vString,
              'Wing Area: ': aString}
    #Initializing dictionary for formatted output
        
    with open("history.txt", 'a') as file:
        #Opening history document for appending
        titleOffset = 78 #Initializing variable for title character spacing
        file.write(f"{title:*^{titleOffset}}\n\n") #Writes formatted title to history
        for k in inputs.keys():
            #Iterating through dictionary for writing inputs to history
            offset = 30 - len(k) #Initializing variable for input character spacing
            tempString = f'\t{k}{inputs[k]:>{offset}}\n'
            file.write(tempString) #Writes formatted input to history
        offset = 30 - len('RESULT: ')
        file.write(f'\tRESULT: {text:>{offset}}\n\n') #Writes formatted result to history
    
    
def rCalc():
    """Calculates Reynolds number given user input and writes inputs and result to user history"""
    rBox.delete(0.0, tk.END) #Deletes previous text from results box in the calculation window
    lString = lEntry.get() #Reads entry from text box in calculation window
    roString = roEntry.get() #Reads entry from text box in calculation window
    vString = vEntry.get() #Reads entry from text box in calculation window
    muString = muEntry.get() #Reads entry from text box in calculation window
    #Verifying user entry
    try:
        #If string is not numerical, will populate input box with 0
        l = float(lEntry.get()) #Converts text entry from string to float
    except:
        l = 0
        lEntry.insert(tk.END, l) #Inserts 0 into textbox
    try:
        #If string is not numerical, will populate input box with 0
        ro = float(roEntry.get()) #Converts text entry from string to float
    except:
        ro = 0
        roEntry.insert(tk.END, ro) #Inserts 0 into textbox
    try:
        #If string is not numerical, will populate input box with 0
        v = float(vEntry.get()) #Converts text entry from string to float
    except:
        v = 0
        vEntry.insert(tk.END, v) #Inserts 0 into textbox
    try:
        #If string is not numerical, will populate input box with 0
        mu = float(muEntry.get()) #Converts text entry from string to float
    except:
        mu = 0
        muEntry.insert(tk.END, mu) #Inserts 0 into textbox
    try:
        #If string is not numerical, will populate output box with 0
        r = (ro * v * l) / mu #Calculating reynolds number
    except:
        r = 0
    text = str(r) #Converting result to string
    #Verifying user entry
    if(ro < 0):
        #If input is negative, presents error message to user
        text = "ERROR: Density must be >= 0!"
    elif(mu < 0):
        #If input is negative, presents error message to user
        text = "ERROR: Viscocity must be >= 0!"
    rBox.insert(tk.END, text) #Inserts result string ("text" variable) into results text box
    
    #Adding calculation to history
    title = " Reynold's Number Calculator " #Initializing title for history
    inputs = {'Fluid Travel Length: ': lString,
              'Fluid Density: ': roString,
              'Velocity: ': vString,
              'Fluid Viscocity: ': muString}
    #Initializing dictionary for formatted output
    
    with open("history.txt", 'a') as file:
        #Opening history document for appending
        titleOffset = 78 #Initializing variable for title character spacing
        file.write(f"{title:*^{titleOffset}}\n\n") #Writes formatted title to history
        for k in inputs.keys():
            #Iterating through dictionary for writing inputs to history
            offset = 30 - len(k) #Initializing variable for input character spacing
            tempString = f'\t{k}{inputs[k]:>{offset}}\n'
            file.write(tempString) #Writes formatted input to history
        offset = 30 - len('RESULT: ')
        file.write(f'\tRESULT: {text:>{offset}}\n\n') #Writes formatted result to history
    
def eCalc():
    """Calculates eccentricity given user input and writes inputs and result to user history"""
    eBox.delete(0.0, tk.END) #Deletes previous text from results box in the calculation window
    aString = aEntry.get() #Reads entry from text box in calculation window
    bString = bEntry.get() #Reads entry from text box in calculation window
    #Verifying user entry
    try:
        #If string is not numerical, will populate input box with 0
        a = float(aEntry.get()) #Converts text entry from string to float
    except:
        a = 0
        aEntry.insert(tk.END, a) #Inserts 0 into textbox
    try:
        #If string is not numerical, will populate input box with 0
        b = float(bEntry.get()) #Converts text entry from string to float
    except:
        b = 0
        bEntry.insert(tk.END, b) #Inserts 0 into textbox
    e = (1 - ((b ** 2) / (a ** 2))) ** (1 / 2)  #Calculating eccentricity
    text = str(e) #Converting result to string
    #Verifying user entry
    if(a < 0):
        #If input is negative, presents error message to user
        text = "ERROR: Distance must be >= 0!"
    elif(b < 0):
        #If input is negative, presents error message to user
        text = "ERROR: Distance must be >= 0!"
    while(b > a):
        #While input for the semi-minor axis is larger than the semi-major axis, an error message will be displayed
        bEntry.delete(0, tk.END) #deletes text from input box
        b = 0
        bEntry.insert(tk.END, b) #Inserts 0 into textbox
        text = "ERROR: Semi-Major Axis must be >= Semi-Minor Axis!"
    eBox.insert(tk.END, text) #Inserts result string ("text" variable) into results text box
    
    #Adding calculation to history
    title = " Eccentricity Calculator " #Initializing title for history
    inputs = {'Semi-Major Axis: ': aString,
              'Semi-Minor Axis: ': bString}
    #Initializing dictionary for formatted output
    
    with open("history.txt", 'a') as file:
        #Opening history document for appending
        titleOffset = 78 #Initializing variable for title character spacing
        file.write(f"{title:*^{titleOffset}}\n\n") #Writes formatted title to history
        for k in inputs.keys():
            #Iterating through dictionary for writing inputs to history
            offset = 30 - len(k) #Initializing variable for input character spacing
            tempString = f'\t{k}{inputs[k]:>{offset}}\n'
            file.write(tempString) #Writes formatted input to history
        offset = 30 - len('RESULT: ')
        file.write(f'\tRESULT: {text:>{offset}}\n\n') #Writes formatted result to history
    
    
def pCalc():
    """Calculates orbital period given user input and writes inputs and result to user history"""
    pBox.delete(0.0, tk.END) #Deletes previous text from results box in the calculation window
    aString = aEntry.get() #Reads entry from text box in calculation window
    mString = mEntry.get() #Reads entry from text box in calculation window
    G = 6.674 * (10 ** -11)
    #Verifying user entry
    try:
        #If string is not numerical, will populate input box with 0
        a = float(aEntry.get()) #Converts text entry from string to float
    except:
        a = 0
        aEntry.insert(tk.END, a) #Inserts 0 into textbox
    try:
        #If string is not numerical, will populate input box with 0
        m = float(mEntry.get()) #Converts text entry from string to float
    except:
        m = 0
        mEntry.insert(tk.END, m) #Inserts 0 into textbox
    try:
        #If string is not numerical, will populate output box with 0
        p = (2 * math.pi) * ((a ** (3 / 2)) / ((G * m) ** (1 / 2))) #Calculating orbital period
        p /= 1000
    except:
        p = 0
    text = str(p) #Converting result to string
    #Verifying user entry
    if(m < 0):
        #If input is negative, presents error message to user
        text = "ERROR: Mass must be >= 0!"
    elif(a < 0):
        #If input is negative, presents error message to user
        text = "ERROR: Distance must be >= 0!"
    pBox.insert(tk.END, text) #Inserts result string ("text" variable) into results text box
    
    #Adding calculation to history
    title = " Orbital Period Calculator " #Initializing title for history
    inputs = {'Semi-Major Axis: ': aString,
              'Central Body Mass: ': mString}
    #Initializing dictionary for formatted output
    
    with open("history.txt", 'a') as file:
        #Opening history document for appending
        titleOffset = 78 #Initializing variable for title character spacing
        file.write(f"{title:*^{titleOffset}}\n\n") #Writes formatted title to history
        for k in inputs.keys():
            #Iterating through dictionary for writing inputs to history
            offset = 30 - len(k) #Initializing variable for input character spacing
            tempString = f'\t{k}{inputs[k]:>{offset}}\n'
            file.write(tempString) #Writes formatted input to history
        offset = 30 - len('RESULT: ')
        file.write(f'\tRESULT: {text:>{offset}}\n\n') #Writes formatted result to history
    
    
def dCalc():
    """Calculates atmospheric density given user input and writes inputs and result to user history"""
    dBox.delete(0.0, tk.END) #Deletes previous text from results box in the calculation window
    hString = hEntry.get() #Reads entry from text box in calculation window
    #Verifying user entry
    try:
        #If string is not numerical, will populate input box with 0
        h = float(hEntry.get()) #Converts text entry from string to float
    except:
        h = 0
        hEntry.insert(tk.END, h) #Inserts 0 into textbox
    t = 15.04 - (0.00649 * h) #Calculating atmospheric temperature
    p = 101.29 * (((t + 273.1) / 288.08) ** 5.256) #Calculating atmospheric pressure
    d = p / (0.2869 * (t + 273.1)) #Calculating atmospheric density
    text = str(d) #Converting result to string
    #Verifying user entry
    if(h < 0):
        #If input is negative, presents error message to user
        text = "ERROR: Height must be >= 0!"
    dBox.insert(tk.END, text) #Inserts result string ("text" variable) into results text box
    
    #Adding calculation to history
    title = " Atmospheric Density Calculator " #Initializing title for history
    inputs = {'Altitude: ': hString}
    #Initializing dictionary for formatted output
    
    with open("history.txt", 'a') as file:
        #Opening history document for appending
        titleOffset = 78 #Initializing variable for title character spacing
        file.write(f"{title:*^{titleOffset}}\n\n") #Writes formatted title to history
        for k in inputs.keys():
            #Iterating through dictionary for writing inputs to history
            offset = 30 - len(k) #Initializing variable for input character spacing
            tempString = f'\t{k}{inputs[k]:>{offset}}\n'
            file.write(tempString) #Writes formatted input to history
        offset = 30 - len('RESULT: ')
        file.write(f'\tRESULT: {text:>{offset}}\n\n') #Writes formatted result to history


def dragWindow():
    """Opens window for user inputs for drag force calculation"""
    global dragBox #Setting object scope to global, to allow editing outside of function
    global cdEntry #Setting object scope to global, to allow editing outside of function
    global roEntry #Setting object scope to global, to allow editing outside of function
    global vEntry #Setting object scope to global, to allow editing outside of function
    global aEntry #Setting object scope to global, to allow editing outside of function
    newWindow = tk.Toplevel(master) #Toplevel object which will be treated as a new window
    newWindow.configure(bg='light blue') #Changing background color to light blue
 
    newWindow.title("Drag Force Calculator") #Setting window title

    newWindow.geometry("400x400") #Setting window geometry (area in pixels)

    #Creating new label object for input
    tk.Label(newWindow, text ="Enter Coefficient of Drag", bg='light blue', fg='black').place(relx=0.5, rely=0.05, anchor=tk.CENTER)
    cdEntry = tk.Entry(newWindow) #Creating new text entry object for input
    cdEntry.place(relx=0.5, rely=0.125, anchor=tk.CENTER) #Setting x and y position for text entry object
    
    #Creating new label object for input
    tk.Label(newWindow, text ="Enter Fluid Density (kg/m^3)", bg='light blue', fg='black').place(relx=0.5, rely=0.20, anchor=tk.CENTER)
    roEntry = tk.Entry(newWindow) #Creating new text entry object for input
    roEntry.place(relx=0.5, rely=0.275, anchor=tk.CENTER) #Setting x and y position for text entry object
    
    #Creating new label object for input
    tk.Label(newWindow, text ="Enter Velocity (m/s)", bg='light blue', fg='black').place(relx=0.5, rely=0.35, anchor=tk.CENTER)
    vEntry = tk.Entry(newWindow) #Creating new text entry object for input
    vEntry.place(relx=0.5, rely=0.425, anchor=tk.CENTER) #Setting x and y position for text entry object
    
    #Creating new label object for input
    tk.Label(newWindow, text ="Enter Reference Area (m^2)", bg='light blue', fg='black').place(relx=0.5, rely=0.50, anchor=tk.CENTER)
    aEntry = tk.Entry(newWindow) #Creating new text entry object for input
    aEntry.place(relx=0.5, rely=0.575, anchor=tk.CENTER) #Setting x and y position for text entry object
    
    #Creating new label object for output
    tk.Label(newWindow, text ="Drag Force Result (N)", bg='light blue', fg='black').place(relx=0.5, rely=0.70, anchor=tk.CENTER)
    dragBox = tk.Text(newWindow, height = 2, width = 52) #Creating new text box object for output
    dragBox.place(relx=0.5, rely=0.775, anchor=tk.CENTER) #Setting x and y position for text box object
    
    #Creating new button object for calculation
    newButton = tk.Button(newWindow, text='Calculate', highlightbackground='light blue', command=dragCalc)
    newButton.place(relx=0.5, rely=0.90, anchor=tk.CENTER) #Setting x and y position for button object
    
    newWindow.mainloop() #Loop for window, acts as a runtime


def liftWindow():
    """Opens window for user inputs for lift force calculation"""
    global liftBox #Setting object scope to global, to allow editing outside of function
    global clEntry #Setting object scope to global, to allow editing outside of function
    global roEntry #Setting object scope to global, to allow editing outside of function
    global vEntry #Setting object scope to global, to allow editing outside of function
    global aEntry #Setting object scope to global, to allow editing outside of function
    newWindow = tk.Toplevel(master) #Toplevel object which will be treated as a new window
    newWindow.configure(bg='light blue') #Changing background color to light blue
 
    newWindow.title("Lift Force Calculator") #Setting window title

    newWindow.geometry("400x400") #Setting window geometry (area in pixels)

    #Creating new label object for input
    tk.Label(newWindow, text ="Enter Coefficient of Lift", bg='light blue', fg='black').place(relx=0.5, rely=0.05, anchor=tk.CENTER)
    clEntry = tk.Entry(newWindow) #Creating new text entry object for input
    clEntry.place(relx=0.5, rely=0.125, anchor=tk.CENTER) #Setting x and y position for text entry object
    
    #Creating new label object for input
    tk.Label(newWindow, text ="Enter Fluid Density (kg/m^3)", bg='light blue', fg='black').place(relx=0.5, rely=0.20, anchor=tk.CENTER)
    roEntry = tk.Entry(newWindow) #Creating new text entry object for input
    roEntry.place(relx=0.5, rely=0.275, anchor=tk.CENTER) #Setting x and y position for text entry object
    
    #Creating new label object for input
    tk.Label(newWindow, text ="Enter Velocity (m/s)", bg='light blue', fg='black').place(relx=0.5, rely=0.35, anchor=tk.CENTER)
    vEntry = tk.Entry(newWindow) #Creating new text entry object for input
    vEntry.place(relx=0.5, rely=0.425, anchor=tk.CENTER) #Setting x and y position for text entry object
    
    #Creating new label object for input
    tk.Label(newWindow, text ="Enter Wing Area (m^2)", bg='light blue', fg='black').place(relx=0.5, rely=0.50, anchor=tk.CENTER)
    aEntry = tk.Entry(newWindow) #Creating new text entry object for input
    aEntry.place(relx=0.5, rely=0.575, anchor=tk.CENTER) #Setting x and y position for text entry object
    
    #Creating new label object for output
    tk.Label(newWindow, text ="Lift Force Result (N)", bg='light blue', fg='black').place(relx=0.5, rely=0.70, anchor=tk.CENTER)
    liftBox = tk.Text(newWindow, height = 2, width = 52) #Creating new text box object for output
    liftBox.place(relx=0.5, rely=0.775, anchor=tk.CENTER) #Setting x and y position for text box object
    
    #Creating new button object for calculation
    newButton = tk.Button(newWindow, text='Calculate', highlightbackground='light blue', command=liftCalc)
    newButton.place(relx=0.5, rely=0.90, anchor=tk.CENTER) #Setting x and y position for button object
    
    newWindow.mainloop() #Loop for window, acts as a runtime


def reynoldWindow():
    """Opens window for user inputs for reynold's number calculation"""
    global rBox #Setting object scope to global, to allow editing outside of function
    global lEntry #Setting object scope to global, to allow editing outside of function
    global roEntry #Setting object scope to global, to allow editing outside of function
    global vEntry #Setting object scope to global, to allow editing outside of function
    global muEntry #Setting object scope to global, to allow editing outside of function
    newWindow = tk.Toplevel(master) #Toplevel object which will be treated as a new window
    newWindow.configure(bg='light blue') #Changing background color to light blue
 
    newWindow.title("Reynold's Number Calculator") #Setting window title

    newWindow.geometry("400x400") #Setting window geometry (area in pixels)

    #Creating new label object for input
    tk.Label(newWindow, text ="Enter Fluid Travel Length", bg='light blue', fg='black').place(relx=0.5, rely=0.05, anchor=tk.CENTER)
    lEntry = tk.Entry(newWindow) #Creating new text entry object for input
    lEntry.place(relx=0.5, rely=0.125, anchor=tk.CENTER) #Setting x and y position for text entry object
    
    #Creating new label object for input
    tk.Label(newWindow, text ="Enter Fluid Density (kg/m^3)", bg='light blue', fg='black').place(relx=0.5, rely=0.20, anchor=tk.CENTER)
    roEntry = tk.Entry(newWindow) #Creating new text entry object for input
    roEntry.place(relx=0.5, rely=0.275, anchor=tk.CENTER) #Setting x and y position for text entry object
    
    #Creating new label object for input
    tk.Label(newWindow, text ="Enter Velocity (m/s)", bg='light blue', fg='black').place(relx=0.5, rely=0.35, anchor=tk.CENTER)
    vEntry = tk.Entry(newWindow) #Creating new text entry object for input
    vEntry.place(relx=0.5, rely=0.425, anchor=tk.CENTER) #Setting x and y position for text entry object
    
    #Creating new label object for input
    tk.Label(newWindow, text ="Enter Viscocity (Pa * s)", bg='light blue', fg='black').place(relx=0.5, rely=0.50, anchor=tk.CENTER)
    muEntry = tk.Entry(newWindow) #Creating new text entry object for input
    muEntry.place(relx=0.5, rely=0.575, anchor=tk.CENTER) #Setting x and y position for text entry object
    
    #Creating new label object for output
    tk.Label(newWindow, text ="Reynold's Number Result", bg='light blue', fg='black').place(relx=0.5, rely=0.70, anchor=tk.CENTER)
    rBox = tk.Text(newWindow, height = 2, width = 52) #Creating new text box object for output
    rBox.place(relx=0.5, rely=0.775, anchor=tk.CENTER) #Setting x and y position for text box object
    
    #Creating new button object for calculation
    newButton = tk.Button(newWindow, text='Calculate', highlightbackground='light blue', command=rCalc)
    newButton.place(relx=0.5, rely=0.90, anchor=tk.CENTER) #Setting x and y position for button object
    
    newWindow.mainloop() #Loop for window, acts as a runtime
    
    
def eccentricityWindow():
    """Opens window for user inputs for eccentricity calculation"""
    global eBox #Setting object scope to global, to allow editing outside of function
    global aEntry #Setting object scope to global, to allow editing outside of function
    global bEntry #Setting object scope to global, to allow editing outside of function
    newWindow = tk.Toplevel(master) #Toplevel object which will be treated as a new window
    newWindow.configure(bg='light blue') #Changing background color to light blue
 
    newWindow.title("Eccentricity Calculator") #Setting window title

    newWindow.geometry("400x400") #Setting window geometry (area in pixels)

    #Creating new label object for input
    tk.Label(newWindow, text ="Enter Semi-Major Axis (km)", bg='light blue', fg='black').place(relx=0.5, rely=0.175, anchor=tk.CENTER)
    aEntry = tk.Entry(newWindow) #Creating new text entry object for input
    aEntry.place(relx=0.5, rely=0.25, anchor=tk.CENTER) #Setting x and y position for text entry object
    
    #Creating new label object for input
    tk.Label(newWindow, text ="Enter Semi-Minor Axis (km)", bg='light blue', fg='black').place(relx=0.5, rely=0.425, anchor=tk.CENTER)
    bEntry = tk.Entry(newWindow) #Creating new text entry object for input
    bEntry.place(relx=0.5, rely=0.5, anchor=tk.CENTER) #Setting x and y position for text entry object
    
    #Creating new label object for output
    tk.Label(newWindow, text ="Eccentricity Result", bg='light blue', fg='black').place(relx=0.5, rely=0.675, anchor=tk.CENTER)
    eBox = tk.Text(newWindow, height = 2, width = 52) #Creating new text box object for output
    eBox.place(relx=0.5, rely=0.75, anchor=tk.CENTER) #Setting x and y position for text box object
    
    #Creating new button object for calculation
    newButton = tk.Button(newWindow, text='Calculate', highlightbackground='light blue', command=eCalc)
    newButton.place(relx=0.5, rely=0.90, anchor=tk.CENTER) #Setting x and y position for button object
    
    newWindow.mainloop() #Loop for window, acts as a runtime
    
    
def periodWindow():
    """Opens window for user inputs for orbital period calculation"""
    global pBox #Setting object scope to global, to allow editing outside of function
    global aEntry #Setting object scope to global, to allow editing outside of function
    global mEntry #Setting object scope to global, to allow editing outside of function
    newWindow = tk.Toplevel(master) #Toplevel object which will be treated as a new window
    newWindow.configure(bg='light blue') #Changing background color to light blue
 
    newWindow.title("Orbital Period Calculator") #Setting window title

    newWindow.geometry("400x400") #Setting window geometry (area in pixels)

    #Creating new label object for input
    tk.Label(newWindow, text ="Enter Semi-Major Axis (km)", bg='light blue', fg='black').place(relx=0.5, rely=0.175, anchor=tk.CENTER)
    aEntry = tk.Entry(newWindow) #Creating new text entry object for input
    aEntry.place(relx=0.5, rely=0.25, anchor=tk.CENTER) #Setting x and y position for text entry object
    
    #Creating new label object for input
    tk.Label(newWindow, text ="Enter Central Body Mass (kg)", bg='light blue', fg='black').place(relx=0.5, rely=0.425, anchor=tk.CENTER)
    mEntry = tk.Entry(newWindow) #Creating new text entry object for input
    mEntry.place(relx=0.5, rely=0.5, anchor=tk.CENTER) #Setting x and y position for text entry object
    
    #Creating new label object for output
    tk.Label(newWindow, text ="Orbital Period Result (yr)", bg='light blue', fg='black').place(relx=0.5, rely=0.675, anchor=tk.CENTER)
    pBox = tk.Text(newWindow, height = 2, width = 52) #Creating new text box object for output
    pBox.place(relx=0.5, rely=0.75, anchor=tk.CENTER) #Setting x and y position for text box object
    
    #Creating new button object for calculation
    newButton = tk.Button(newWindow, text='Calculate', highlightbackground='light blue', command=pCalc)
    newButton.place(relx=0.5, rely=0.90, anchor=tk.CENTER) #Setting x and y position for button object
    
    newWindow.mainloop() #Loop for window, acts as a runtime
    
    
def densityWindow():
    """Opens window for user inputs for atmospheric density calculation"""
    global dBox #Setting object scope to global, to allow editing outside of function
    global hEntry #Setting object scope to global, to allow editing outside of function
    newWindow = tk.Toplevel(master) #Toplevel object which will be treated as a new window
    newWindow.configure(bg='light blue') #Changing background color to light blue
 
    newWindow.title("Atmospheric Density Calculator") #Setting window title

    newWindow.geometry("400x400") #Setting window geometry (area in pixels)

    #Creating new label object for input
    tk.Label(newWindow, text ="Enter Altitude (m)", bg='light blue', fg='black').place(relx=0.5, rely=0.325, anchor=tk.CENTER)
    hEntry = tk.Entry(newWindow) #Creating new text entry object for input
    hEntry.place(relx=0.5, rely=0.40, anchor=tk.CENTER) #Setting x and y position for text entry object
    
    #Creating new label object for output
    tk.Label(newWindow, text ="Atmospheric Density (kg / m^3)", bg='light blue', fg='black').place(relx=0.5, rely=0.625, anchor=tk.CENTER)
    dBox = tk.Text(newWindow, height = 2, width = 52) #Creating new text box object for output
    dBox.place(relx=0.5, rely=0.70, anchor=tk.CENTER) #Setting x and y position for text box object
    
    #Creating new button object for calculation
    newButton = tk.Button(newWindow, text='Calculate', highlightbackground='light blue', command=dCalc)
    newButton.place(relx=0.5, rely=0.90, anchor=tk.CENTER) #Setting x and y position for button object
    
    newWindow.mainloop() #Loop for window, acts as a runtime
    

def startfile(fn):
    """Opens file using OS, given a filename"""
    os.system('open %s' % fn) #Uses OS to open file with given filename


def playVideo1():
    """Opens video for drag force equation"""
    startfile('dragforce.mp4') #Opens video and plays
    
    
def playVideo2():
    """Opens video for lift force equation"""
    startfile('liftforce.mp4') #Opens video and plays
    
    
def playVideo3():
    """Opens video for reynold's number equation"""
    startfile('rn.mp4') #Opens video and plays
    
    
def playVideo4():
    """Opens video for eccentricity equation"""
    startfile('eccentricity.mp4') #Opens video and plays
    
    
def playVideo5():
    """Opens video for orbital period equation"""
    startfile('orbitalperiod.mp4') #Opens video and plays
    
    
def playVideo6():
    """Opens video for atmospheric density equation"""
    startfile('atmosdensity.mp4') #Opens video and plays
    

def tutorialsWindow():
    """Opens window for tutorial video options"""
    newWindow = tk.Toplevel(master) #Toplevel object which will be treated as a new window
    newWindow.configure(bg='light blue') #Changing background color to light blue
 
    newWindow.title("Tutorial Player") #Setting window title

    newWindow.geometry("600x600") #Setting window geometry (area in pixels)
    
    #Creating new button object for selection
    b1 = tk.Button(newWindow, text='Drag Force Tutorial', highlightbackground='light blue', command=playVideo1)
    b1.place(relx=0.5, rely=0.15, anchor=tk.CENTER) #Setting x and y position for button object
    
    #Creating new button object for selection
    b2 = tk.Button(newWindow, text='Lift Force Tutorial', highlightbackground='light blue', command=playVideo2)
    b2.place(relx=0.5, rely=0.25, anchor=tk.CENTER) #Setting x and y position for button object
    
    #Creating new button object for selection
    b3 = tk.Button(newWindow, text='Reynold\'s Number Tutorial', highlightbackground='light blue', command=playVideo3)
    b3.place(relx=0.5, rely=0.35, anchor=tk.CENTER) #Setting x and y position for button object
    
    #Creating new button object for selection
    b4 = tk.Button(newWindow, text='Orbit Eccentricity Tutorial', highlightbackground='light blue', command=playVideo4)
    b4.place(relx=0.5, rely=0.45, anchor=tk.CENTER) #Setting x and y position for button object
    
    #Creating new button object for selection
    b5 = tk.Button(newWindow, text='Orbital Period Tutorial', highlightbackground='light blue', command=playVideo5)
    b5.place(relx=0.5, rely=0.55, anchor=tk.CENTER) #Setting x and y position for button object
    
    #Creating new button object for selection
    b6 = tk.Button(newWindow, text='Atmospheric Density Tutorial', highlightbackground='light blue', command=playVideo6)
    b6.place(relx=0.5, rely=0.65, anchor=tk.CENTER) #Setting x and y position for button object
    
    #Creating new label object for disclaimer
    labelText = "DISCLAIMER: I DO NOT OWN ANY OF THESE INTELLECTUAL PROPERTIES\nTHESE VIDEOS ARE FOR GENERAL USE ONLY"
    Label = tk.Label(newWindow, text=labelText, bg='light blue', fg='black', relief=tk.RAISED)
    Label.place(relx=0.5, rely=0.75, anchor=tk.CENTER) #Setting x and y position for label object
    
    
def openHistory():
    """Opens user history"""
    startfile("history.txt") #Opens history file
    
#Start of global main code:
    
#Wiping previous user history
with open("history.txt", 'w') as file:
    file.write('')
    
#Copying works cited to history
with open("workscited.txt", "r") as file:
    lines = file.readlines()

with open("history.txt", 'a') as file:
    file.write(f"{' WORKS CITED ':*^78}\n\n") #Writing formatted title 
    for l in lines:
        file.write(l) #Writing every line of works cited document to history document
    file.write("\n\n")

master = tk.Tk() #Creates new Tk object for top-level window
master.geometry('500x500') #Setting window geometry
master.configure(background="light blue") #Sets window background color
master.title("Aerospace Calculator") #Sets window title

f1 = tk.Frame(master) #Initializing new frame using top-level window object

labelText = "Welcome to the Aerospace Calculator! Please select an option"
#Creating new label object for title
mainLabel = tk.Label(master, text=labelText, bg='light blue', fg='black', relief=tk.RAISED)
mainLabel.place(relx=0.5, rely=0.05, anchor=tk.CENTER) #Setting x and y position for label object

#Creating new button object for selection
b1 = tk.Button(master, text='Drag Force Calculator', highlightbackground='light blue', command=dragWindow)
b1.place(relx=0.5, rely=0.15, anchor=tk.CENTER) #Setting x and y position for button object

#Creating new button object for selection
b2 = tk.Button(master, text='Lift Force Calculation', highlightbackground='light blue', command=liftWindow)
b2.place(relx=0.5, rely=0.25, anchor=tk.CENTER) #Setting x and y position for button object

#Creating new button object for selection
b3 = tk.Button(master, text="Reynold's Number Calculation", highlightbackground='light blue', command=reynoldWindow)
b3.place(relx=0.5, rely=0.35, anchor=tk.CENTER) #Setting x and y position for button object

#Creating new button object for selection
b4 = tk.Button(master, text='Orbit Eccentricity Calculation', highlightbackground='light blue', command=eccentricityWindow)
b4.place(relx=0.5, rely=0.45, anchor=tk.CENTER) #Setting x and y position for button object

#Creating new button object for selection
b5 = tk.Button(master, text='Orbital Period Calculation', highlightbackground='light blue', command=periodWindow)
b5.place(relx=0.5, rely=0.55, anchor=tk.CENTER) #Setting x and y position for button object

#Creating new button object for selection
b6 = tk.Button(master, text='Atmospheric Density Calculation', highlightbackground='light blue', command=densityWindow)
b6.place(relx=0.5, rely=0.65, anchor=tk.CENTER) #Setting x and y position for button object

#Creating new button object for selection
b7 = tk.Button(master, text='Tutorial Videos', highlightbackground='light blue', command=tutorialsWindow)
b7.place(relx=0.5, rely=0.75, anchor=tk.CENTER) #Setting x and y position for button object

#Creating new button object for selection
b8 = tk.Button(master, text='History', highlightbackground='light blue', command=openHistory)
b8.place(relx=0.5, rely=0.85, anchor=tk.CENTER) #Setting x and y position for button object

#Creating new button object for selection
exitButton = tk.Button(master, text = "Exit", highlightbackground='light blue', command = master.destroy) 
exitButton.place(relx=0.5, rely=0.95, anchor=tk.CENTER) #Setting x and y position for button object

master.mainloop() #Loop for window, acts as a runtime
