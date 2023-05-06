from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    if request.method == 'POST':
        return HttpResponse(request.POST['item_text'])
    return render(request, 'home.html')

def test_can_save_a_POST_request(self):
   response = self.client.post('/', data={'item_text': 'A new list item'})
   self.assertIn('A new list item', response.content.decode())
   self.assertTemplateUsed(response, 'home.html')