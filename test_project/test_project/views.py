from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
import stripe
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView
from .models import Item

stripe.api_key = "sk_test_51OHqQMA0O7Z5JXeoVQaLTNNfAIIjBNT6aKiDfXq5bSu5jk0FRBbJlOv0VstxIB9FDTM8cRa51cT4LAW9kVC2Vac000sPkqILMX"
@csrf_exempt
def get_stripe_session_id(request, id):
    item = get_object_or_404(Item, pk=id)
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': item.currency,
                'product_data': {
                    'name': item.name,
                    'description': item.description
                },
                'unit_amount': int(item.price * 100),
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri(reverse('success')),
        cancel_url=request.build_absolute_uri(reverse('cancel')),
    )
    print(session.status)
    print(session.id)
    return JsonResponse({'session_id': session.id})
    # return render(request, 'item_detail.html', {'item': item, 'session_id': session.id})
class ItemDetailView(DetailView):
    model = Item
    pk_url_kwarg = 'id'
    template_name = 'item_detail.html'

def SuccessDetailView(DetailView):
        return HttpResponse(f'<h1>Товар успешно куплен</h1>')
def CanselDetailView(DetailView):
        return HttpResponse(f'<h1>Товар не куплен</h1>')

def get_item_html(request, id):
    item = get_object_or_404(Item, pk=id)
    return HttpResponse(f'<h1>{item.name}</h1><p>{item.description}</p><button onclick="redirectToCheckout({item.id})">Buy</button>')
