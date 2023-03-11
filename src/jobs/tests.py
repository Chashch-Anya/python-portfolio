from datetime import datetime

from django.test import TestCase

from jobs.models import Job


class BlogTestCase(TestCase):
    """
    Тестирование функций работ.
    """

    def setUp(self) -> None:
        """
        Настройка перед тестированием.

        :return:
        """

        Job.objects.create(
            image="job",
            description="job",
            detailed_description="job",
        )

    def test_blog_messages_creation(self) -> None:
        """
        Тестирование моделей.

        :return:
        """

        job = Job.objects.get(description="job")

        content = "job" * 100
        self.assertEqual(job.summary(), content[:100] + "...")
        self.assertEqual(str(job), f'Объект "Выполненная работа" (id={job.pk})')
