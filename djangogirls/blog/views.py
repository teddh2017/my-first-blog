from django.shortcuts import render, get_object_or_404, redirect
#from django.http.response import HttpResponse
from .models import Post
#from _datetime import timezone
from django.utils import timezone
from .forms import PostForm


# Create your views here.
def post_list(request):
    # return HttpResponse("post_list 준비중!!!!")
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    #Post를 담고 있는 변수이다. 
    return render(request, "blog/post_list.html", {'posts':posts})

'''
Post.object. 을 이용해서 다음 조건을 만족시키는 ORM을 사용해보세요.
배포 시간이 현재 시간 이전일것
published_date 기준으로 내림차순 설정 
'''

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    #form 양식을 작성할 경우에는 forms.py내부의 자룔를 form이라는 변수에 저장 
    #form = PostForm()
    #저장된 form을 render 함수를 이용해서 템플릿으로 보내준다. 
    #return render(request, 'blog/post_edit.html', {'form': form})
    
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #author 컬럼에는 요청한 유저를 집어넣는다.
            #admin에서 로그인을 할 경우에만 가능 
            post.published_date = timezone.now()
            #위 컬럼에는 현재 시간을 집어 넣는다. 
            post.save()
            #모자란 2개 컬럼을 다 채웠기 때문에 데베에 완전 저장.
            return redirect('post_detail', pk=post.pk)
            #자료를 다 집어 넣었다면 올린 글을 확인할 수 있도록 상세페이지로 간다. 
    else:
        form = PostForm()
        #추가적으로 유효한 자료가 검증되지 않는다면  form을 다시 비운다. 
    return render(request, 'blog/post_edit.html', {'form': form})
   
    ''' postform 양식을 받아오되  포스트 방식으로 전달된 데이터를 채워넣는다. 
           이렇게 되면 title, text, create_date 세개의 컬럼에 지료가 채워진다.
          단, 아직 author publishe_date에는 자료가 채워지지 않는 상태이다. --if request.method == "POST"
       
         들어온 자료가 올바른 자료인지 .is_valid() 로 검사한다.
         자료가 올바른 (폼을 통해 전달된 자료)라면  is_valid() True이다. --if form.is_valid():
         
      나머지 2개 컬럼에 대해서도 자료를 모두 저장하기 위해서 먼저 현재 들어와있는 3개 자료에 대해서 임시저장을 한다. 
    commit=False로 save() 함수를 실행하면 임시저장 상태가 된다. -- post = form.save(commit=False)
     '''

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            #수정시에도 역시 published_date와 글쓴이 확인을 해야함
            #그래서 임시저장을 먼저 하고 나서 밑에 2개를 다시 입력
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            #그래서 정보를 모두 넘겨받으면 다시 최종적으로 저장 
            post.save()
            #마지막으로 수정 결과를 확인 받게 하는 것 
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
    #만약에 get방식인 경우에는 수정결과 변영이 안니 수정창만 보여준다. 













