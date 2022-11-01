from django.contrib import admin

# Register your models here.
from .models import Artiste
admin.site.register(Artiste)

from .models import Song
admin.site.register(Song)

from .models import Lyric
admin.site.register(Lyric)