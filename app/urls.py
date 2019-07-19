from django.urls import path
from .import views
urlpatterns = [
    # path('',views.home,name='home'),
    path('', views.homepageview.as_view(),name='home'),
    # path('details/<task_id>/',views.details,name='details'),
    path('details/<int:pk>/',views.detailpageview.as_view(),name='details'),
    # path('delete/<task_id>/',views.delete,name='delete'),
    # path('delete/<int:pk>',views.deletepageview.as_view(),name='delete'),
    path('search/',views.search,name='search'),
    path('contacts/create/',views.CreateBaseView.as_view(),name='create'),
    path('details/update/<int:pk>/',views.UpdateBaseView.as_view(),name='update'),
    path('details/delete/<int:pk>/',views.ContactDeleteView.as_view(),name='delete'),
    path('signup/',views.SignupForm.as_view(),name='signup'),
]