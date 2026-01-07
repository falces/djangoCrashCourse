from django.urls import path
from . import views

urlpatterns = [
    path('hello', views.hello_world_view, name='hello_world'),
    path('', views.hello_python_view, name='hello_python'),
    path('html', views.hello_html_view, name='hello_html'),
    path('name/<str:name>', views.hello_name, name='hello_name'),
    path('add/<int:number1>/<int:number2>', views.hello_add, name='hello_add'),
    path('search', views.hello_search, name='hello_search'),
    path('redirectToHTML', views.redirect_to_html, name='redirect_to_html'),
    path('postexample', views.post_example, name='post_example'),
    path('basicform', views.basic_form, name='basic_form'),
    path('djangoform', views.django_form, name='django_form'),
    path('templateview', views.template_view, name='template_view'),
    path('todos', views.todos_view, name='todos_view'),
]
