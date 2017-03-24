from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tracker.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$','trackerapp.views.home', name = 'home'),
    url(r'^register/$','trackerapp.views.register', name = 'register'),
    url(r'^login/$','trackerapp.views.login', name = 'login'),
    url(r'^logout$','trackerapp.views.logout', name = 'logout'),
    url(r'^change_password/$','trackerapp.views.change_password', name = 'change_password'),
    url(r'^resetpassword/passwordsent$','django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'^resetpassword/$','django.contrib.auth.views.password_reset', name="reset_password"),
    url(r'^password_reset_confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$','django.contrib.auth.views.password_reset_confirm', name="password_reset_confirm"),
    url(r'^reset/done/$','django.contrib.auth.views.password_reset_complete', name="password_reset_complete"),
    url(r'^contact/$','trackerapp.views.contact', name = 'contact'),
    url(r'^profile/$','trackerapp.views.profile', name = 'profile'),
    url(r'^activation/$','trackerapp.views.activation', name = 'activation'),
    url(r'^individual_activation/$','trackerapp.views.individual_activation', name = 'individual_activation'),
    url(r'^admin/', include(admin.site.urls)),
)
