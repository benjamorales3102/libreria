from django.contrib import admin
from .models import editorial, libro

# Register your models here.
@admin.register(editorial)
class EditorialAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'telefono', 'correo')
    search_fields = ('nombre', 'direccion', 'telefono', 'correo')

@admin.register(libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'editorial', 'fecha_publicacion', 'isbn', 'precio_formateado')
    search_fields = ('titulo', 'autor', 'editorial__nombre', 'isbn')
    list_filter = ('editorial', 'fecha_publicacion')
    