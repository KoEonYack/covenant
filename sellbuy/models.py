import re
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models


class SellPost(models.Model):
    ''' 다음 모델링은 삽니다 팝니다의 잔재로 남은 것에 대한 모델링이다.
    STATUS_CHOICES = (
        ('d', '도서'),
        ('b', '부동산'),
        ('g', '가구'),
        ('j', '전자기기'),
        ('h', '화장품'),
        ('e', '의류'),
        ('s', '스포츠'),
        ('h', '생활용품'),
        ('g', '기타'),
    )
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    tag_set = models.ManyToManyField('Tag', blank=True)
    price = models.CharField( max_length=100, blank=False)
    # 판매중 판매완료에 대한 모델링을 해야 한다.
    '''

    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=100, verbose_name='제목',
                             help_text='포스팅 제목을 입력해주세요. 최대 100자 내외.')  # 길이 제한이 있는 문자열
    content = models.TextField(verbose_name='내용')  # 길이 제한이 없는 문자열

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # 사진 첨부기능 추가하기

    class Meta:
        ordering = ['-id']

    def get_absolute_url(self):
        return reverse('sell_list_page:sell_detail', args=[self.id])  #오류가 발생한 곳

    def __str__(self):
        return self.title