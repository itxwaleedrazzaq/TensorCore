from django.urls import path
from . import views

app_name = 'portfolio'
urlpatterns = [
    path('',views.CategoryListView.as_view(),name='list_view'),
    path('contact/',views.ContactUsView.as_view(),name='contact'),
    path('<slug:pk>/',views.CategoryDetailView.as_view(),name='detail_view'),
    path('<slug:pk>/create/',views.CreateProjectView.as_view(),name='create_project'),
    path('<slug:pk>/update/',views.UpdateProjectView.as_view(),name='update_project'),
    path('<slug:pk>/delete/',views.DeleteProjectView.as_view(),name='delete_project'),

    #AIviews
 
]