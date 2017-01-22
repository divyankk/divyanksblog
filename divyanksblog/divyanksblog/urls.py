from django.conf.urls import url
from django.contrib import admin
import posts.views
import sitepages.views
from django.conf.urls.static import static
from django.conf import settings
# above two imports are to load the image on home page

# Here posts is the name of the app and views is the name of the file 'views.py'
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', posts.views.home, name='home'),  # home is the name of the function defined in views.py file
    url(r'^posts/(?P<post_id>[0-9]+)/$', posts.views.post_details, name='post_detail'),
    url(r'^aboutus/', sitepages.views.aboutus, name='aboutus'),
    # post_id can be any other name
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# The statement "+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) " is used to set the URL for image fetching
