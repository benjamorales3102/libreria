from django.db import migrations, models


def move_prices_to_libros(apps, schema_editor):
    Libro = apps.get_model('libreria', 'libro')
    Precio = apps.get_model('libreria', 'precio')
    processed_libros = set()

    prices = Precio.objects.order_by('libro_id', '-fecha_actualizacion', '-pk')
    for price in prices.iterator():
        if price.libro_id in processed_libros:
            continue

        Libro.objects.filter(pk=price.libro_id).update(
            precio=price.precio,
            fecha_actualizacion=price.fecha_actualizacion,
        )
        processed_libros.add(price.libro_id)


def restore_prices_from_libros(apps, schema_editor):
    Libro = apps.get_model('libreria', 'libro')
    Precio = apps.get_model('libreria', 'precio')

    for libro in Libro.objects.exclude(precio__isnull=True).iterator():
        precio = Precio.objects.create(libro_id=libro.pk, precio=libro.precio)
        if libro.fecha_actualizacion is not None:
            Precio.objects.filter(pk=precio.pk).update(
                fecha_actualizacion=libro.fecha_actualizacion,
            )


class Migration(migrations.Migration):
    dependencies = [
        ('libreria', '0002_alter_editorial_id_alter_libro_id_alter_precio_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='precio',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='libro',
            name='fecha_actualizacion',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='editorial',
            name='telefono',
            field=models.CharField(max_length=20),
        ),
        migrations.AddField(
            model_name='editorial',
            name='correo',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.RunPython(move_prices_to_libros, restore_prices_from_libros),
        migrations.DeleteModel(
            name='precio',
        ),
    ]
