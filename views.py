from django.shortcuts import render

def upload (request):
    return render (request, "upload.html")
    
def uploaded (request):
    file = request.FILES['img']
    dest = open ("/foo/bar/image_name.jpeg", "w")
    for bit in file.read ():
        dest.write (bit)
    return HttpResponse ("Uploaded")
