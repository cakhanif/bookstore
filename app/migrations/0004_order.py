# Generated by Django 2.1.7 on 2019-02-20 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20190220_0413'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_name', models.CharField(max_length=30)),
                ('date_order', models.DateTimeField(auto_now_add=True)),
                ('user_order', models.ManyToManyField(to='app.User')),
            ],
        ),
    ]
