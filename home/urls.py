
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index,name='home'),
    path('collections/',views.collections,name="collections"),
    path('collections/<str:slug>',views.collectionsview,name="collectionsview"),
    path('login/',views.logpage,name="login"),
    path('reg/',views.register,name="register"),
    path('collections/<str:cate_slug>/<str:prod_slug>',views.productview,name="productview"),
    path('logout/',views.logout,name="logout"),
    path('test/',views.test,name="test"),
    path('contact/',views.contact,name="contact"),



]
