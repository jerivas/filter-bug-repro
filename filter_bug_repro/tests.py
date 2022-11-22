from django.contrib.auth.models import User
from django.test import TestCase

from .urls import Document


class FilterTestCase(TestCase):
    def test_unfiltered(self) -> None:
        user1 = User.objects.create_user("user1")
        user2 = User.objects.create_user("user2")
        Document.objects.create(name="foo", owner=user1)
        Document.objects.create(name="bar", owner=user2)

        response = self.client.get("/api/docs/")
        self.assertJSONEqual(
            response.content.decode("utf-8"),
            [
                {"id": 1, "name": "foo", "owner": 1},
                {"id": 2, "name": "bar", "owner": 2},
            ],
        )

    def test_filtered(self) -> None:
        user1 = User.objects.create_user("user1")
        user2 = User.objects.create_user("user2")
        Document.objects.create(name="foo", owner=user1)
        Document.objects.create(name="bar", owner=user2)

        response = self.client.get("/api/docs/", {"owner": user1.id})
        self.assertJSONEqual(
            response.content.decode("utf-8"),
            [
                {"id": 1, "name": "foo", "owner": 1},
            ],
        )
