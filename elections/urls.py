from django.urls import path
from . import views    # .은 현재 폴더라는 뜻


urlpatterns = [

    path('a/', views.index), #localhost:8000으로 요청이 들어오면 view.index로 연결이 되도록 함
]
