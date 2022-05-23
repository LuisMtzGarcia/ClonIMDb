# Generated by Django 4.0.4 on 2022-05-23 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appIMDb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'generos',
            },
        ),
        migrations.AddField(
            model_name='pelicula',
            name='genero',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='appIMDb.genero'),
            preserve_default=False,
        ),
    ]
