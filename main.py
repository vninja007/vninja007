import os
import datetime
import random
print("started!")
past="I'm afraid for the calendar. Its days are numbered." #Joke #1
jokes = []
with open("jokes.txt") as rfile:
    jokes = rfile.readlines()

jokes = [i.replace("\n","") for i in jokes]

canReset = True
print("initialized!")
while True:
    now = datetime.datetime.now()
    
    if(now.hour==0 and canReset):
        print(now.hour)

        print("is making dadjoke")
        joke = past[:]
        while(joke[:]==past[:]):
            joke = random.choice(jokes)
        canReset = False
        with open("README.md") as rfile:
            with open("rm2.md","a+") as wfile:
                for line in rfile:
                    if(len(line) > 3 and "Dad joke of the day" in line):
                        wfile.write("Dad joke of the day: "+joke)
                        wfile.write("\n")
                    else:
                        wfile.write(line)
        #risky
        os.remove("README.md")
        os.rename("rm2.md","README.md")
        os.system("git add .")
        os.system('git commit -m "DJOTD '+str(now.year)+"-"+str(now.month)+"-"+str(now.day)+'"')
        os.system('git push')
    elif(now.hour==1 and not canReset):
        canReset = True
    
        


