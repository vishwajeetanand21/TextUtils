#we have created this file- Vishwajeet

#we have to import this header file everytim
from django.http import HttpResponse
from django.shortcuts import render #this hedder file we have to include always when we are using templates like html, css and js file

#the code below is for Home page and for about page
#def index(request):#by default this home page function takes request as a argument
#    return HttpResponse('''<h1>Hello World, This is the Home Page</h1> <a href="https://youtu.be/AepgWsROO4k">Visit code with harry django playlist</a>''')
#def about(request):
#    return HttpResponse("This is the about page")


def index(request):
    #myDict={'name':'Anand','place':'Ranchi'}
    return render(request,'index.html')#render takes the first argument as 'request' and second argument as templates file 'index.html' and the third argument is a dictionary
    #return HttpResponse("Home page ")



def analyze(request):
    djtext=request.POST.get('text','default')#getting the 'text' from the html page ans storing it in a variable
    print(djtext)#this will be printed in our comand prompt

    #check the value of checkbox
    removepunctuation=request.POST.get('removepunctuation','off')#we have set the default value of our checkbox as off for removing punctuations
    fullcaps=request.POST.get('capitalized','off')#to get the string in which we have to change it into UPPER CASE
    LineRemover=request.POST.get('newLineRemover','off')#if it is on we have to remove the new line function
    spaceRemover=request.POST.get('spaceRemover','off')
    charCount=request.POST.get('charCount','off')

    #check which checkbox is on
    if removepunctuation == "on":#if the removepunctuation checkbox is on then remove all the punctuations in the string
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""#creating a empty string
        for char in djtext:#loop to traverse the punctuations string
            if char not in punctuations:
                analyzed = analyzed + char
        parameters={'purpose':'Remove Punctuations','analyzed_text':analyzed} #creating a dictionary, which we will send as parameter to our analyze.html page
        djtext=analyzed
        #return render(request,'analyze.html',parameters)#rendering request to analyze.html page with a dictionary which is parameters



    if(fullcaps=="on"):#if the UPPER CASE checkbox is one then we will convert the whole string into upper case
        analyzed=""#same as before creating an empty string in which we will store the result
        for char in djtext:#loop to traverse the input string provided by the user
            analyzed=analyzed+char.upper()#storing the upper case letter
        parameters={'purpose':'change to UPPER CASE','analyzed_text':analyzed}#creating a dictionary, which we will send as parameter to our analyze.html page
        djtext=analyzed
        #return render(request,'analyze.html',parameters)#rendering request to analyze.html page with a dictionary which is parameters



    if(LineRemover=="on"):
        analyzed=""
        for char in djtext:
            if char=='\n' and char =='\r':
                continue
            else:
                analyzed=analyzed+char
        parameters={'purpose':'New Line Remover','analyzed_text':analyzed}
        djtext=analyzed
        #return render(request,'analyze.html',parameters)



    if(spaceRemover=="on"):
        analyzed=""
        for char in djtext:
            if char==' ':
                continue
            else:
                analyzed=analyzed+char
        parameters={'purpose':'Space Remover','analyzed_text':analyzed}
        djtext=analyzed
        #return render(request,'analyze.html',parameters)



    if removepunctuation != 'on' and fullcaps != 'on' and LineRemover != 'on' :
    #if the checkbox is off then don't do anything simply return an 'Error' message
        return HttpResponse("Error")
        #return render(request, 'analyze.html', parameters)

    return render(request, 'analyze.html', parameters)
