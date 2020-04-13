# Generated by Django 3.0.4 on 2020-04-12 15:18

import core.managers
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import post.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('location', '0001_initial'),
        ('post', '0005_auto_20200409_1540'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='post',
            managers=[
                ('objects', core.managers.CustomModelManager()),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(help_text='작성자', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('digital', '디지털/가전'), ('furniture', '가구/인테리어'), ('baby', '유아동/유아도서'), ('life', '생활/가공식품'), ('woman_wear', '여성의류'), ('woman_goods', '여성잡화'), ('beauty', '뷰티/미용'), ('male', '남성패션/잡화'), ('sports', '스포츠/레저'), ('game', '게임/취미'), ('book', '도서/티켓/음반'), ('pet', '반려동물용품'), ('other', '기타 중고물품'), ('buy', '삽니다')], help_text='카테고리', max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(help_text='본문'),
        ),
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='locate',
            field=models.ForeignKey(help_text='거래 지역', on_delete=django.db.models.deletion.CASCADE, to='location.Locate'),
        ),
        migrations.AlterField(
            model_name='post',
            name='price',
            field=models.IntegerField(default=0, help_text='가격'),
        ),
        migrations.AlterField(
            model_name='post',
            name='showed_locate',
            field=models.ManyToManyField(help_text='보여질 지역', related_name='showed_locate', to='location.Locate'),
        ),
        migrations.AlterField(
            model_name='post',
            name='state',
            field=models.CharField(choices=[('sales', '판매중'), ('reserve', '예약중'), ('end', '거래완료')], default='sales', help_text='주문 상태', max_length=10),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(help_text='제목', max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='view_count',
            field=models.IntegerField(default=0, help_text='조회 수'),
        ),
        migrations.AlterField(
            model_name='postimage',
            name='photo',
            field=models.ImageField(help_text='상품 사진', upload_to=post.models.post_image_path),
        ),
        migrations.AlterField(
            model_name='postimage',
            name='post',
            field=models.ForeignKey(help_text='게시물 번호', on_delete=django.db.models.deletion.CASCADE, related_name='post_images', to='post.Post'),
        ),
        migrations.AlterField(
            model_name='postlike',
            name='post',
            field=models.ForeignKey(help_text='게시물 번호', on_delete=django.db.models.deletion.CASCADE, to='post.Post'),
        ),
        migrations.AlterField(
            model_name='postlike',
            name='user',
            field=models.ForeignKey(help_text='좋아요 누른 유저', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='recommendword',
            name='content',
            field=models.CharField(help_text='추천 검색어', max_length=100),
        ),
        migrations.AlterField(
            model_name='recommendword',
            name='count',
            field=models.IntegerField(default=0, help_text='검색 횟수'),
        ),
    ]
