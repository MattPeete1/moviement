# Generated by Django 4.2.5 on 2023-10-05 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_take'),
    ]

    operations = [
        migrations.AddField(
            model_name='take',
            name='movie',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main_app.movie'),
            preserve_default=False,
        ),
    ]
