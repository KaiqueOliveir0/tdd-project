from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    return render(request, 'home.html', {
        'new_item_text': request.POST.get('item_text', ''),
    })

def test_can_save_a_POST_request(self):
   response = self.client.post('/', data={'item_text': 'A new list item'})
   self.assertIn('A new list item', response.content.decode())
   self.assertTemplateUsed(response, 'home.html')