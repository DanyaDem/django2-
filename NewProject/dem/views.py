from django.http import HttpResponse, HttpResponseNotFound

def index(request):
    host = request.META['HTTP_HOST']
    user_agent =  request.META["HTTP_USER_AGENT"]
    path = request.path
    return HttpResponse(f"""
    <p>Host: {host}</p>
    <p>Path: {path}</p>
    <p>User-agent: {user_agent}</p>
    """)

def error(request):
    return HttpResponseNotFound('Page not found')
    
def user(request, login='sdfsdfsg',folder='sdfsdkjh',numpost='1'):
    return HttpResponse(f"{login}, {folder}, {numpost}")
    
