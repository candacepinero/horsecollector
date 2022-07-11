from django.contrib import admin
from .models import Horse
from .models import Feeding
from .models import Toy
# Register your models here.
admin.site.register(Horse)
admin.site.register(Feeding)
admin.site.register(Toy)