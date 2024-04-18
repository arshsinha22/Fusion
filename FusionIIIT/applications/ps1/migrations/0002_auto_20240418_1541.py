# Generated by Django 3.1.5 on 2024-04-18 15:41

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('globals', '0002_auto_20240418_1541'),
        ('ps1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomenclature', models.CharField(max_length=100, unique=True)),
                ('inUse', models.BooleanField(default=True)),
                ('location', models.CharField(choices=[('H1', 'Vashistha Hostel'), ('H4', 'Vivekananda Hostel'), ('H3', 'AryaBhatta Hostel'), ('SR1', 'Storage Room 1'), ('SR2', 'Storage Room 2'), ('SR3', 'Storage Room 3'), ('SR4', 'Storage Room 4'), ('SR5', 'Storage Room 5')], default='SR1', max_length=100)),
                ('isTransferred', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'StockItem',
            },
        ),
        migrations.RenameField(
            model_name='indentfile',
            old_name='indent_type',
            new_name='item_type',
        ),
        migrations.RemoveField(
            model_name='stockentry',
            name='item_name',
        ),
        migrations.AddField(
            model_name='indentfile',
            name='grade',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C')], default='A', max_length=1),
        ),
        migrations.AddField(
            model_name='stockentry',
            name='location',
            field=models.CharField(choices=[('H1', 'Vashistha Hostel'), ('H4', 'Vivekananda Hostel'), ('H3', 'AryaBhatta Hostel'), ('SR1', 'Storage Room 1'), ('SR2', 'Storage Room 2'), ('SR3', 'Storage Room 3'), ('SR4', 'Storage Room 4'), ('SR5', 'Storage Room 5')], default='SR1', max_length=100),
        ),
        migrations.CreateModel(
            name='StockTransfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('src_location', models.CharField(choices=[('H1', 'Vashistha Hostel'), ('H4', 'Vivekananda Hostel'), ('H3', 'AryaBhatta Hostel'), ('SR1', 'Storage Room 1'), ('SR2', 'Storage Room 2'), ('SR3', 'Storage Room 3'), ('SR4', 'Storage Room 4'), ('SR5', 'Storage Room 5')], default='SR1', max_length=100)),
                ('dest_location', models.CharField(choices=[('H1', 'Vashistha Hostel'), ('H4', 'Vivekananda Hostel'), ('H3', 'AryaBhatta Hostel'), ('SR1', 'Storage Room 1'), ('SR2', 'Storage Room 2'), ('SR3', 'Storage Room 3'), ('SR4', 'Storage Room 4'), ('SR5', 'Storage Room 5')], default='SR2', max_length=100)),
                ('dateTime', models.DateTimeField(default=django.utils.timezone.now)),
                ('dest_dept', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dept_dest_transfers', to='globals.departmentinfo')),
                ('indent_file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ps1.indentfile')),
                ('src_dept', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dept_src_transfers', to='globals.departmentinfo')),
                ('stockItem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ps1.stockitem')),
            ],
            options={
                'db_table': 'StockTransfer',
            },
        ),
        migrations.AddField(
            model_name='stockitem',
            name='StockEntryId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ps1.stockentry'),
        ),
        migrations.AddField(
            model_name='stockitem',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='globals.departmentinfo'),
        ),
    ]
