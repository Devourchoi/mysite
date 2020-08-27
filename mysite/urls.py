
from django.contrib import admin
from django.urls import path,include

urlpatterns = [

    path('admin/', admin.site.urls),
    path('polls/', include('elections.urls')), #localhost:8000 으로 접속하면(''이 기본 주소이므로(?)) elections.url로 전달하도록 함
]
