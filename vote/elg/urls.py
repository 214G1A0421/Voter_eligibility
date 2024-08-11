from django.urls import path
from elg import views
urlpatterns=[
    path('man/<int:age>',views.func1)
]