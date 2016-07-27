# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-12 11:30
from __future__ import unicode_literals

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
            name='LoginUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=50, verbose_name='昵称')),
                ('sex', models.CharField(choices=[('F', '男'), ('M', '女')], max_length=2, verbose_name='性别')),
                ('age', models.IntegerField(verbose_name='年龄')),
                ('remark', models.CharField(blank=True, max_length=200, null=True, verbose_name='签名')),
                ('friends', models.ManyToManyField(related_name='_loginuser_friends_+', to='chatroom.LoginUser')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupname', models.CharField(max_length=100, verbose_name='用户分组名')),
                ('members', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usergroup_member', to='chatroom.LoginUser')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mygroup', to='chatroom.LoginUser')),
            ],
        ),
        migrations.CreateModel(
            name='WebGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='群组名')),
                ('brief', models.CharField(blank=True, max_length=200, null=True, verbose_name='群组备注')),
                ('max_members', models.IntegerField()),
                ('admins', models.ManyToManyField(blank=True, null=True, related_name='webgroup_admins', to='chatroom.LoginUser')),
                ('members', models.ManyToManyField(blank=True, null=True, related_name='webgroup_member', to='chatroom.LoginUser')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chatroom.LoginUser')),
            ],
        ),
    ]