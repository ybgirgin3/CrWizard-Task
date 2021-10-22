from django.shortcuts import render

# Create your views here.
def home(request):    
    import urllib3
    import xmltodict
    import traceback
    
    url = "https://www.w3schools.com/xml/plant_catalog.xml"
    http = urllib3.PoolManager()
    response = http.request("GET", url)
    try:
        data = xmltodict.parse(response.data)
        print(data)
    except: 
        data = "Hata"
    return render(request, "root/home.html", {'data': data})
    

# def parsing(request):
#     import urllib3
#     import xmltodict
#     import traceback
    
#     url = "https://www.w3schools.com/xml/plant_catalog.xml"
#     http = urllib3.PoolManager()
#     response = http.request("GET", url)
#     data = xmltodict.parse(response.data)
#     return render(request, "root/home.html", {'data': data})
    
    



from django.contrib.auth import logout



def logout_view(request):
    logout(request)
    