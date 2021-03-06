# Generated by Django 4.0.1 on 2022-01-19 22:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crochet', '0007_gauge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gauge',
            name='hook',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='gauges', to='crochet.hook'),
        ),
        migrations.AlterField(
            model_name='gauge',
            name='stitch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='gauges', to='crochet.stitch'),
        ),
        migrations.CreateModel(
            name='Pattern',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('instructions', models.TextField()),
                ('notes', models.TextField()),
                ('pattern_image', models.ImageField(upload_to='patterns')),
                ('gauge', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='patterns', to='crochet.gauge')),
                ('hook', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='patterns', to='crochet.hook')),
                ('stitches', models.ManyToManyField(related_name='patterns', to='crochet.Stitch')),
                ('yarn', models.ManyToManyField(related_name='patterns', to='crochet.Yarn')),
            ],
        ),
    ]
