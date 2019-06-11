from django.contrib import admin
from .models import Post
# Register your models here.

admin.site.register(Post)
#이곳에 Post을 입력해 홈페이이제엇 수정을 할 수 있도록 가능하게 해준다. 
#방금 막 모델링 한 글들을 장고 관리자에서 추가하거나 수정, 삭제할 수 있어요.