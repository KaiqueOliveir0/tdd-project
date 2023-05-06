from django.http import HttpResponse
from django.shortcuts import render
from django.test import TestCase
from lists.models import Item

def home_page(request):
    return render(request, 'home.html', {
        'new_item_text': request.POST.get('item_text', ''),
    })

def test_can_save_a_POST_request(self):
   response = self.client.post('/', data={'item_text': 'A new list item'})
   self.assertIn('A new list item', response.content.decode())
   self.assertTemplateUsed(response, 'home.html')

class ItemModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = 'O primeiro item'
        first_item.save()

        second_item = Item()
        second_item.text = 'O segundo item'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'O primeiro item')
        self.assertEqual(second_saved_item.text, 'O segundo item')