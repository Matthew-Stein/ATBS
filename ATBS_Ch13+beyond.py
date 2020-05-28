# -*- coding: utf-8 -*-
"""
Created on Tue May 19 11:56:54 2020

@author: Matthew
"""
#skipped the end of the Excel section because all of the book text is outdated
#dont want to beat my head against that wall
#can learn an alternative Excel-file manipulation later. 
import os
os.getcwd()
os.chdir(r"C:\Users\Matthew\Documents\GitHub\BioInf")

import PyPDF2
pdfFileObj = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pdfReader.numPages

pageObj = pdfReader.getPage(0)
pageObj.extractText()

#decrypting pdf's
import PyPDF2
pdfReader = PyPDF2.PdfFileReader(open('encrypted.pdf', 'rb'))
#dfReader.isEncrypted
#pdfReader.getPage(0)
#inputting password into it. 
pdfReader.decrypt('rosebud')
pageObj = pdfReader.getPage(0)
#okay works now that those 2 lines are commented out. Idk man. 
### Creating PDF's 
#limited to creating new pdfs out of components of other pdfs.
#Cant make it from nothing like you can with text files
import PyPDF2
pdf1File = open('meetingminutes.pdf', 'rb')
pdf2File = open('meetingminutes2.pdf', 'rb')
pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
pdf2Reader = PyPDF2.PdfFileReader(pdf2File)
pdfWriter = PyPDF2.PdfFileWriter()
for pageNum in range(pdf1Reader.numPages):
    pageObj = pdf1Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)
    
for pageNum in range(pdf2Reader.numPages):
    pageObj = pdf2Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

pdfOutputFile = open('combinedminutes.pdf', 'wb')
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()
pdf1File.close()
pdf2File.close()
#copys all of the pages in pdf1File to the write program,
#then all the pages in the 2nd, then writes all to a new PDF
#rotating pdf pages:
import PyPDF2
minutesFile = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(minutesFile)
page = pdfReader.getPage(0)
page.rotateClockwise(90)

pdfWriter = PyPDF2.PdfFileWriter()
pdfWriter.addPage(page)
resultPdfFile = open('rotatedpage.pdf', 'wb')
pdfWriter.write(resultPdfFile)
resultPdfFile.close()
minutesFile.close()
#nice
#Overlaying pages: - useful for adding logos, timestamp, etc. 
import PyPDF2
minutesFile = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(minutesFile)
minutesFirstPage = pdfReader.getPage(0)
pdfWatermarkReader = PyPDF2.PdfFileReader(open('watermark.pdf', 'rb'))
minutesFirstPage.mergePage(pdfWatermarkReader.getPage(0))
pdfWriter = PyPDF2.PdfFileWriter()
pdfWriter.addPage(minutesFirstPage)

for pageNum in range(1, pdfReader.numPages):
    pageObj = pdfReader.getPage(pageNum)
    pdfWriter.addPage(pageObj)
resultPdfFile = open('watermarkedCover.pdf', 'wb')
pdfWriter.write(resultPdfFile)
minutesFile.close()
resultPdfFile.close()
#great

#now we can encrypt this:
import PyPDF2
pdfFile = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)
pdfWriter = PyPDF2.PdfFileWriter()
for pageNum in range(pdfReader.numPages):
    pdfWriter.addPage(pdfReader.getPage(pageNum))
pdfWriter.encrypt('swordfish')
resultPdf = open('encryptedminutes.pdf', 'wb')
pdfWriter.write(resultPdf)
resultPdf.close()
#nice. 
#end page 302. chapter ends at 316.
#Just going to do the pdf section because I have no interest in Docx stuff. 

### Combining select pages from many PDFs
#All pdfs in the CWD, sort them, grab all but the 1st page, write all to 1 file
import os
os.getcwd()

