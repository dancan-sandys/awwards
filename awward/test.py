word='Racecar'
sortetword = ''.join(sorted(word))
print(sortetword)

def isAlphabetic(string):
    sortedstring = ''.join(sorted(string))
    if sortedstring == string:
        results = True
    
    else:
        results = False
    
    return results




Given a sting
When  
    T
then
The string is in alpahbetical order return a True, if not return False
Pseudo code
1) create a function 
2) create a variable to store a copy of the string in alphabetical order
3) compare the sorted string and the given string using an if statement and return true if they are and false if they are not