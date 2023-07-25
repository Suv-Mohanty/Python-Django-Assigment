from django.urls import path,include
from techpro import views

urlpatterns = [
    path('state/',views.StateView.as_view()),
    path('state/<int:pk>/',views.StateViewID.as_view()),
    path('state/<int:state_id>/city/',views.CityListView.as_view()),
    path('city/',views.CityView.as_view()),
    path('city/<int:pk>/',views.CityViewID.as_view()),
    path('city/<int:city_id>/branch/',views.BranchListView.as_view()),
    path('branch/',views.BranchView.as_view()),
    path('branch/<int:pk>/',views.BranchViewID.as_view())
]