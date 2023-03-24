from django.test import TestCase
from .views import zodiac


class TestHoroscope(TestCase):

    def test_libra(self):
        response = self.client.get('/horoscope/libra/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября)',
                      response.content.decode())


    def test_signs(self):
        for page in list(zodiac.keys()):
            response = self.client.get(f'/horoscope/{page}/')
            self.assertEqual(response.status_code, 200)
            self.assertIn(zodiac[page].response, response.content.decode())

    def test_redirect(self):
        for num in range(1,13):
            response = self.client.get(f'/horoscope/{num}')
            self.assertEqual(response.status_code, 302)
            self.assertEqual(response.url, f'/horoscope/{list(zodiac.keys())[num-1]}/')