# Generated by Django 3.2.4 on 2021-07-01 08:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Productdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=30)),
                ('pdesc', models.CharField(max_length=200)),
                ('pprice', models.FloatField()),
                ('pdiscount', models.FloatField()),
                ('pimg', models.ImageField(upload_to='product/%y/%m/%d')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.productitem')),
            ],
        ),
    ]