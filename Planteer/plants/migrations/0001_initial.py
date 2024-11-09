# Generated by Django 5.1.3 on 2024-11-06 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('alpha_code', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1024)),
                ('about', models.TextField()),
                ('used_for', models.TextField()),
                ('image', models.ImageField(default='images/default.JPG', upload_to='images/')),
                ('category', models.CharField(choices=[('flower', 'Flower'), ('tree', 'Tree'), ('herb', 'Herb'), ('shrubs', 'Shrubs'), ('aquatic', 'Aquatic Plant'), ('fungus', 'Fungus'), ('shadow', 'Shadow Plant'), ('fruit', 'Fruit'), ('vegetable', 'Vegetable')], max_length=10)),
                ('is_edible', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('native_to', models.ManyToManyField(to='plants.country')),
            ],
        ),
    ]