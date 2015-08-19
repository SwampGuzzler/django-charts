from django.test import TestCase

# Create your tests here.
from api.models import Character

class ViewTest(TestCase):

    def test_create_character_view(self):
        self.assertEqual(Character.objects.count(), 0)

        # Run the view function via POST
        resp = self.client.post('/create', {'name': 'testname', 'img_url': 'www.test.com/test.jpg'})

        # Verify the page redirected to the new character's page
        self.assertEqual(resp['location'], 'http://testserver/testname/thanks')

        # Verify the character was created as expected
        self.assertEqual(Character.objects.count(), 1)
        test_character = Character.objects.first()
        self.assertEqual(test_character.name, 'testname')
        self.assertEqual(test_character.img_url, 'www.test.com/test.jpg')