from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, FormView

from mysite.forms import ArticleForm, RegisterUserForm, ContactForm, CommentForm, LoginUserForm
from mysite.models import Post, Category


class Home(ListView):
    model = Category
    template_name = 'mysite/home.html'
    cats = Category.objects.all()
    extra_context = {'cats': cats}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        return Category.objects.all


class PostAll(ListView):
    paginate_by = 9
    model = Post
    template_name = 'mysite/allpost.html'
    context_object_name = 'posts'
    cats = Category.objects.all()
    extra_context = {'cats': cats}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Все посты'
        return context

    def get_queryset(self):
        return Post.objects.order_by('title')


def show_post(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    random_post = Post.objects.order_by('?')[:2]
    cats = Category.objects.all()
    comments = post.comments.filter(active=True)

    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(request.POST, request.FILES)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=True)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
            return redirect(request.path)
    else:
        comment_form = CommentForm()

    context = {
        'post': post,
        'cats': cats,
        'random_post': random_post,
        'title': post.title,
        'comments': comments,
        'comment_form': comment_form
    }

    return render(request, 'mysite/post.html', context=context)

class PostCategory(ListView):
    paginate_by = 9
    model = Post
    template_name = 'mysite/allpost.html'
    context_object_name = 'posts'
    cats = Category.objects.all()
    extra_context = {'cats': cats}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['title'] = 'Категория - '
        context['title'] = 'Категория - ' + str(context['posts'][0].cat)
        return context

    def get_queryset(self):
        return Post.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True).order_by('title')


def addpost(request):
    cats = Category.objects.all()
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():

            form.save()
            return redirect('home')  # Перенаправление на главную страницу после успешной обработки формы
    else:
        form = ArticleForm()

    return render(request, 'mysite/addpost.html', {'form': form, 'title': 'Новый пост', 'cats': cats})


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'mysite/register.html'
    success_url = reverse_lazy('login')
    cats = Category.objects.all()
    extra_context = {'cats': cats, 'title': 'Регистрация'}

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'mysite/login.html'
    cats = Category.objects.all()
    extra_context = {'cats': cats, 'title': 'Авторизация'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'mysite/contact.html'
    success_url = reverse_lazy('home')
    cats = Category.objects.all()
    extra_context = {'cats': cats, 'title': 'Контакты'}

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')


class SearchView(ListView):
    model = Post
    template_name = 'mysite/search.html'
    cats = Category.objects.all()
    extra_context = {'cats': cats}

    def get_queryset(self):  # новый
        query = self.request.GET.get('q')
        object_list = Post.objects.filter(Q(title__iregex=query) | Q(content__iregex=query))
        return object_list


