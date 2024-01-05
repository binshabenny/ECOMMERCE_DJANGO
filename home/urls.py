
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
    path('detail_view/<str:prod_slug>/', views.detail_view, name='detail_view'),
    path('add_to_cart/<int:product_id>/',views.add_to_cart,name="add_to_cart"),
    path('view_cart/', views.view_cart, name='view_cart'),
    path('cart/', views.cart, name='cart'),
    path("add/<int:product_id>/", views.add_to_cart, name="add_to_cart"),
    path("cart/cart_detail/", views.cart_detail, name="cart_detail"),
    path("remove_from_cart/<int:product_id>", views.remove_from_cart, name="remove_from_cart"),
 

]
