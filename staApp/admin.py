from django.contrib import admin
from .models.user import User
from .models.vuelo import Vuelo

# Register your models here.

admin.site.register(User)
admin.site.register(Vuelo)
