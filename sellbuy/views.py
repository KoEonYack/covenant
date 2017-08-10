# blog/views.py
from django.http import Http404
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from .models import SellPost
from .forms import PostForm
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from hitcount.models import HitCount
from hitcount.views import HitCountMixin


# 처음 페이지 메인에 들어올 때마다 로그인을 체크한다.
def main(request):
    if 'username' in request.POST:
        user = authenticate(username=request.POST['username'], password=request.POST['password'])

        if user is not None:
            auth_login(request, user)
        else:
            redirect('login')  # 로그인폼 url

    return render(request, 'sellbuy/main.html')

# 계시글의 list 보여주기

@login_required
def sell_list(request):
    """
    page = request.GET.get('page', '1') # page = request.GET.get('page', '1')
    if page == '':
        page = '1'
    page = int(page)
    qs = SellPost.objects.all()
    q = request.GET.get('q', '')
    if q:
        qs = qs.filter(title__icontains=q)

    num = 10
    paginator = Paginator(qs, num)
    contacts = paginator.page(page)

    start_index = 1
    for i in reversed(range(1, page + 1)):
        if i % num == 1:
            start_index = i
        break

    end_index = start_index + num
    page_range = range(start_index, end_index)

    return render(request, 'sellbuy/sell_list.html', {
        'post_list': qs,
        'q': q,
        'contacts': contacts,
        'page_range': page_range
    })
    """
    # 검색 코드
    q = request.GET.get('q', '')
    if q:
        qs = SellPost.objects.filter(title__icontains=q)
    else:
        qs = SellPost.objects.all()

    paginator = Paginator(qs, 15)  # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        qs = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        page = 1
        qs = paginator.page(page)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        if int(page) <= 0:
            page = 1
        else:
            page = paginator.num_pages
        qs = paginator.page(page)

    num = 10
    end_index = ((int(page) + num - 1) // num) * num
    start_index = end_index - num + 1
    prev = end_index - num
    next = start_index + num

    if paginator.num_pages < end_index:
        end_index = paginator.num_pages

    page_range = range(start_index, end_index + 1)

    return render(request, 'sellbuy/sell_list.html', {
        'post_list': qs,
        'q': q,
        'page_range': page_range,
        'prev': prev,
        'next': next,
        'currentPage' : int(page),
    })


# 계시글의 세부 사항을 보여주기
@login_required
def sell_detail(request, id):

    post = get_object_or_404(SellPost, id=id)

    hit_count = HitCount.objects.get_for_object(post)  # 해당객체를의 조회수를 불러옵니다.
    hit_count_response = HitCountMixin.hit_count(request, hit_count)  # 같은 사용자가 이미 방문을 했다면 false를 반환합니다.(이미 조회수를 저리했기때문)

    return render(request, 'sellbuy/sell_detail.html', {
        'post': post,
    })

# sell에서 새로운 계시글을 만들기
@login_required
def sell_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            messages.info(request, '새 포스팅을 저장했습니다.')
            return redirect(post)  # post.get_absolute_url() => post detail
    else:
        form = PostForm()
    return render(request, 'sellbuy/sell_form.html', {
        'form': form,
    })

# sell에서 계시글을 수정하기
@login_required
def sell_edit(request, id):
    post = get_object_or_404(SellPost, id=id)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            messages.info(request, '포스팅을 수정했습니다.')
            return redirect(post)  # post.get_absolute_url() => post detail
    else:
        form = PostForm(instance=post)
    return render(request, 'sellbuy/sell_form.html', {
        'form': form,
    })



def introduce_human(request):
    return render(request, 'sellbuy/introduce_human.html')

