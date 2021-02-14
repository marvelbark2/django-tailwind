from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="out.index"),
    path("create", views.create, name="out.create"),
    path("<bad_id>", views.bad , name="out.bad"),
    path("subs/<bad_id>", views.subs , name="out.subs"),
    path("subs/<bad_id>/create", views.subs_create, name="out.subs.create"),

]
