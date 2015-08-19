from django.conf.urls import patterns, url

urlpatterns = patterns('api.views',
	url(r'^hello$', 'hello_world_view'),
	# url(r'^kirk/(?P<input_phrase>[\w]+)$', 'kirk_view'),
	# url(r'^spock/(?P<input_phrase>[\w]+)$', 'spock_view'),
	url(r'^(?P<input_character>[\w]+)/(?P<input_phrase>[\w]+)$', 'get_character_view'),
	url(r'^create$', 'create_character_view'),
)