
import os

from django.core.wsgi import get_wsgi_application

env = os.environ.get('PYSTAGRAM_ENV', '')
if env:
	if not env.endswith('_settings'):
		env = '{}_settings'.format(env)
else:
	env = 'settings'

os.environ.setdefault(
	"DJANGO_SETTINGS_MODULE", "pystagram.{}".format(env)
)

application = get_wsgi_application()
