from django.test import TestCase
from lists.forms import EMPTY_ITEM_ERROR, ItemForm
from lists.models import List, Item


class ItemFormTest(TestCase):

    def test_form_renders_id_text_input(self):
        form = ItemForm(data={'text':''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['text'], [EMPTY_ITEM_ERROR])

    def test_form_handles_saving_to_a_list(self):
        list_ = List.objects.create()
        form = ItemForm(data={'text':'do me'})
        new_item = form.save(for_list=list_)
        self.assertEqual(new_item, Item.objects.first())
        self.assertEqual(new_item.text, 'do me')
        self.assertEqual(new_item.list, list_)