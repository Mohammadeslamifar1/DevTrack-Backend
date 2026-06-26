import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from projects.models import Project
from tasks.models import Task
from django.urls import reverse

@pytest.mark.django_db
def test_project_crud_and_permissions():
    client = APIClient()

    # create two users
    alice = User.objects.create_user(username='alice', password='pass')
    bob = User.objects.create_user(username='bob', password='pass')

    # alice logs in
    client.force_authenticate(user=alice)

    # alice creates a project
    resp = client.post('/api/projects/', {'name': 'Alice Project', 'description': 'x'})
    assert resp.status_code == 201
    project_id = resp.data['id']

    # alice can list her projects
    resp = client.get('/api/projects/')
    assert resp.status_code == 200
    assert any(p['id'] == project_id for p in resp.data['results'])

    # bob cannot access alice's project
    client.force_authenticate(user=bob)
    resp = client.get(f'/api/projects/{project_id}/')
    assert resp.status_code in (403, 404)

@pytest.mark.django_db
def test_task_creation_under_owned_project():
    client = APIClient()
    user = User.objects.create_user(username='u', password='p')
    client.force_authenticate(user=user)

    # create project
    resp = client.post('/api/projects/', {'name': 'P', 'description': ''})
    assert resp.status_code == 201
    project_id = resp.data['id']

    # create task under project
    task_payload = {'project': project_id, 'title': 'T1', 'description': '', 'status': 'todo', 'priority': 'medium'}
    resp = client.post('/api/tasks/', task_payload)
    assert resp.status_code == 201
    assert resp.data['title'] == 'T1'
