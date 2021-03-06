# Generated by Django 3.0.3 on 2020-05-27 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=50)),
                ('website', models.URLField()),
                ('chief_officer', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Minerals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mineral_name', models.CharField(max_length=25)),
                ('symbol', models.CharField(default='DEFAULT VALUE', max_length=3)),
                ('atomic_num', models.PositiveIntegerField(default=1)),
                ('appearance', models.CharField(default='DEFAULT VALUE', max_length=25)),
                ('description', models.TextField(default='DEFAULT VALUE')),
            ],
        ),
        migrations.CreateModel(
            name='Minesite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=25)),
                ('region', models.CharField(max_length=25)),
                ('production', models.PositiveIntegerField(default=0)),
                ('minerals', models.ManyToManyField(to='beamish2_app.Minerals')),
                ('owners', models.ManyToManyField(to='beamish2_app.Company')),
            ],
        ),
        migrations.AddField(
            model_name='company',
            name='mineral_profile',
            field=models.ManyToManyField(to='beamish2_app.Minerals'),
        ),
    ]
