# Generated by Django 3.1.6 on 2022-04-27 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rides', '0003_remove_person_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='date',
        ),
        migrations.RemoveField(
            model_name='person',
            name='destination_city',
        ),
        migrations.RemoveField(
            model_name='person',
            name='destination_state',
        ),
        migrations.RemoveField(
            model_name='person',
            name='email',
        ),
        migrations.RemoveField(
            model_name='person',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='person',
            name='origination_city',
        ),
        migrations.RemoveField(
            model_name='person',
            name='origination_state',
        ),
        migrations.RemoveField(
            model_name='person',
            name='premium',
        ),
        migrations.RemoveField(
            model_name='person',
            name='seats_available',
        ),
        migrations.RemoveField(
            model_name='person',
            name='taking_passengers',
        ),
        migrations.RemoveField(
            model_name='person',
            name='vehicle_type',
        ),
        migrations.AddField(
            model_name='person',
            name='Xacceleration',
            field=models.DecimalField(decimal_places=64, default=0, max_digits=64),
        ),
        migrations.AddField(
            model_name='person',
            name='Xgyroscope',
            field=models.DecimalField(decimal_places=64, default=0, max_digits=64),
        ),
        migrations.AddField(
            model_name='person',
            name='Yacceleration',
            field=models.DecimalField(decimal_places=64, default=0, max_digits=64),
        ),
        migrations.AddField(
            model_name='person',
            name='Ygyroscope',
            field=models.DecimalField(decimal_places=64, default=0, max_digits=64),
        ),
        migrations.AddField(
            model_name='person',
            name='Zacceleration',
            field=models.DecimalField(decimal_places=64, default=0, max_digits=64),
        ),
        migrations.AddField(
            model_name='person',
            name='Zgyroscope',
            field=models.DecimalField(decimal_places=64, default=0, max_digits=64),
        ),
    ]
