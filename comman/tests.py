from django.test import TestCase
from .models import AboutPage, HomePage


class ImageUploadPathTests(TestCase):
    def test_homepage_images_upload_to_homepage_folder(self):
        for field_name in ("logo", "image"):
            with self.subTest(field=field_name):
                field = HomePage._meta.get_field(field_name)
                filename = field.generate_filename(HomePage(), "sample.jpg")
                self.assertEqual(filename.replace("\\", "/"), "homepage/sample.jpg")

    def test_about_images_upload_to_about_folder(self):
        for field_name in ("BackgroundImage", "FirstImage", "SecondImage"):
            with self.subTest(field=field_name):
                field = AboutPage._meta.get_field(field_name)
                filename = field.generate_filename(AboutPage(), "sample.jpg")
                self.assertEqual(filename.replace("\\", "/"), "about/sample.jpg")
