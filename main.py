### Assignment: Regex and Files
##Name: Tyler Kennedy
##Date: 

#don't forget to import regex
import re

##(/5) Task 1: MODIFY the code below.
#A# Change the regex from .* to what is required to capture an email address
#B# Add a condition so that no blanks are printed.
#C# Count the number of email addresses found and print a final output line.

def reEmail(fname):
  
  fhand = open(fname,'r')
  for line in fhand:
    extr = re.findall('\S*@\S*',line)
    if len(extr): 
      print(extr)
        

  print()

#reEmail('rural-staff.txt')
    

'''### Task 1 Results for 
>reEmail('rural-staff.txt')
['demcisaac@edu.pe.ca']
...
['pewynne@edu.pe.ca']
There were 89 email addresses in rural-staff.txt 
### '''

##(/5) Task 2: MODIFY code that will open the athletics file and extract all award winners
#notice that in the rural-athletics.txt file, the pattern is "... - AWARD WINNER(S)"
#You should use a ( and ) regex like " (extract this) " to extract a portion of the match

def reAward(fname):
  fhand = open(fname, 'r')
  for line in fhand:
    extr = re.findall('-.*', line)
    if len(extr):
      print(extr)

#reAward('rural-athletics.txt')

'''### Task 2 Results for
>reAward('rural-athletics.txt')
['Devon Lawlor']
...
['Jose Crisostomo, Kalon MacDonald-Wood'] 
###'''

##(/5) Task 3: CREATE code that will open a file and extract all the phone numbers 

def rePhone(fname):
  fhand = open(fname, 'r')
  for line in fhand:
    extr = re.findall('\d\d\d\S\d\d\d\S\d\d\d\d', line)
    if len(extr):
      print(extr)

rePhone('rural-staff.txt')







  
