# IPND Stage 2 Final Project

# these are the sentences minus answers displayed to the user
lvlEasySentence = '''A grown up puppy is called a ___1___.  A grown up kitten is called a ___2___. A grown up fawn is called a ___3___. A grown up guppy is called a ___4___.'''
lvlMediumSentence = '''The boat that couldnt sink but did was called the ___1___.  The ring around the center of the earth is called the ___2___.  The country directly above North America is called ___3___. The largest state in North America is ___4___.'''
lvlHardSentence = '''The average person ___1___ thirteen times a day? The Average American opens a ___2___ times a day? In Texas it's illegal to swear in front of a ___3___. What is Johnny Depp afraid of ___4___.'''

# these are the answer slot and answers
lvlEasyQA = {"___1___" : "dog", "___2___" : "cat", 
"___3___": "deer", "___4___" : "fish"}

lvlMediumQA = {"___1___" : "titanic", "___2___" : "equator", 
"___3___": "canada", "___4___" : "alaska"}

lvlHardQA = {"___1___" : "laughs", "___2___" : "fridge", 
"___3___": "corpse", "___4___" : "clowns"}    

# this fucntion accepts the int question and str answer, it returns a boolean 1 if success, 0 if failed
def checkAnswer(question,answer):	  
    if lvlQA.get("___" + str(question) + "___") == answer:        
        varAnswered = 1    
    else:    
        varAnswered = 0    
    return varAnswered

varLevel = raw_input("Which level would you like to try? Choose easy, medium or hard.")
print("you chose " + varLevel)

#checks input and assigned global variables
if varLevel == "easy":
    lvlQA = lvlEasyQA
    lvlSentence = lvlEasySentence
elif varLevel == "medium":
    lvlQA = lvlMediumQA
    lvlSentence = lvlMediumSentence
elif varLevel == "hard":
    lvlQA = lvlHardQA
    lvlSentence = lvlHardSentence
else:
    lvlQA = "error"  

if lvlQA == "error":
	print "You chose an incorrect level, please restart"
else:    
    #start the game    
    for x in range(1, len(lvlQA)+1):
        print "The paragraph reads: \n" + lvlSentence
        while True:
            varAnswer = raw_input("what should be substituted for ___" + str(x) + "___?")            
            if checkAnswer(x,varAnswer) == 1:
                lvlSentence = lvlSentence.replace("___" + str(x) + "___", varAnswer)
                break
            else:                
                print "please try again \n" 
    print "The paragraph reads: \n" + lvlSentence
    print "Thanks for Playing!"          


