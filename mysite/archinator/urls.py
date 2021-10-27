from django.urls import path
from . import views

app_name='archinator'

urlpatterns = [
    path('', views.index, name='index'), ##부위 고르게 하기
    path('<int:part_id>/', views.detail, name='detail'),
    path('<int:part_id>/<int:symptom_id>/', views.diagnose, name='diagnose'),
    path('<int:part_id>/<int:symptom_id>/<int:question_num>/', views.question, name='question')
]

