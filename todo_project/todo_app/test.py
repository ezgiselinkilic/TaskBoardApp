from http import HTTPStatus
from django.test import TestCase,SimpleTestCase
from .models import Project, Todos
from .forms import ListForm


class URLTests(TestCase):
    def test_testhomepage(self):
        response=self.client.get('/')
        self.assertEqual(response.status_code,200)


class BasicTest(TestCase):
    def test_fields(self):
        project=Project()
        project.project_name="Proje 1"
        project.save()
        record=Project.objects.get(pk=1)
        self.assertEqual(record,project)
        
class ProjectName(SimpleTestCase):
    def IsEmpty(projectName):
        project=Project()
        if(project.project_name == ""):
            return false

        return true
        assert(isEmpty("string"))

class TestForms(SimpleTestCase):
    def test_list_form_valid_data(self):
        form = ListForm(data={
            'title' : 'todo1',
            'description' : 'todos',
            'notes' : 'Yapılacaklar',
            'project_name' : 'Proje 1'
        })
        self.assertTrue(form.is_valid)
