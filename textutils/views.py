from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def output(request):
    inputText = request.POST.get('text', 'default')
    # Check checkbox values
    special = request.POST.get('special', 'off')
    upper = request.POST.get('upper', 'off')
    newline = request.POST.get('newline', 'off')
    space = request.POST.get('space', 'off')


    #Check which checkbox is on
    if special == "on":
        specialChar = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in inputText:
            if char not in specialChar:
                analyzed = analyzed + char

        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        inputText = analyzed

    if(upper=="on"):
        analyzed = ""
        for char in inputText:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        inputText = analyzed

    if(space=="on"):
        analyzed = ""
        for index, char in enumerate(inputText):
            if not(inputText[index] == " " and inputText[index+1]==" "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed Extra Space', 'analyzed_text': analyzed}
        inputText = analyzed

    if (newline == "on"):
        analyzed = ""
        for char in inputText:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char
            else:
                print("no")
        print("pre", analyzed)
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}

    if(special != "on" and newline!="on" and space!="on" and upper!="on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'output.html', params)

