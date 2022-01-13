from django.shortcuts import render


posts = [
    {
        'author': 'GunjanDhanuka',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'Jan 13, 2022'
    },
    {
        'author': 'Niyati',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'Jan 14, 2022'
    }
]

# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})