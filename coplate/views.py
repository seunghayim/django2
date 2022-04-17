from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from braces.views import LoginRequiredMixin, UserPassesTestMixin
from allauth.account.models import EmailAddress
from allauth.account.views import PasswordChangeView
from coplate.models import Review, User
from coplate.forms import ReviewForm, ProfileForm
from coplate.functions import confirmation_required_redirect
# Create your views here.


class IndexView(ListView):
    model = Review
    template_name = "coplate/index.html"
    context_object_name = "reviews"
    paginate_by = 4
    ordering = ["-dt_created"]


class ReviewDetailView(DetailView):
    model = Review
    template_name = "coplate/review_detail.html"
    # URL에 전달되는 오브젝트 id 이름을 제네릭 뷰에 전달할 때 사용
    pk_url_kwarg = 'review_id'


class ReviewCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "coplate/review_form.html"

    # view에 접근하지 못한 유저들 중에 로그인을 안한 유저와 한 유저를 어떻게 처리할 것인지
    # True일 경우 로그인 한 유저는 raise 안한 유저는 로그안 창으로
    # False일 경우 둘다 raise로 처리
    redirect_unauthenticated_users = True
    # 위의 여부에 따라 raise에서 처리
    raise_exception = confirmation_required_redirect

    # 입력받은 데이터가 유효할 때, 데이터로 채워진 모델 오브젝트를 만들고 오브젝트를 저장하는 역할
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("review-detail", kwargs={"review_id": self.object.id})

    # 로그인한 유저의 이메일 인증 여부
    def test_func(self, user):
        return EmailAddress.objects.filter(user=user, verified=True).exists()


class ReviewUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = 'coplate/review_form.html'
    pk_url_kwarg = 'review_id'

    # 다른 유저들 모두 권한오류를 주겠다.
    raise_exception = True
    # redirect_unauthenticated_users = False

    def get_success_url(self):
        return reverse('review-detail', kwargs={'review_id': self.object.id})

    # 로그인한 유저가 작성게시글의 유저와 같은지 같아야만 수정가능
    def test_func(self, user):
        review = self.get_object()
        return review.author == user


class ReviewDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Review
    TEMPLATE_NAME = 'coplate/review_confirm_delete.html'
    pk_url_kwarg = 'review_id'

    # 다른 유저들 모두 권한오류를 주겠다.
    raise_exception = True
    # redirect_unauthenticated_users = False

    def get_success_url(self):
        return reverse('index')

    # 로그인한 유저가 작성게시글의 유저와 같은지 같아야만 수정가능
    def test_func(self, user):
        review = self.get_object()
        return review.author == user


class ProfileView(DetailView):
    model = User
    template_name = 'coplate/profile.html'
    pk_url_kwarg = 'user_id'
    context_object_name = 'profile_user'

    # user_id에 해당하는 유저는 profile_user라는 이름으로 template에 전달
    # 이 유저가 작성한 리뷰중 최신 리뷰 4개가
    # 'user_review' 라는 이름으로 template에 전달된다.
    def get_context_data(self, **kwargs):
        # 먼저 기존의 context를 가져오고,
        context = super().get_context_data(**kwargs)
        # URL로 전달되는 user_id 파라미터를 가져옴
        user_id = self.kwargs.get('user_id')
        # 게시글 작성자의 id가 user_id인 게시글만 필터
        context['user_reviews'] = Review.objects.filter(
            author__id=user_id).order_by('-dt_created')[:4]
        return context


class UserReviewListView(ListView):
    model = Review
    template_name = "coplate/user_review_list.html"
    context_object_name = "user_reviews"
    paginate_by = 4

    # 현재 패이지에 있는 유저
    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        return Review.objects.filter(author__id=user_id).order_by('dt_created')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile_user'] = get_object_or_404(
            User, id=self.kwargs.get('user_id'))
        return context


class ProfileSetView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = ProfileForm
    template_name = 'coplate/profile_set_form.html'

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse('index')


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = ProfileForm
    template_name = 'coplate/profile_update_form.html'

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse('profile', kwargs={'user_id': self.request.user.id})


class CustomPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    def get_success_url(self):
        return reverse('profile', kwargs={'user_id': self.request.user.id})
