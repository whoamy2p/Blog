from django.urls import path
from .views import Forms_contact

urlpatterns = [
    path ('', Forms_contact.as_view (), name="Contact")
]