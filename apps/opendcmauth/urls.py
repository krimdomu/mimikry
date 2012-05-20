from django.conf.urls.defaults import *

urlpatterns = patterns('django.contrib.auth.views',
    url(r'^login/$', 'login', {'template_name': 'opendcmauth/login.html'},
        name='opendcmauth_login'),
    url(r'^logout/$', 'logout', {'next_page': '/'},
        name='opendcmauth_logout'),
    url(r'^password_change/$', 'password_change',
        {'template_name': 'opendcmauth/password_change_form.html'},
        name='opendcmauth_password_change'),
    url(r'^passwort_changed/$', 'password_change_done',
        {'template_name': 'opendcmauth/password_change_done.html'},
        name='opendcmauth_password_change_done')
)