import PyPDF2, os
pdfFiles = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
pdfFiles.sort(key=str.lower)
pdfWriter = PyPDF2.PdfFileWriter()
for filename in pdfFiles: #Loop through each file
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    #loop through all pages except the 1st and add them
    for pageNum in range(1, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
#now save them
pdfOutput = open('allminutes.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()
#good

#End of PDF Section - Skipped Word doc section because not interested - can always return. 
#End Chapter 13
###############

#Chapter 14 - Working with .csv and JSON data. 
#csv "comma-separated values" - spreadsheets in raw text
#JSON info stored as JavaScript source code in plaintext files
    #used in many web applications

#csv's have their own escape characters so best to use CSV module. 
import csv
exampleFile =  open('example.csv')
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)
exampleData
#sweet
#access data with format: exampleData[row][col] : Ex:
exampleData[1][0]
exampleData[0][2]
exampleData[6][2]
#reading date from reader objects in a for loop (for large csv files)
import csv
exampleFile = open('example.csv')
exampleReader = csv.reader(exampleFile)
for row in exampleReader:
    print('Row #' + str(exampleReader.line_num)+ ' ' + str(row))
#now writing data to a csv file:
import csv
outputFile = open('output.csv', 'w', newline='')
#if you dont specify newline argument, will be double spaced 
outputWriter = csv.writer(outputFile)
outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham'])
outputWriter.writerow(['Hello, world!', 'eggs', 'bacon', 'ham'])
outputWriter.writerow([1, 2, 3.141592, 4])
outputFile.close()

#delimiter and lineterminator keyword arguments;
    #if you wanted cells separated with tab and row double spaced:
import csv
csvFile = open('example.tsv','w', newline='')
csvWriter = csv.writer(csvFile, delimiter = '\t', lineterminator='\n\n')
csvWriter.writerow(['apples', 'oranges', 'grapes'])
csvWriter.writerow(['eggs', 'bacon', 'ham'])
csvWriter.writerow(['spam','spam','spam','spam','spam','spam'])
csvFile.close()
#.tsv = tab separated values - basic text file
#yarp
###################
#Project: Removing the Reader from CSV files:
#(deleting the first row of multiple files)
import csv, os
os.makedirs('headerRemoved', exist_ok=True)
#loop through files in cwd
for csvFilename in os.listdir('.'): # this '.' shorthand must mean the cwd
    if not csvFilename.endswith('.csv'):
        continue #skip non-csv's
    print('Removing header from ' + csvFilename + '...')
    #now read in csv files, skipping first row. 
    csvRows = []  
    csvFileObj = open(csvFilename)
    readerObj = csv.reader(csvFileObj)
    for row in readerObj:
        if readerObj.line_num == 1: 
            continue #skip 1st row
        csvRows.append(row)    
    csvFileObj.close()    
    #added all non 1st rows to a list called csvRows[] now need to write out csv
    csvFileObj = open(os.path.join('headerRemoved', csvFilename), 'w',
                     newline = '')
    csvWriter = csv.writer(csvFileObj)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFileObj.close()
#bingo bango
###################### 

#most websites make their data available as JSON. 
    #websites over JSON content as a way to interact with programs;
    #this interaction is called an 'Application Programming Interface' or API

stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught" : 0,"felineIQ": null}'
#json strings always use double quotes
import json
jsonDataAsPythonValue = json.loads(stringOfJsonData)
jsonDataAsPythonValue
#loads = load string, dumps = dump string
pythonValue = {'isCat': True, 'miceCaught': 0, 'name': 'Zophie', 'felineIQ': None}
import json
stringOfJsonData = json.dumps(pythonValue)
stringOfJsonData
#converting back and forth^

#Project: fetching current weather data:
#! python3
# quickWeather.py - Prints the weather for a location from the command line.

import json, requests, sys
#compute location from command line arguments
if len(sys.argv) < 2:
    print('Usage: quickWeather.py location')
    sys.exit()
location = ''.join(sys.argv[1:])
#download Json data from openweathermap.orgs api
url ='http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3' % (location)
response = requests.get(url)
response.raise_for_status()
#load JSOn data and print weather:
weatherData = json.loads(response.text)
#print weather data
w = weatherData['list']
print('Current weather in %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])

#this doesnt work because i need an API key from the website.
#will just call it there - outdated book. 
#didnt need API key before 2015. 

#end chapter 14.
import os
os.getcwd()
os.chdir(r"C:\Users\Matthew\Documents\GitHub\BioInf")
### Keeping time, scheduling tasks, launching programs.
#Time module
import time
time.time()
#reports the time in seconds from the start of computing essentially -'Unix epoch'
#can be used at start and end of program to track how long it took to run. 
import time
def calcProd():
    #calculate the product of the first 100,000 numbers.
    product = 1
    for i in range(1,100000):
        product = product * i
    return product
startTime = time.time()
prod = calcProd()
endTime = time.time()
print('The result is %s digits long.' % (len(str(prod))))
print('Took %s seconds to calculate.' % (endTime - startTime))
#neat - now time.sleep()
import time
for i in range(3):
    print('Tick')
    time.sleep(1)
    print('Tock')
    time.sleep(1)
time.sleep(5)
#used to get program to pause for a period of time. 
#cant interrupt sleep calls, so dont do a huge sleep, break it into multiple little sleeps
#like this: - can use CTRL-C to interrupt
for i in range(30):  
    time.sleep(1)
#time values will often have a ton of digits after decimal. Useful to round them
import time
now = time.time()
now
round(now, 2)
round(now)
#Stopwatch Program; - time between 'enter' presses, with lap times. 
import time
#display instructions:
print('Press ENTER to begin. Afterwards press ENTER to "click" the stopwatch. Press Ctrl-C to quit.') 
input() #press enter to begin
print('Started')
startTime = time.time() #1st lap start time
lastTime = startTime
lapNum = 1 
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print('Lap #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
        lapNum += 1
        lastTime = time.time() # reset the last lap time. 
except KeyboardInterrupt:
    #handle the Ctrl-C exception to keep its error message from displaying. 
    print('\nDone.')        
#datetime module:
import datetime
import time
datetime.datetime.now()
dt = datetime.datetime(2020, 6, 1, 12, 12, 12, 12)
dt.year, dt.month, dt.day
dt.hour, dt.minute, dt.second
#to convert between a unix epoch time;
datetime.datetime.fromtimestamp(1000000)
datetime.datetime.fromtimestamp(time.time())
#times can have comparison operators called on them to find out which time is older
halloween2015 = datetime.datetime(2015, 10, 31, 0, 0, 0)
newyears2016 = datetime.datetime(2016, 1, 1, 0, 0, 0)
newyears2016 > halloween2015
#Timedelta data type:
delta = datetime.timedelta(days = 11, hours=10, minutes=9, seconds= 8)
delta.days, delta.seconds, delta.microseconds
delta.total_seconds()
str(delta)
#nice.  --- Now date arithmetic
dt = datetime.datetime.now()
dt
thousandDays = datetime.timedelta(days=1000)
dt + thousandDays


###########################
#MULTITHREADING: Running multiple processes simultaneously. Unlike all previous examples:
###########################
#Start page 347 - big idea. Done for now. 
import time, datetime
startTime = datetime.datetime(2029, 10, 31, 0, 0, 0)
while datetime.datetime.now() < startTime:
    time.sleep(1)
print('Program now starting on Halloween 2029')    
#this occupies single thread, program will just wait till that time.
#cant do anything else, unless you multithread:
#can put the delayed/scheduled code into a separate thread and continue to do \
#work in the main thread.
import threading, time
print('Start of program')
def takeANap():
    time.sleep(5)
    print('Wake up!')
    
threadObj = threading.Thread(target = takeANap) #passed function into separate thread
threadObj.start() #starts the separate thread
print('End of Program.')
#no () in the argument because we want to pass the function itself, not call it on a return value
#End of program prints first because the main thread finished before the 2nd thread
#python program will not end till all threads have been terminated
###
#passing arguments to the threads target function
import threading
threadObj = threading.Thread(target=print, args=['Cats','Dogs','Frogs'], kwargs={'sep':' & '})
#kwargs = key word arguments
threadObj.start()
#dont fall into the trap of having multiple threads reading and writing the 
#same global variables - very hard to debug
#skipped XKCD downloader

#Launching other programs from python w/ popen() - 'process open ()'
import subprocess
subprocess.Popen('C:\\Windows\\System32\\calc.exe')
#poll() - checks to see if the opened program is still running
#wait() - will pause code until opened program is closed. 
calcProc = subprocess.Popen('C:\\Windows\\System32\\calc.exe')
calcProc.poll() == None
calcProc.wait()
calcProc.poll()
#passing command line arguments to popen()
subprocess.Popen(['C:\\Windows\\notepad.exe', 'C:\\hello.txt'])
#taskscheduler, launchd, and cron
#taskscheduler for windows can learn more here if interested: http://nostarch.com/automatestuff/.
#can open websites with webbrowser.open() or other python scripts with popen() just like the text ex
fileObj = open('hello.txt', 'w')
fileObj.write('Hello world!')
#idk
#####
#project: countdown program
import time, subprocess

timeLeft = 10
while timeLeft > 0:
    print(timeLeft, end='')
    time.sleep(1)
    timeLeft = timeLeft - 1
subprocess.Popen(['start', 'alarm.wav'], shell = True)
#what an awful alarm noise jesus
#End Chapter 15 

#Will skip Chapter 16 beause no concievable interest in using this at the moment.
#Can always return. 

#Ditto for Chapter 17 Could only see myself using these if i ever have to mass-watermark images
# not at a stage in any of my hobbies where this would be relevant. 

#Chapter 18 - Contrilling Keyboard and Mouse with GUI automation
#can be tricky to exit if there is an issue. 
#ctrl-alt-delete can often exit
import pyautogui
pyautogui.PAUSE = 1 #will pause for 1 between pyautogui actions to allow for interrupting
#wont pause other python actions
pyautogui.FAILSAFE = True #this means rapidly moving mouse to upper left will crash program
#utilizes X,Y coordinates for mouse movement. 
import pyautogui
pyautogui.size()
width, height = pyautogui.size()
#moving the mouse
for i in range(10):
    pyautogui.moveTo(100,200, duration=0.25)
    pyautogui.moveTo(200,100, duration=0.25)
    pyautogui.moveTo(100,200, duration=0.25)
    pyautogui.moveTo(200,100, duration=0.25)
#moves to that absolute grid coordinate. move.Rel moves relative to current position
import pyautogui
pyautogui.FAILSAFE = True #yeet it works
for i in range(10):
    pyautogui.moveRel(100, 0, duration=0.25)
    pyautogui.moveRel(0, 100, duration=0.25)
    pyautogui.moveRel(-100, 0, duration=0.25)
#getting current position
pyautogui.position()
#Project: Where is the mouse right now??
import pyautogui, time
print('Press Ctrl-C to quite')
pyautogui.FAILSAFE = True
try:
    while True:
        #get mouse coords:
        x,y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        #can erase written text as long as not in newline.
        print(positionStr, end='')
        print('\r')
        time.sleep(1)
except KeyboardInterrupt:
    print('Done')
#doesnt auto-delete but is a nice implementation. Think due to spyder. 
#clicking
import pyautogui
pyautogui.click(10,5) #x=10, y=5, default is left click
#alt:
pyautogui.click(100, 150, button = 'left')
pyautogui.click(100, 150, button = 'right')
#alt
#pyautogui.mousedown to click mouse down (held) then .mouseup to release. 
#also .middleclick(), .rightclick(), .doubleClick()
#draw test
import pyautogui, time
time.sleep(5)
pyautogui.click()
distance = 200
while distance > 0:
    pyautogui.dragRel(distance, 0, duration=0.2) #move right
    distance = distance - 5
    pyautogui.dragRel(0, distance, duration=0.2) #down
    pyautogui.dragRel(-distance, 0, duration=0.2) #left
    distance = distance -5
    pyautogui.dragRel(0, -distance, duration=0.2) #up
#satisfying as fuck
#also
pyautogui.scroll()
#Keyboard stuff:
pyautogui.click(100,100) ;pyautogui.typewrite('Hello world!')
#dang thats fast
#inputing non-text characters:
pyautogui.typewrite(['a', 'b', 'left', 'right', 'ctrlleft', 'tab']) #etc. 
#form filling program if I am ever interested

# Thats the book gone through, WOO~!















