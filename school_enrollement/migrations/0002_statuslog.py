# Generated by Django 4.2.13 on 2024-05-17 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school_enrollement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatusLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('from_status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='from_status', to='school_enrollement.funnelstatus')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_enrollement.student')),
                ('to_status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='to_status', to='school_enrollement.funnelstatus')),
            ],
        ),
    ]
