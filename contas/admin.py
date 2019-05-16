from django.contrib import admin
from .models import Usuario
from .models import Curriculo

# Registro de modelos
admin.site.register(Usuario)
admin.site.register(Curriculo)