from django.db import models
from django.contrib.auth.models import AbstractUser
from coplate.validators import (
    validate_no_special_characters,
    validator_restauant_link,
)

# Create your models here.


class User(AbstractUser):
    nickname = models.CharField(
        max_length=15,
        unique=True,
        null=True,
        validators=[validate_no_special_characters],
        error_messages={"unique": "이미 사용중인 닉네임입니다."},
    )

    profile_pic = models.ImageField(
        default="default_profile_pic.jpg", upload_to="profile_pics")

    intro = models.CharField(max_length=60, blank=True)

    def __str__(self):
        return self.email


class Review(models.Model):
    title = models.CharField(max_length=30)
    restaurant_name = models.CharField(max_length=20)
    restaurant_link = models.URLField(validators=[validator_restauant_link])

    RATING_CHOICES = [
        (1, '★'),
        (2, '★★'),
        (3, '★★★'),
        (4, '★★★★'),
        (5, '★★★★★'),
    ]
    rating = models.IntegerField(choices=RATING_CHOICES, default=None)

    image1 = models.ImageField(upload_to="review_pics")
    image2 = models.ImageField(upload_to="review_pics", blank=True)
    image3 = models.ImageField(upload_to="review_pics", blank=True)
    content = models.TextField()
    dt_created = models.DateTimeField(auto_now_add=True)
    dt_updated = models.DateTimeField(auto_now=True)

    # ForeignKey(관계되는 모델): 1:N  N쪽에 설정하는 것
    # on_delete 참조하는 오브젝트가 삭제될 때 데이터를 어떻게 할 것인가
    # CASCADE: 유저가 삭제될 때 리뷰가 모드 삭제되도록 설정
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
