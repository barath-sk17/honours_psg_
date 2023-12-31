# Generated by Django 4.2.1 on 2023-08-10 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('hrs', models.IntegerField()),
                ('status', models.CharField(choices=[('Present', 'Present'), ('Absent', 'Absent')], max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='CourseIndex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.CharField(max_length=10, unique=True)),
                ('course_name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='FacultyIndex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty_id', models.CharField(max_length=10, unique=True)),
                ('faculty_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sem', models.CharField(choices=[('Odd', 'Odd'), ('Even', 'Even')], max_length=15, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=7)),
                ('sem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='years', to='record.semester')),
            ],
        ),
        migrations.CreateModel(
            name='StudentIndex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=10, unique=True)),
                ('student_name', models.CharField(max_length=50)),
            ],
            options={
                'unique_together': {('student_id', 'student_name')},
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='record.faculty')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='studentindex', to='record.studentindex')),
                ('student_year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='studentyear', to='record.year')),
            ],
        ),
        migrations.AddConstraint(
            model_name='semester',
            constraint=models.UniqueConstraint(fields=('sem',), name='unique_combination1'),
        ),
        migrations.AlterUniqueTogether(
            name='facultyindex',
            unique_together={('faculty_id', 'faculty_name')},
        ),
        migrations.AddField(
            model_name='faculty',
            name='course_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='faculties', to='record.course'),
        ),
        migrations.AddField(
            model_name='faculty',
            name='faculty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='facultyindex', to='record.facultyindex'),
        ),
        migrations.AddField(
            model_name='faculty',
            name='faculty_year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='facultyyear', to='record.year'),
        ),
        migrations.AddField(
            model_name='course',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courseindex', to='record.courseindex'),
        ),
        migrations.AddField(
            model_name='course',
            name='course_year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='record.year'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='student_detail',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='atendance_student', to='record.student'),
        ),
        migrations.AlterUniqueTogether(
            name='year',
            unique_together={('year', 'sem')},
        ),
        migrations.AlterUniqueTogether(
            name='student',
            unique_together={('student', 'course_id', 'student_year')},
        ),
        migrations.AlterUniqueTogether(
            name='faculty',
            unique_together={('faculty', 'course_id', 'faculty_year')},
        ),
        migrations.AlterUniqueTogether(
            name='course',
            unique_together={('course', 'course_year')},
        ),
        migrations.AlterUniqueTogether(
            name='attendance',
            unique_together={('student_detail', 'hrs', 'status', 'date')},
        ),
    ]
