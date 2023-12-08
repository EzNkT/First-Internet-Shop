from django.shortcuts import render


def rules(request):
    template = "pages/rules.html"
    context = {}
    return render(request, template, context)


def help(request):
    template = "pages/help.html"
    context = {}
    return render(request, template, context)


def adress(request):
    template = "pages/adress.html"
    context = {}
    return render(request, template, context)
