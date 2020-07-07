from django.shortcuts import render
from blog.models import BlogPost

# Create your views here.

# def index_unlog(request):
#     return render(request, 'index_unlog.html')

# def index_unlog(request):
#     return render(request, 'index_unlog.html')

# def login(request):
#     if request.method == 'POST':
#         user_name = request.POST.get('username', '')
#         pass_word = request.POST.get('password', '')
#         user = User.objects.filter(username=user_name)
#         if user:
#             user = User.objects.get(user_name=user_name)
#             if pass_word == User.password:
#                 request.session['IS_LOGIN'] = True
#                 request.session['username'] = user_name
#                 request.session['nickname'] = user.nickname
#                 return render(request, 'index.html', {'user': user})
#             else:
#                 return render(request, 'login.html', {'error': '密码错误'})
#         else:
#             return render(request, 'login.html', {'error': '该用户不存在'})
#     else:
#         return render(request, 'login.html')


# def logsuccess(request):
#     return render(request, 'index.html')

# def archive(request):
#     posts = BlogPost.objects.all()
#     return render(request, 'archive.html', {'posts': posts})

def blog_index(request):
    blog_list = BlogPost.objects.all()
    return render(request, 'index.html', {'blog_list': blog_list})


