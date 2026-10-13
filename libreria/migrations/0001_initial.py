from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='editorial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='libro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('autor', models.CharField(max_length=100)),
                ('fecha_publicacion', models.DateField()),
                ('isbn', models.CharField(max_length=13)),
                ('editorial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libreria.editorial')),
            ],
        ),
        migrations.CreateModel(
            name='precio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.DecimalField(decimal_places=0, max_digits=10)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
                ('libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libreria.libro')),
            ],
        ),
    ]
