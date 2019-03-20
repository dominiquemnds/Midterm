import re
import sys
#Starting by opening the files-works!

file=open('ALevel.java',mode='r')
Acode=file.read()

#Verifying/getting rid of class statement
braces=re.findall(r'class\s+[A-Za-z]+({)\s*[\w\s(\[\]\)\{\}\/=\.;"?+<>,*]+(\})(\s+class\s+[A-Za-z]+({)\s*[\w\s(\[\]\)\{\}\/=\.;"?+<>,*]+(\}))*', Acode)

if not braces:
    print("Your class braces are formatted incorrectly")
        
classverif=re.compile(r'class\s+[A-Za-z]+{\n')#matches class xxx{\n, not closing bracket
classcheck=re.compile(r'class\s+[\w]*{')

if not classverif.search(Acode) and classcheck.search(Acode):
    print("You have an error regarding your class declaration")
    sys.exit();
 

if classverif.search(Acode):
    noclass=classverif.sub("",Acode)
    
else:
   print("You have an error regarding your class declaration")
   sys.exit();

#Getting rid of comments
comments=re.compile(r'(\/\*\s+[a-zA-Z\s\-\,\.]*\*\/)')
onelinecomment= re.compile(r'(\/{2}[\w\s\!]*$)', re.MULTILINE)

if comments.search(noclass):#multiline comments
    withoutcomments=comments.sub(" ", noclass, count=2)#python strings are immutable so I have to make a new string


if onelinecomment.search(withoutcomments):#single line comments
    nocomments=onelinecomment.sub("",withoutcomments, count=2)


#Getting rid of spaces
nospace=re.compile(r'(\s{2,})')

if nospace.search(nocomments):
    oneline=nospace.sub("",nocomments)



#Verifying/getting rid of imports
importstate=re.compile(r'import\s+java\.(io.\*|util.Scanner|text.\*|awt.\*|util.regex.\*);', re.MULTILINE)
importcheck=re.compile(r'import\s+[\w.*]*;?')

if not importstate.search(oneline) and importcheck.search(oneline):
    print("You have an error regarding your import statement")
    print(importcheck.findall(oneline))
    sys.exit()

if importstate.search(oneline):
    noimport=importstate.sub("",oneline)
    
#print(noimport)


#Verifying/getting rid of public static fix to grab last bracket
publicstatic=re.compile(r'public\s+static\s+void\s+main\s+(\(String\s+\[\]\s+arg(s|ss)\)\{)')
check0= re.compile(r'public\s*sta(\w+)\s*\w*\s*\w*\s*[\(\w\s\[\]\)]*\{*')

if not publicstatic.search(noimport) and check0.search(noimport):
    print("You have an error regarding your public static statement")
    sys.exit()

if publicstatic.search(noimport):
    nopublic=publicstatic.sub("",noimport)
    

#print (nopublic) #->feel free to check the progress by uncommenting
    
#Verifying/getting rid of String declarations
string=re.compile(r'(public\s+|private\s+)*String\s+([A-Za-z]*)(\s*\=\s*(\"([A-Za-z\s+])*\"|sc\.next\(\)))*;')
check1= re.compile(r'(public\s+|private\s+)*St\w+\s*\w+[\w=\s".()]*;?')

if not string.search(nopublic) and check1.search(nopublic):
    print("You have an error regarding on of your Strings")
    sys.exit()

    
if string.search(nopublic):
    nostrings=string.sub("",nopublic)


#print(nostrings)

#Verifying/getting rid of all variable declarations
intregex=re.compile(r'(public\s+|private\s+)*int\s+[\w]*(;|\s*\=[\s.\w\(\)]*;)')#is able to detect int age; || int age = 56;
intcheck= re.compile(r'(public\s+|private\s+)*(?<![rlo\s])i\w+\s+\w+(?![p,])\s*(;|\=?\s*\w+.\w+\(?\)?;|\=\s+\d;)*')

booleanregex=re.compile(r'(public\s+|private\s+)*boolean\s+\w+\s*(;|=\s?(false|true);)')
booleancheck=re.compile(r'(public\s+|private\s+)*bo\w+\s+\w([=\s\w])*;?')


if intcheck.search(nostrings) and not intregex.search(nostrings):
    print("You have an error regarding one of your int declaration statements")
    sys.exit()
else:
    noints=intregex.sub("",nostrings)


if not booleanregex.search(noints) and booleancheck.search(noints):
    print("You have an error regarding one of your boolean declaration statements")
    sys.exit()

if booleanregex.search(noints):
    nobool=booleanregex.sub("", noints)
    
#print(nobool)

#Verifying/getting rid of any System.out.prints
outregex=re.compile(r'System.out.print(ln)?\((\"[\w\s?<+>=.]+\"(\s*\+\s*\w+)*(\s*\+\s*\"\s*[\w\s]+\")?)?(\s*\+\s*\w+)?(\w\+\w)?(\s*\+\s*\"\s*[\w\s?<+>=.]+\")?\);')
check2= re.compile(r'Sy\w+\.\w+\.?\w+\(?\"?[\w\s?.<>=+]+\"?\s*\+*\s*[\w\s]*\+*\s*\"*[\w\s?.<>=+]*\"*\s*\+*\s*[\w\s]*\+*\s*\"*[\w\s?.<>=+]*\"*\)?;?')

