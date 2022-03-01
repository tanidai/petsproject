from django.urls import path
from . import views
from .views import signupview, loginview, Listview, gobackview,CreateClass,ArticleDetailsview,IndexView,photobuildingview,deletelistview,choiceview,choice1view,deleteview
app_name = 'petsgallery'

urlpatterns = [
    path('',IndexView, name='index'),
    path('login/', loginview ,name='login'),
    path('signup/', signupview,name='signup'),
    path('List/',Listview ,name='List'),
    path('Logouthtml/', views.Logouthtmlview.as_view(),name='Logouthtml'),  
    path('goback/',gobackview,name='goback'),
    path('myself/', views.myselfview.as_view(),name='myself'),
    path('photobuilding/',photobuildingview,name='photobuilding'),
    path('ArticleProduction/',CreateClass.as_view(),name='ArticleProduction'),
    path('ArticleDetails/<int:pk>/', ArticleDetailsview,name='ArticleDetails'),
    path('ArticleArticleDeletion/', views.ArticleDeletionview.as_view(),name='ArticleDeletion'),
    path('deletelist/',deletelistview,name='deletelist'),
    path('delete/<int:pk>',deleteview,name='delete'),
    path('choice/',choiceview,name='choice'),
    path('choice1/',choice1view,name='choice1')

]