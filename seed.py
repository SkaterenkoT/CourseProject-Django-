import os
import django

# Настройка Django

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    'CourseProject_web.settings'
)

django.setup()

# Импорты моделей ТОЛЬКО ПОСЛЕ django.setup()

from datetime import date, timedelta

from users.models import User
from topics.models import Topic
from projects.models import Project
from stages.models import Stage
from defenses.models import Defense
from archives.models import Archive


print('Удаление старых данных...')

Stage.objects.all().delete()
Defense.objects.all().delete()
Archive.objects.all().delete()
Project.objects.all().delete()
Topic.objects.all().delete()
User.objects.all().delete()

# ---------------- USERS ----------------

print('Создание пользователей...')

admin = User.objects.create_superuser(
    username='admin',
    password='admin123',
    email='admin@example.com',
    role='admin',
    first_name='System',
    last_name='Administrator',
)

supervisor1 = User.objects.create_user(
    username='ivanov',
    password='12345678',
    email='ivanov@example.com',
    role='supervisor',
    first_name='Иван',
    last_name='Иванов',
)

student1 = User.objects.create_user(
    username='student1',
    password='12345678',
    email='student1@example.com',
    role='student',
    first_name='Алексей',
    last_name='Смирнов',
)

student2 = User.objects.create_user(
    username='student2',
    password='12345678',
    email='student2@example.com',
    role='student',
    first_name='Мария',
    last_name='Кузнецова',
)

# ---------------- TOPICS ----------------

print('Создание тем...')

topic1 = Topic.objects.create(
    title='Система управления дипломами',
    description='Django + DRF система',
    supervisor=supervisor1,
)

topic2 = Topic.objects.create(
    title='AI помощник',
    description='Система поддержки студентов',
    supervisor=supervisor1,
)

# ---------------- PROJECTS ----------------

print('Создание проектов...')

project1 = Project.objects.create(
    student=student1,
    topic=topic1,
    supervisor=supervisor1,
    status='В процессе',
)

project2 = Project.objects.create(
    student=student2,
    topic=topic2,
    supervisor=supervisor1,
    status='На проверке',
)

# ---------------- STAGES ----------------

print('Создание этапов...')

Stage.objects.create(
    project=project1,
    name='Выбор темы',
    status='approved',
    deadline=date.today() + timedelta(days=7),
    order=1,
    comment='Тема утверждена',
)

Stage.objects.create(
    project=project1,
    name='Проектирование БД',
    status='in_review',
    deadline=date.today() + timedelta(days=14),
    order=2,
    comment='На проверке',
)

Stage.objects.create(
    project=project2,
    name='Разработка API',
    status='pending',
    deadline=date.today() + timedelta(days=20),
    order=1,
    comment='Ожидает начала',
)

# ---------------- DEFENSE ----------------

print('Создание защиты...')

defense = Defense.objects.create(
    project=project2,
    defense_date='2026-06-15 10:00:00',
    grade='A',
    result='Допущен',
)

defense.commission.set([
    supervisor1,
    admin,
])

# ---------------- ARCHIVE ----------------

print('Создание архива...')

Archive.objects.create(
    project=project2,
)

print('\\nБаза данных успешно заполнена!')
print('\\nЛогин администратора:')
print('admin / admin123')