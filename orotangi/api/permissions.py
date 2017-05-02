from rest_framework import permissions


class DjangoModelPermissions(permissions.BasePermission):

    perms_map = {
        'GET': [],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['orotangi.add_books', 'orotangi.add_notes'],
        'PUT': ['orotangi.change_books', 'orotangi.change_notes'],
        'PATCH': ['orotangi.change_books', 'orotangi.change_notes'],
        'DELETE': ['orotangi.delete_books', 'orotangi.delete_notes'],
    }
