from django.contrib import admin
from .models.user import User
from .models.vuelo import Vuelo
# from .models.vuelos import Vuelos

# Register your models here.

admin.site.register(User)
admin.site.register(Vuelo)
