from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.decorators.cache import cache_page
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    # path('post/city/', cache_page(20)(PostCity.as_view()), name='city'),
    path('post/', PostAll.as_view(), name='allpost'),
    path('post/<slug:post_slug>/', show_post, name='showpost'),
    path('category/<slug:cat_slug>/', PostCategory.as_view(), name='showcat'),
    path('addpost/', addpost, name='addpost'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('search/', SearchView.as_view(), name='search')

]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

