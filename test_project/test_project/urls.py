# urls.py
from django.urls import path
from django.contrib import admin
from .views import get_stripe_session_id, ItemDetailView, get_item_html,SuccessDetailView,CanselDetailView

urlpatterns = [
    path('buy/<int:id>/', get_stripe_session_id, name='get_stripe_session_id'),
    path('item/<int:id>/', ItemDetailView.as_view(), name='item_detail'),
    path('item_html/<int:id>/', get_item_html, name='get_item_html'),
    path('admin/', admin.site.urls),
    path('success/', SuccessDetailView, name='success'),
    path('cancel/', CanselDetailView, name='cancel')


]
