# Generated by Django 2.0.13 on 2019-06-12 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aulas', '0002_auto_20190612_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aula',
            name='curso',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='curso', to='aulas.Curso'),
        ),
    ]