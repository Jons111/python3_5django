# Generated by Django 4.2 on 2024-01-22 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0002_alter_portfolio_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=200)),
                ('subject', models.CharField(max_length=50)),
                ('text', models.TextField()),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]