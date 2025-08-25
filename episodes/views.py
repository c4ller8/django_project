from django.shortcuts import render


def episodes(request):
    return render(request, "episodes/episodes.html")
