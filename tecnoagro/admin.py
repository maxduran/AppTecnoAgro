'''from django.contrib import admin
from .models import Consulta
# Register your models here.
admin.site.register(Consulta)'''

from django.contrib import admin
from .models import Consulta, Usuario
# Register your models here.


#admin.site.Register(Consulta)
admin.site.register(Consulta)
admin.site.register(Usuario)