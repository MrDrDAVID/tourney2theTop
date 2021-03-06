# Generated by Django 4.0.5 on 2022-06-15 23:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_title', models.CharField(max_length=50)),
                ('date_posted', models.DateField(auto_now_add=True)),
                ('description_rules', models.TextField()),
                ('game_image', models.ImageField(upload_to='')),
                ('max_participants', models.IntegerField(choices=[(16, 'Small'), (32, 'Medium'), (64, 'Large'), (128, 'X Large')])),
                ('winner', models.CharField(max_length=30)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date_posted'],
            },
        ),
        migrations.CreateModel(
            name='Participants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.tournament')),
            ],
        ),
        migrations.CreateModel(
            name='Matches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_num', models.IntegerField()),
                ('winner', models.CharField(max_length=30)),
                ('loser', models.CharField(max_length=30)),
                ('competitor_one', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_query_name='competitor_one', to=settings.AUTH_USER_MODEL)),
                ('competitor_two', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='competitor_two', to=settings.AUTH_USER_MODEL)),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.tournament')),
            ],
        ),
    ]
