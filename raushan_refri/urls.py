from django.contrib import admin
from django.urls import path
from website import views
from rest_framework.views import APIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register',views.register),
    path('signin',views.signin),
    path('signout',views.signout),
    path('head',views.head),
    path('show',views.show),
    # path('show/<user_id>',views.show),
    path('edit/<id>',views.edit),
    path('update/<id>',views.update),
    path('delete/<id>',views.delete),
    # path('logout',views.logout),
    path('customer',views.customer_data.as_view()),
    path('customerapi/<pk>/',views.customer_detail_data.as_view()),
]