if check2.search(nobool) and not outregex.search(nobool) :
    print("You have an error regarding one of your System output statements")
    sys.exit()
    
if outregex.search(nobool):
    noout=outregex.sub("", nobool)

#print (noout)    

#Verifying/getting rid of assignment statements
scan=re.compile(r'Scanner\s+(\w)+\s*\=\s*new\s+Scanner\(System\.in\);')
scancheck=re.compile(r'Sc\w+\s+\w+\s*[=\s\w]+\(?\w*\.?\w*\)?;?')
assign=re.compile(r'\w+\s*=\s*[\w\s\+\-\/\*\%\.\(\)]*;')

if not scan.search(noout) and scancheck.search(noout):
    print("There is an error regarding one of your Scanner declarations")
    sys.exit()
    
if scan.search(noout):
    noscan=scan.sub("", noout)
    
if assign.search(noscan):
    noassign=assign.sub("", noscan)


#print(noassign)
    
#Verifying/getting rid of while statements
whileregex= re.compile(r'while(\([A-Za-z]+\s*[<=>!]+\s*[0-9A-Za-z]+\)){([A-Za-z.()"\s+-\/?;]*)}')
check3=re.compile(r'wh\w+\s*\(?[\w\s<=>\/]+\)?{?[A-Za-z.()"\s+-\/?;]?}?')

if not whileregex.search(noassign) and check3.search(noassign):
    print("There is an error regarding one of your while loop declarations")
    sys.exit()

if whileregex.search(noassign):
    nowhile=whileregex.sub("", noassign)
    
#print(nowhile)

#Verifying/getting rid of if/else statements
ifregex= re.compile(r'if(\s*\([A-Za-z0-9\s<>=!-+)]*){([A-Za-z.()"<>+-+!0-9;=]*)}(else if{[A-Za-z.()"<>+-+!0-9;=]*})*(else{[A-Za-z.()"<>+-+!0-9;=]*})*')
check4= re.compile(r'if\s*\(?\s*[\w+=><\/\s]+\)?\{[\w\s<>=!-+)]*\}?\s*(else if\s*\(?\s*[\w+=><\/]+\)?\{[\w\s<>=!-+)]*\})*(else\s*\{?[\w\s<>=!-+)]*\}?)*')

if not ifregex.search(nowhile) and check4.search(nowhile):
    print("There is an error regarding one of your if(else) statements")
    sys.exit()

if ifregex.search(nowhile):
    noif=ifregex.sub("", nowhile)

#print(noif)

#Verifying/getting rid of object declaration statements
objectify=re.compile(r'Person\s+\w+\s*\=\s*new\s+Person\(\w+,\s+\w+\);')
objectcheck=re.compile(r'P\w+\s*\w+\s*\=?\s*[\w\s(),]+;')

if not objectify.search(noif) and objectcheck.search(noif):
    print("There is an error regarding one of your object declaration statements")
    sys.exit()

if objectify.search(noif):
    noobject=objectify.sub("",noif)

#print(noobject)

#Verifying/getting rid of person info
method=re.compile(r'you\.printInfo\(\);')
methodcheck=re.compile(r'\w+\.\w+\(?\)?;?')

if not method.search(noobject) and methodcheck.search(noobject):
    print("There is an error regarding one of your method calling statements")
    sys.exit()
    
if method.search(noobject):
    nomethod=method.sub("",noobject)

#print(nomethod)
    
#Verifying/getting rid of object class declaration statements
obclass=re.compile(r'(public|private)\s+\w+\((int|String|double)\s+\w(,\s+(int|String|double)\s+\w)*(,\s+(int|String|double)\s+\w)*\){}')
obcheck=re.compile(r'(public|private)*\s*\w*\s*\(?[\w\s,]+\)?{}')

if not obclass.search(nomethod) and obcheck.search(nomethod):
    print("There is an error regarding one of your object class declaration statements")
    sys.exit()
    
if obclass.search(nomethod):
    noob=obclass.sub("",nomethod)


#print(noob)

#Verifying/getting rid of object method declaration statements
opening=re.compile(r'(public|private)\s+(static\s+)*void\s+\w+\([\w,\s]*\){')
opencheck=re.compile(r'(public|private)*\s*\w+\s*\w+\s*\w*\(?[\w\D\s]*\)?{')

if not opening.search(noob) and opencheck.search(noob):
    print("There is an error regarding one of your method declaration statements")
    sys.exit()
    
if opening.search(noob):
    noopen=opening.sub("",noob)

#print(noopen)
    
#Final check
final=re.compile(r'\w')

if final.search(noopen):
    print("There's an error in your code the compiler missed")
    sys.exit()

file.close()

print("Your code was compiled with no errors")
