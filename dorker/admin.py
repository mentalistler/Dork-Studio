from django.contrib import admin
from .models import *

admin.site.register(country_codes)
admin.site.register(wordlist)
admin.site.register(wordlistmain)
admin.site.register(dorktype)
admin.site.register(dorkcontents)

