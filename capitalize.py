string=('this is a string')
string=string.capitalize()
print(string)

def capitalize(s):
    words=s.split()
    capitalized=(word.capitalize() for word in words)
    return" ".join(capitalized)

string1=('this! will be capitalized. i am a boy')
print(capitalize(string1))