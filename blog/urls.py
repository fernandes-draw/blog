from django.urls import path

# from .views import post_list, post_detail
from .views import BlogDetailView, BlogListView

# FUNCTION-BASED VIEW
# urlpatterns = [
#     path("post/<int:pk>/", post_detail, name="post_detail"),
#     path("", post_list, name="home"),
# ]

# GENERIC CLASS-BASED VIEW
urlpatterns = [
    path("post/<int:pk>/", BlogDetailView.as_view(), name="post_detail"),
    path("", BlogListView.as_view(), name="home"),
]
