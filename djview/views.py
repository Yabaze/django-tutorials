from django.http import HttpResponse ,  HttpResponseRedirect

# def home(request):#class
    #print(request )
    #print(request.method)
    #print(request.get_full_path)
    #print(request.is_ajax())
    #print(request.method)
    #return HttpResponse("Hello World")

def home(request):
    request = HttpResponse()
    request.content = 'Main Content '
    request.write("Hi Baby How Are You ? <br>")
    request.write("Hi Baby How Are You ? <br>")
    request.write("Hi Baby How Are You ? <br>")
    request.write("Hi Baby How Are You ? <br>")
    request.write("Hi Baby How Are You ? <br>")
    print(request.status_code)
    print(dir(request))
    request.status_code = 200
    return request

def redirect_somewhere(request):
    return HttpResponseRedirect("/login")

def login(request):
    return HttpResponse("login please")    