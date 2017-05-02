from django.contrib.auth.models import User
from django.urls import reverse

from orotangi.models import Books, Notes

from rest_framework import status
from rest_framework.test import APITestCase, APIClient


class OrotangiTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='john',
                                             email='john@doe.info',
                                             password='doe')

        self.client = APIClient()
        self.client.force_authenticate(user=self.user)


class BooksTests(OrotangiTests):

    def test_get_books(self):
        """
        Ensure we can get the books list.
        """
        url = reverse('books-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_book(self):
        """
        Ensure we can create a new book object.
        """

        data = {'name': 'Book1',
                'user': self.user.username}

        url = reverse('books-list')
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Books.objects.count(), 1)
        self.assertEqual(Books.objects.get().name, 'Book1')


class NotesTests(OrotangiTests):

    def test_get_notes(self):
        """
        Ensure we can get the notes list.
        """
        url = reverse('notes-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_notes_and_books_and_q(self):
        """
        Ensure we can get the notes list.
        """
        url = reverse('notes-list')
        data = {'book': 'Book1'}
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # test for getting in Book1 a string in the book name or note name
        # containing 'Book'
        data = {'book': 'Book1', 'q': 'Book'}
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_note(self):
        """
        Ensure we can create a new note object.
        """
        data = {'name': 'Book1',
                'user': self.user.username}

        url = reverse('books-list')
        self.client.post(url, data, format='json')

        data = {'user': self.user.id,
                'book': 1,
                'title': 'Note1',
                'content': 'this is my note',
                'url': '',
                'status': True,
                }

        url = reverse('notes-list')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Notes.objects.count(), 1)
        self.assertEqual(Notes.objects.get().title, 'Note1')

    def test_model_note(self):
        data = {'user': self.user,
                'book': Books(name="Book1", user=self.user),
                'title': 'Note1',
                'content': 'this is my note',
                'url': '',
                'status': True,
                }
        n = Notes(**data)
        self.assertTrue(isinstance(n, Notes))
        self.assertEqual(n.__str__(), "%s - %s" % (n.book, n.title))
