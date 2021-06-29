from django.urls import path 
from django.views.generic import RedirectView
from . import views 


urlpatterns = [
    path('home/', views.Home, name='home'),
    path('about/', views.AboutUs,name='about'),
    path('signin/', views.SignIn, name='signin'),
    path('signup/', views.Signup, name='signup'),
    path('artical/', views.Article, name='artical'),
    path('academi/', views.Academi, name='academi'),
    path('logout/', views.log_out, name='logout'),
    path('profile/<int:pk>', views.Profile, name='profile'),
    path('editprofile/<int:pk>',views.ProfileUpdateView.as_view()),
    path('editPost/<int:pk>', views.EditPostView.as_view(success_url='/collageapp/artical/')),
    path('delete/<int:pk>', views.delete),   
    path('classRoutine/', views.ClassRoutine,name='classRoutine'),
    path('creatpost/', views.PostCreate.as_view()),
    path('notice/', views.Notice,name='notice'),
    path('study/', views.study,name='study'),
    path('syllebus/<int:pk>', views.sullybus,name='syllebus'),
    path('notes/<int:pk>', views.notes,name='notes'),
    path('question/<int:pk>', views.question,name='question'),
    path("",RedirectView.as_view(url = 'home/'))
]
