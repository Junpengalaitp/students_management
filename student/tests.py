from django.test import TestCase, Client

from .models import Student

class StudentTestCase(TestCase):
    def setUp(self):
        Student.objects.create(
            name='the5fire',
            sex=1,
            email='hejp009@gmail.com',
            profession='Software Engineer',
            qq='553931470',
            phone='339922',
        )
    
    def test_create_and_sex_show(self):
        student = Student.objects.create(
            name='huyang',
            sex=1,
            email='nobody@dd.com',
            profession='developer',
            qq='3333',
            phone='3213',
        )
        self.assertEqual(student.sex_show, 'Male', 'Sex are not equal to the content showing!')

    def test_filter(self):
        Student.objects.create(
            name='huyang',
            sex=1,
            email='nobody@dd.com',
            profession='coder',
            qq='3333',
            phone='32',
        )
        name = 'the5fire'
        students = Student.objects.filter(name=name)
        self.assertEqual(students.count(), 1, 'There should be only one name record as {}'.format(name))


    def test_get_index(self):
        # test index
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200, 'status code must be 200!')

    def test_post_student(self):
        client = Client()
        data = dict(
            name='test_for_post',
            sex=1,
            email='333@dd.com',
            profession='coder',
            qq='3333',
            phone='32222',
        )
        response = client.post('/', data)
        self.assertEqual(response.status_code, 302, 'status code must be 302!')

        response = client.get('/')
        self.assertTrue(b'test_for_post' in response.content,
                        'response content must contain "test_for_post"')
    