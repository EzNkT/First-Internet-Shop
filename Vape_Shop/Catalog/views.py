from django.shortcuts import render

from .forms import OfferForm


def catalog(request):
    template = "catalog/catalog.html"
    context = {}
    return render(request, template, context)


def make_offer(request):
    template = "catalog/offer_form.html"
    form = OfferForm(request.POST or None)
    context = {'form': form}
    if form.is_valid():
        form.save()
    return render(request, template, context)
