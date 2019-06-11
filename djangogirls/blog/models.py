from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model): # 모델을 정의하는 코드 모델 = 객체 
    #
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    #'auth.User'라는 창고가 존재하고 있었기 때문에 연결이 가능햇다. 
    #admin 계정을 위해 장고에서 자동으로 생성하는 모델명 creatsuperuser 명려어등으로 생성한 계정을 저장
    title = models.CharField(max_length=200)
    #제목 부분, charfield는 글자수가 제한된 필드 최대 200글자
    text = models.TextField()
    #본문 표시 , textfield는 글자수 제한이 없음을 의미함
    created_date = models.DateTimeField(
            default=timezone.now)
    # 작성시간을 나타내는 부분  ---- ctrl+space 
    # 이것은 timezone use in django.utils, 
    # first text write time part, default is 미입력시 자동기입할 자료  
    published_date = models.DateTimeField(
            blank=True, null=True)
    # 최종 수정시간을 나타내는 부분,
    # blank는 공백으로 둬도 되는지, null은 입력을 안해도 되는지를 나타냄 

    def publish(self):
        self.published_date = timezone.now()
        self.save()
        
    #글을 수정할 때 실험할 함수, 사용자가 날짜를 기입하는게 아니라 
    #수정시 매번 호출되어 최종 수정시간을 갱신한다. 
    #바꾼 시간은 저장까지 해 줘야 db에 반영이 된다. 

    def __str__(self):
        return self.title
    
    #str양 옆에 언더스코어(_) 를 두 개씩 넣었는지 다시 확인하세요. 
    #파이썬에서 자주 사용되는데, "던더(dunder; 더블-언더스코어의 준말)"라고도 불려요.
    #글 제목이 설정하게 해주는  부분 
    
    