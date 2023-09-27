from django.http import HttpResponse
def home_page(request):
    print("Home page")
    return HttpResponse("<p>You can use /api/v1/companies <br> or /api/v1/employees <br> for showing api's </p>")

 