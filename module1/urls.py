from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
   # path('admin/', admin.site.urls),
    path('hello/',hello1,name='hello'),
    path('',newhomepage, name='newhomepage'),
    path('travelpacakge123/',travelpacakge, name='travelpacakge123'),
    path('print_to_console/',print_to_console, name='print_to_console'),
    path('p/',print1,name="print1"),
    path('randomcall/',randomcall,name='randomcall'),
    path('randomlogic',randomlogic,name='randomlogic'),
    path('getdate1/',getdate1,name='getdate1'),
    path('get_date',get_date, name = 'get_date'),
path('myregister/',myregister,name='myregister'),
    path('registerloginfunction',registerloginfunction, name = 'registerloginfunction'),
    path('pie_chart/',pie_chart,name = 'pie_chart'),
    path('card123/',card123,name='card123'),
path('weatherlogic', weatherlogic, name='weatherlogic'),
    path('weather/',weather,name='weather'),
path('feedback/',feedback,name='feedback'),
    path('feedbackform',feedbackform,name='feedbackform'),
    path('login/',login,name='login'),
    path('login1',login1,name='login1'),
    path('signup/',signup,name='signup'),
    path('signup1',signup1,name='signup1'),
    path('logout',logout,name='logout'),
]