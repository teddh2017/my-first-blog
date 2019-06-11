'''
바로 블로그 글을 추가하거나 수정하는 멋진 기능을 추가하는 것이죠. 
장고의 관리자 기능도 충분히 멋있기는 하지만, 
좀 더 입맛에 맞게 바꾸고 예쁘게 꾸미기에는 좀 한계가 있습니다. 
폼(양식, forms)으로 강력한 인터페이스를 만들 수 있어요. 
- 우리가 상상할 수 있는 거의 모든 것을 할 수 있거든요!
'''

from django import forms
# 장고 폼 양식을 사용하기 위해 폼즈 호출
from .models import Post
# post 모델에 자룔를 보내주기 위한 것 

class PostForm(forms.ModelForm):
    #post에 대한 form이기 때문에 이름은 PostForm
    #forms.ModelForm을 괄호 사이에 집어 넣어야  form 구현 가능

    class Meta:
        model = Post
        fields = ('title', 'text',)
    # PostForm 내부에 Meta라는 이름으로 작성할 경우, 타켓 모델은 model = 모델이름 형식으로  
    # 사용자에게 입력받을 부분은 fields = ('1번 컬럼','2번 컬럼',...)형식으로 작성할 수 있다. 