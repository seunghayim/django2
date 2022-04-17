from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Review
# Register your models here.
admin.site.register(User, UserAdmin)
# 유저 모델의 추가 field를 admin 에 추가하기 위해
UserAdmin.fieldsets += (("Custom fields",
                        {"fields": ("nickname", "profile_pic", "intro")}),)

admin.site.register(Review)
