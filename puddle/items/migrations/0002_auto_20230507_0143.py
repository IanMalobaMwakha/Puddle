# Generated by Django 2.1.5 on 2023-05-06 22:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.FloatField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='item_images')),
                ('is_sold', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='cartegory',
            options={'ordering': ('name',), 'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='item',
            name='cartegory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='items.Cartegory'),
        ),
        migrations.AddField(
            model_name='item',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to=settings.AUTH_USER_MODEL),
        ),
    ]