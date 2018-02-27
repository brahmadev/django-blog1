

# Create your views here.
# Create your views here.
from django.views.generic import ListView, DetailView

from post.models import Post


class LandingPage(ListView):
    template_name = 'post/landing.html'
    model = Post
    ordering = ['-created_at']



class PostDetail(DetailView):
    template_name = 'post/detail.html'
    model = Post

