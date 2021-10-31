# Generated by Django 3.0.2 on 2021-10-19 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patientdischargedetails',
            old_name='otherCharge',
            new_name='OtherCharge',
        ),
        migrations.AlterField(
            model_name='appointment',
            name='description',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='doctorName',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='patientName',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='address',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='department',
            field=models.CharField(choices=[('Cardiologist', 'Cardiologist'), ('Dermatologists', 'Dermatologists'), ('Emergency Medicine Specialists', 'Emergency Medicine Specialists'), ('Allergists/Immunologists', 'Allergists/Immunologists'), ('Anesthesiologists', 'Anesthesiologists'), ('Colon and Rectal Surgeons', 'Colon and Rectal Surgeons')], default='Cardiologist', max_length=50),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='mobile',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pic/DoctorProfilePic/'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='address',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='patient',
            name='mobile',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='patient',
            name='symptoms',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='patientdischargedetails',
            name='address',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='patientdischargedetails',
            name='assignedDoctorName',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='patientdischargedetails',
            name='mobile',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='patientdischargedetails',
            name='patientName',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='patientdischargedetails',
            name='symptoms',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
