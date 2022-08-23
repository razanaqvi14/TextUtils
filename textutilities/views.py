from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,"index.html")

def analyze(request):
    djtext=request.POST.get("text","default")
    removepunc=request.POST.get("removepunc","off")
    capitalize=request.POST.get("capitalize","off")
    newlineremove=request.POST.get("newlineremove","off")
    extraspaceremove=request.POST.get("extraspaceremove","off")
    charcount=request.POST.get("charcount","off")
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    if removepunc=="on" and capitalize=="on" and charcount=="on" and extraspaceremove=="on":
        analyzed=""
        for index,char in enumerate(djtext):
            if char not in punctuations and not(djtext[index]==" " and djtext[index+1]==" "):
                analyzed+=char.upper()
        count=0
        for i in range(len(analyzed)):
            count+=1
        params={
            "purpose":'''your text has been transformed into upper case and after removing punctuations and extra spaces the number of characters in your text including spaces is/are''',
            "analyzed_text":analyzed,
            "count":count
        }
        return render(request,"analyze.html",params)

    elif removepunc=="on" and capitalize=="on" and charcount=="on":
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed+=char.upper()
        count=0
        for i in range(len(analyzed)):
            count+=1
        params={
            "purpose":'''your text has been transformed into upper case and after removing punctuations the number of characters in your text including spaces is/are''',
            "analyzed_text":analyzed,
            "count":count
        }
        return render(request,"analyze.html",params)

    elif removepunc=="on" and extraspaceremove=="on" and capitalize=="on":
        analyzed=""
        for index,char in enumerate(djtext):
            if char not in punctuations and not(djtext[index]==" " and djtext[index+1]==" "):
                analyzed+=char.upper()
        params={
            "purpose":'''The punctuations and extra spaces from your text have been removed and your text has been transformed into uppercase''',
            "analyzed_text":analyzed
        }      
        return render(request,"analyze.html",params)

    elif removepunc=="on" and capitalize=="on":
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed+=char.upper()
        params={
            "purpose":'''The punctuations have been removed and your text has been transformed into uppercase''',
            "analyzed_text":analyzed
        }
        return render(request,"analyze.html",params)    

    elif removepunc=="on" and charcount=="on":
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed+=char
        count=0
        for i in range(len(analyzed)):
            count+=1
        params={
            "purpose":'''The punctuations have been removed and after removing punctuations the number of characters in your text including spaces is/are''',
            "analyzed_text":analyzed,
            "count":count
        }
        return render(request,"analyze.html",params)    

    elif removepunc=="on" and extraspaceremove=="on":
        analyzed=""
        for index,char in enumerate(djtext):
            if char not in punctuations and not(djtext[index]==" " and djtext[index+1]==" "):
                analyzed+=char
        params={
            "purpose":'''The punctuations and extra spaces from your text have been removed''',
            "analyzed_text":analyzed
        }      
        return render(request,"analyze.html",params)

    elif capitalize=="on" and charcount=="on":
        analyzed=""
        count=0
        analyzed=""
        for i in range(len(djtext)):
            count+=1
        for characters in djtext:
            analyzed+=characters.upper()
        params={
            "purpose":'''Your text is transformed into upper case and the total number of characters in your text is/are''',
            "count":count,
            "analyzed_text":analyzed,
        }      
        return render(request,"analyze.html",params)

    elif removepunc=="on":
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed+=char
        params={
            "purpose":'''The punctuations have been removed''',
            "analyzed_text":analyzed
        }
        return render(request,"analyze.html",params)

    elif capitalize=="on":
        analyzed=djtext.upper()
        params={
            "purpose":'''Your text has been transformed to uppercase''',
            "analyzed_text":analyzed
        }
        return render(request,"analyze.html",params)

    elif newlineremove=="on":
        analyzed=""
        for char in djtext:
            if char!="\n" and char!="\r":
                analyzed+=char
        params={
            "purpose":'''New line has been removed''',
            "analyzed_text":analyzed
        }
        return render(request,"analyze.html",params)

    elif extraspaceremove=="on":
        analyzed=""
        for index,char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analyzed+=char
        params={
            "purpose":'''All the spaces have been removed''',
            "analyzed_text":analyzed
        }
        return render(request,"analyze.html",params)

    elif charcount=="on":
        count=0
        for char in range(len(djtext)):
            count+=1
        params={
            "purpose":'''The number of characters in your text including spaces is/are''',
            "count":count,
            "analyzed_text":"You just only checked the box which count the characters in your text so there is no text to display"
        }
        return render(request,"analyze.html",params)
        
    else:
        params={"purpose":"No actions have been taken because you did not check any of the boxes on the previous page",
        "analyzed_text":djtext,
        }
        return render(request, "analyze.html",params)
def contact(request):
    return render(request, "contact.html")
def about(request):
    return render(request, "about.html")