from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(City)
admin.site.register(Street)
admin.site.register(Community)
admin.site.register(Residence)
admin.site.register(Grocery)
admin.site.register(Googleuser)
admin.site.register(Review)
admin.site.register(Transportation)
admin.site.register(Stop)