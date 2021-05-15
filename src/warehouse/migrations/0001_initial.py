# Generated by Django 3.2 on 2021-05-15 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0002_auto_20210417_1909'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('product_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
    ]
