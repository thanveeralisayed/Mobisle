from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm,MyPasswordChangeForm,MypasswordResetForm,MysetPasswordForm


urlpatterns = [
    path('', views.ProductView.as_view(),name='home'),
    path('product-detail/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),

    
    path('cart/',views.show_cart,name='showcart'),
    path('remove/',views.removefromcart,name='removecart'),
    
    path('pluscart/',views.plus_cart),
    path('minuscart/',views.minus_cart),
    path('cup/',views.cartupdate),


    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.ProfileView.as_view(), name='profile'),



    path('address/', views.AddressView, name='address'),
    path('address/<slug:data>', views.AddressView, name='adelete'),
    path('saddress/<slug:data>', views.SetAddressDefault, name='adefault'),


    path('orders/', views.orders, name='orders'),


    path('aphones/',views.aphones,name ='aphones'),
    path('aphones/<slug:data>', views.aphones, name='aphonesdata'),

    path('search/',views.SearchItem,name='search'),

    


    path('iphones/',views.iphones,name ='iphones'),
    path('iphones/<slug:data>', views.iphones, name='iphonesdata'),

    path('qphones/',views.qphones,name ='qphones'),
    path('qphones/<slug:data>', views.qphones, name='qphonesdata'),

    path('kphones/',views.kphones,name ='kphones'),
    path('kphones/<slug:data>', views.kphones, name='kphonesdata'),


    path('accounts/login/',auth_views.LoginView.as_view(template_name='app/reglogin.html',
    authentication_form=LoginForm), name='login'),

    path('logout/',auth_views.LogoutView.as_view(next_page='login'),name='logout'),
    path('passwordchange/',auth_views.PasswordChangeView.as_view(template_name='app/chpass.html',form_class=MyPasswordChangeForm),name = 'passwordchange'),
    path('passwordchangedone/',auth_views.PasswordChangeDoneView.as_view(template_name='app/chpass.html'),name='password_change_done'),


    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='app/password_reset.html',form_class=MypasswordResetForm),name='password-reset'),

    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='app/password_reset.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html',form_class=MysetPasswordForm),name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='app/password_reset_confirm.html'),name='password_reset_complete'),
     


    path('registration/', views.CustomerRegistrationView.as_view(), name='registration'),


    path('checkout/', views.checkout, name='checkout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
