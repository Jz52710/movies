# Generated by Django 2.2.7 on 2019-11-29 06:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MovieBackgrounds', '0003_auto_20191129_1434'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='moviecollection',
            options={'verbose_name': '电影收藏', 'verbose_name_plural': '电影收藏'},
        ),
        migrations.AlterField(
            model_name='moviecollection',
            name='mid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MovieBackgrounds.MovieInformation', verbose_name='电影ID'),
        ),
        migrations.AlterField(
            model_name='moviecollection',
            name='uid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户ID'),
        ),
    ]
