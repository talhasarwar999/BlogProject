from django.urls import path
from . import views
urlpatterns = [
    path('',views.blogs, name="blogs"),
    path('postComment',views.postComment,name="postComment"),
    path('blogss/<str:slug>',views.blogss, name="blogss"),
    path('blogsss/<str:slug>',views.blogsss, name="blogsss"),
    path('delete/<int:sno>',views.delete, name="delete"),
    path('deletep/<int:sno>',views.deletep, name="deletep"),
    path('edit/<int:sno>', views.edit,name="edit"),
    path('update/<int:sno>', views.update,name="update"),
    path('editreply/<int:sno>', views.editreply, name="editreply"),
    path('updatereply/<int:sno>', views.updatereply, name="updatereply"),
]
