
from tkinter import *
from PIL import Image,ImageTk
from timeit import default_timer as timer
import random  

#Creating an instance of Tk() class
root = Tk()

#Setting the dimensions for the created window
root.geometry(newGeometry="500x350")
root.minsize(400,200)

#flag variable for checking the user is playing first time or Replaying it
alpha=0




# To start the speed test
def speedTest():
    global alpha
    global name
   
    # Will print name of user for only first time
    if alpha==0:
       print(name.get())

# To display results in console
    def result():
    
      
        if x3.get()==samples[sample]:  # will check the user entered and displayed text is same
           end=timer()  # Record the time of end
           res = len(samples[sample].split()) # Store number of words from the sample sentence
           ans=(end-start)/res # Calculate result
           x6=round(ans,2)
           acc="you took {} sec/word"
           bcc=acc.format(x6)
           x6 =Label(game,text=bcc,font="Times 15") 
           x6.place(x=180,y=250)
           
        else:  # if enetred text does not match with sample text
           print("Sentence does not match")

# reading the samples in the text.txt file and converting its lines into lists of samples.
    fo = open("text.txt", "r")
    samples = list(fo.readlines());
    for i in range(len(samples)):
        str=samples[i]
        s1=str[:len(str)-1]
        samples[i]=s1
    #print(samples)
    
    sample=random.randint(0,(len(samples)-1)) #Selecting random sample from samples
    #sample=samples #Selecting random sample from samples
    start=timer() # Recording the time of starts
    
    if alpha==0 : # If user is not replaying 
        root.destroy() # Will destroy the root window
        alpha=1 # Update the alpha flag
    
    game = Tk() # Create a new Instance for typing the displayed sentence
    game.geometry(newGeometry="500x350") #Setting the dimensions for the created window
    
    image=Image.open('background.jpg') # Setting the background image for it
    pic=ImageTk.PhotoImage(image)
    label=Label(image=pic) # creating label for image
    label.pack() # Packing the image label

    # creating label for sample text and placing it
    x1 = Label(game,text=samples[sample],font="Times 20") 
    x1.place(x=10,y=5)


    # creating label for text and placing it
    x2 = Label(game,text="Type the sentence here",font="Times 15")
    x2.place(x=120,y=100)

    # creating label for Input box and placing it
    x3=Entry(game,text="Type here",width=70)
    x3.place(x=20,y=150)

    # creating label for Submit button and placing it
    x4 = Button(game,text="Submit",command=result,width=14,bg='gray')
    x4.place(x=120,y=200)



    # creating label for Replay button and placing it
    x5 = Button(game,text="Replay",command=speedTest,width=14,bg='gray')
    x5.place(x=240,y=200)
    game.mainloop() # Closed the game instance here

   

# Setting image for backgroung of root instance
image=Image.open('background.jpg')
pic=ImageTk.PhotoImage(image)
label=Label(image=pic)
label.pack()

# Setting Title for root instance
head = Label(root,text="Typing Speed Test",font="Times 20")
head.place(x=130,y=5)

# Placing Button for start in root window
b1 = Button(root,text="Start",command=speedTest,width=14,bg='gray')
b1.place(x=170,y=130)

# Getting name of user from root window
hname = Label(root,text="Enter your Name: ",font="Times 12")
hname.place(x=10,y=70)
name=Entry(root,text="Enter your name",width=70)
name.place(x=10,y=90)

root.mainloop() # Closed the root instance here