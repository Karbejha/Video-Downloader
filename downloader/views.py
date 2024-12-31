from django.shortcuts import render
from django.http import JsonResponse
import yt_dlp
import os

def index(request):
    status = ""
    if request.method == "POST":
        url = request.POST.get("url")
        folder = request.POST.get("folder")
        if url and folder:
            try:
                ydl_opts = {
                    'outtmpl': os.path.join(folder, '%(title)s.%(ext)s'),
                }
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
                status = "Download Completed!"
            except Exception as e:
                status = f"Error: {e}"
        else:
            status = "Please provide both video URL and folder path."

    return render(request, "downloader/index.html", {"status": status})
