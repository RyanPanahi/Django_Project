# Generated by Django 3.2 on 2023-01-10 07:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='file',
            options={'verbose_name': 'file', 'verbose_name_plural': 'files'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'product', 'verbose_name_plural': 'products'},
        ),
        migrations.AlterField(
            model_name='category',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='categorise/', verbose_name='avatar'),
        ),
        migrations.AlterField(
            model_name='category',
            name='updated_time',
            field=models.DateTimeField(auto_now=True, verbose_name='updated_time'),
        ),
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(upload_to='file/%Y/%m/%d', verbose_name='file'),
        ),
        migrations.AlterField(
            model_name='file',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='product'),
        ),
        migrations.AlterField(
            model_name='file',
            name='updated_time',
            field=models.DateTimeField(auto_now=True, verbose_name='updated_time'),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated_time',
            field=models.DateTimeField(auto_now=True, verbose_name='updated_time'),
        ),
        migrations.AlterModelTable(
            name='file',
            table='files',
        ),
        migrations.AlterModelTable(
            name='product',
            table='products',
        ),
    ]
