from django.test import TestCase
from users.models import User, Profile


class UserTestCase(TestCase):
    def test_false_is_false(self):
        self.assertEqual(False, False)

    def test_create_user_manual(self):
        test_user = User.objects.create(username='test')

        user = User.objects.filter(username='test').exists()

        self.assertTrue(user)


class ProfileTestCase(TestCase):
    def test_true_is_true(self):
        self.assertEqual(True, True)

    def test_profile_created_on_user_creation(self):
        test_user = User.objects.create(username='test')

        profile = Profile.objects.all()[:1].get()
        
        self.assertEqual(str(profile), 'test Profile')
        