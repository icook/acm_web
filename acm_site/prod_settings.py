from acm_web import settings
# Modify the base settings for production
#######
# Used in various places to know the context root
URL_BASE = 'http://people.eecs.ku.edu/~acm/'
DEBUG = False

# URL to access our dynamic media from.
MEDIA_URL = URL_BASE + '/dynamic/'
# Absolute filesystem path to the directory that will hold user-uploaded files.
MEDIA_ROOT = '/home/isaac/public_html/dynamic/'

# Location of our static collection area. 
# Should be at public_html root for simplicity
STATIC_ROOT = '/home/isaac/public_html/static/'
