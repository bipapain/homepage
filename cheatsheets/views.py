from django.shortcuts import render, get_object_or_404

from .models import Cheatsheet


def all_cheatsheets(request):
    cheatsheets = Cheatsheet.objects.all()
    return render(request, 'cheatsheets/all_cheatsheets.html', {'cheatsheets': cheatsheets})


def detail(request, cheatsheet_id):
    cheatsheet = get_object_or_404(Cheatsheet, pk=cheatsheet_id)
    return render(request, 'cheatsheets/detail.html', {'cheatsheet': cheatsheet})

