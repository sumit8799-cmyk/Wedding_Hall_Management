
from django.urls import path
from . import views


urlpatterns = [
    
    path('', views.dashbord, name='dashbord'),

    # ------___------____------____----_____HOME PAGE ------____----_____-----____---_______------____--

    path('homepage/', views.homepage, name='homepage'),
    path('homepagelist/', views.homepagelist, name='homepagelist'),
    path('homepageUpdate/<int:homepage_id>/', views.homepageUpdate, name='homepageUpdate'),
    path('homepageDelete/<int:homepage_id>/', views.homepageDelete, name='homepageDelete'),

     # ------___------____------____----_____ABOUT PAGE ------____----_____-----____---_______------____--

    path('aboutpage/', views.aboutpage, name='aboutpage'),
    path('aboutpagelist/', views.aboutpagelist, name='aboutpagelist'),
    path('aboutpageUpdate/<int:about_id>/', views.aboutpageUpdate, name='aboutpageUpdate'),
    path('aboutpageDelete/<int:about_id>/', views.aboutpageDelete, name='aboutpageDelete'),

     # ------___------____------____----_____GALLERY PAGE ------____----_____-----____---_______------____--

    path('gallerypage/', views.gallerypage, name='gallerypage'),
    path('gallerypagelist/', views.gallerypagelist, name='gallerypagelist'),
    path('gallerypageUpdate/<int:gallery_id>/', views.gallerypageUpdate, name='gallerypageUpdate'),
    path('gallerypageDelete/<int:gallery_id>/', views.gallerypageDelete, name='gallerypageDelete'),

     # ------___------____------____----_____CONTACT PAGE ------____----_____-----____---_______------____--

    path('contactpage/', views.contactpage, name='contactpage'),
    path('contactpagelist/', views.contactpagelist, name='contactpagelist'),
    path('contactpageUpdate/', views.contactpageUpdate, name='contactpageUpdate'),

     # ------___------____------____----_____STATIC PAGE ------____----_____-----____---_______------____--
    path('staticadd/', views.staticadd, name='staticadd'),
    path('staticlist/', views.staticlist, name='staticlist'),
    path('staticUpdate/<int:counter_id>/', views.staticUpdate, name='staticUpdate'),
    path('staticDelete/<int:counter_id>/', views.staticDelete, name='staticDelete'),

     # ------___------____------____----_____REGISTERED USERS PAGE ------____----_____-----____---_______------____--

    path('registereduserlist/', views.registereduserlist, name='registereduserlist'),
    path('approve-user/<int:user_id>/', views.approve_user, name='approve_user'),
    path('reject-user/<int:user_id>/', views.reject_user, name='reject_user'),
    path('rejecteduserlist/', views.rejecteduserlist, name='rejecteduserlist'),
    path('regecteduserlist/', views.rejecteduserlist, name='regecteduserlist'),
    path('approveduserlist/', views.approveduserlist, name='approveduserlist'),

     # ------___------____------____----_____LOGIN PAGE ------____----_____-----____---_______------____--

    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

      # ------___------____------____----_____PROFILE PAGE ------____----_____-----____---_______------____--

    path('profile/', views.profile, name='profile'),

     # ------___------____------____----_____CHANGE PASSWORD PAGE ------____----_____-----____---_______------____--

    path('changepassword/', views.changepassword, name='changepassword'),
]