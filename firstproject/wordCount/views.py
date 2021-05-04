from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def result(request):
    sentence = request.GET["sentence"]
    wordlist = sentence.split()
    worddict = {}

    for word in wordlist:
        if word in worddict:
            worddict[word] += 1
        else:
            worddict[word] = 1

    return render(request, "result.html", {"fulltext": sentence, "count": len(wordlist), "worddict": worddict.items})