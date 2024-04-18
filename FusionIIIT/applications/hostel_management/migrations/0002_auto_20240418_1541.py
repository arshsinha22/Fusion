# Generated by Django 3.1.5 on 2024-04-18 15:41

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('globals', '0002_auto_20240418_1541'),
        ('academic_information', '0001_initial'),
        ('hostel_management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GuestRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room', models.CharField(max_length=255)),
                ('occupied_till', models.DateField(blank=True, null=True)),
                ('vacant', models.BooleanField(default=True)),
                ('room_type', models.CharField(choices=[('single', 'Single'), ('double', 'Double'), ('triple', 'Triple')], default='single', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='HostelAllotment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assignedBatch', models.CharField(max_length=50)),
                ('assignedCaretaker', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='globals.staff')),
                ('assignedWarden', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='globals.faculty')),
            ],
        ),
        migrations.CreateModel(
            name='HostelComplaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hall_name', models.CharField(max_length=100)),
                ('student_name', models.CharField(max_length=100)),
                ('roll_number', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('contact_number', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='HostelFine',
            fields=[
                ('fine_id', models.AutoField(primary_key=True, serialize=False)),
                ('student_name', models.CharField(max_length=100)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Paid', 'Paid')], default='Pending', max_length=50)),
                ('reason', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='HostelHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('batch', models.CharField(max_length=50, null=True)),
                ('caretaker', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='caretaker_history', to='globals.staff')),
            ],
        ),
        migrations.CreateModel(
            name='HostelInventory',
            fields=[
                ('inventory_id', models.AutoField(primary_key=True, serialize=False)),
                ('inventory_name', models.CharField(max_length=100)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='HostelLeave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=100)),
                ('roll_num', models.CharField(max_length=20)),
                ('reason', models.TextField()),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('start_date', models.DateField(default=django.utils.timezone.now)),
                ('end_date', models.DateField()),
                ('status', models.CharField(default='pending', max_length=20)),
                ('remark', models.TextField(blank=True, null=True)),
                ('file_upload', models.FileField(blank=True, null=True, upload_to='hostel_management/')),
            ],
        ),
        migrations.CreateModel(
            name='HostelTransactionHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('change_type', models.CharField(max_length=100)),
                ('previous_value', models.CharField(max_length=255)),
                ('new_value', models.CharField(max_length=255)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='StudentDetails',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('programme', models.CharField(blank=True, max_length=100, null=True)),
                ('batch', models.CharField(blank=True, max_length=100, null=True)),
                ('room_num', models.CharField(blank=True, max_length=20, null=True)),
                ('hall_no', models.CharField(blank=True, max_length=20, null=True)),
                ('hall_id', models.CharField(blank=True, max_length=20, null=True)),
                ('specialization', models.CharField(blank=True, max_length=100, null=True)),
                ('parent_contact', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='guestroombooking',
            name='room_type',
            field=models.CharField(choices=[('single', 'Single'), ('double', 'Double'), ('triple', 'Triple')], default='single', max_length=10),
        ),
        migrations.AddField(
            model_name='hall',
            name='assigned_batch',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='hall',
            name='type_of_seater',
            field=models.CharField(choices=[('single', 'Single Seater'), ('double', 'Double Seater'), ('triple', 'Triple Seater')], default='single', max_length=50),
        ),
        migrations.AlterField(
            model_name='guestroombooking',
            name='guest_email',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='guestroombooking',
            name='guest_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='guestroombooking',
            name='guest_phone',
            field=models.CharField(max_length=255),
        ),
        migrations.RemoveField(
            model_name='guestroombooking',
            name='guest_room_id',
        ),
        migrations.AddField(
            model_name='guestroombooking',
            name='guest_room_id',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='guestroombooking',
            name='nationality',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='guestroombooking',
            name='status',
            field=models.CharField(choices=[('Confirmed', 'Confirmed'), ('Pending', 'Pending'), ('Rejected', 'Rejected'), ('Canceled', 'Canceled'), ('CancelRequested', 'Cancel Requested'), ('CheckedIn', 'Checked In'), ('Complete', 'Complete'), ('Forward', 'Forward')], default='Pending', max_length=255),
        ),
        migrations.AlterField(
            model_name='staffschedule',
            name='staff_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globals.staff'),
        ),
        migrations.DeleteModel(
            name='GuestRoomDetail',
        ),
        migrations.AddField(
            model_name='hosteltransactionhistory',
            name='hall',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hostel_management.hall'),
        ),
        migrations.AddField(
            model_name='hostelinventory',
            name='hall',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hostel_management.hall'),
        ),
        migrations.AddField(
            model_name='hostelhistory',
            name='hall',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hostel_management.hall'),
        ),
        migrations.AddField(
            model_name='hostelhistory',
            name='warden',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='warden_history', to='globals.faculty'),
        ),
        migrations.AddField(
            model_name='hostelfine',
            name='hall',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hostel_management.hall'),
        ),
        migrations.AddField(
            model_name='hostelfine',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.student'),
        ),
        migrations.AddField(
            model_name='hostelallotment',
            name='hall',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hostel_management.hall'),
        ),
        migrations.AddField(
            model_name='guestroom',
            name='hall',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hostel_management.hall'),
        ),
    ]
