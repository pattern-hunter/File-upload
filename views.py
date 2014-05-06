from django.shortcuts import render

def upload (request):
    return render (request, "upload.html")
    
def uploaded (request):
    file = request.FILES['filename']
    dest = open ("/foo/bar/file_name.jpeg", "w") # The path is the one where you want the file to be stored on the server.
    for bit in file.read ():
        dest.write (bit)
    return HttpResponse ("Uploaded")
