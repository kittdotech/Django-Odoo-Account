from django.conf.urls import include, url
from django.contrib import admin
import oerp_account.urls as oerpurls
urlpatterns = [
    # Examples:
    # url(r'^$', 'Test.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(oerpurls)),
]
