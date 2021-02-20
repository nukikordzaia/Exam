# Generated by Django 3.1.7 on 2021-02-20 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='ticket name')),
                ('start_date', models.DateTimeField(verbose_name='start time')),
                ('end_date', models.DateTimeField(verbose_name='start time')),
                ('code', models.CharField(max_length=10, verbose_name='code')),
            ],
            options={
                'verbose_name': 'Ticket',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='price')),
                ('start_date', models.DateTimeField(verbose_name='start order')),
                ('end_date', models.DateTimeField(verbose_name='start order')),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='order', to='ecommerce.ticket')),
            ],
            options={
                'verbose_name': 'Order',
            },
        ),
    ]
