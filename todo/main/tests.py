from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse, resolve, resolve
from django.contrib.auth.views import LogoutView
from main.views import *
from main.models import *


class TestUrls(SimpleTestCase):

    def test_home_url_is_resolved(self):
        url = reverse('home')
        #print(resolve(url))

        self.assertEquals(resolve(url).func, home)


    def test_register_url_is_resolved(self):
        url = reverse('register')

        self.assertEquals(resolve(url).func, register)


    def test_reminders_url_is_resolved(self):
        url = reverse('reminders')

        self.assertEquals(resolve(url).func.view_class, ReminderList)


    def test_tasks_url_is_resolved(self):
        url = reverse('tasks')

        self.assertEquals(resolve(url).func.view_class, TaskList)


    def test_user_todos_url_is_resolved(self):
        url = reverse('user_todos', args=['some-user'])

        self.assertEquals(resolve(url).func.view_class, TodoUserList)

    
    def test_todos_url_is_resolved(self):
        url = reverse('todos')

        self.assertEquals(resolve(url).func.view_class, TodoList)


    def test_user_url_is_resolved(self):
        url = reverse('user', args=['some-user'])

        self.assertEquals(resolve(url).func.view_class, SpecificUser)


    def test_users_url_is_resolved(self):
        url = reverse('users')

        self.assertEquals(resolve(url).func.view_class, UserList)

    
    def test_logout_url_is_resolved(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func.view_class, LogoutView)
        

    def test_add_user_url_is_resolved(self):
        url = reverse('add_user')
        self.assertEquals(resolve(url).func.view_class, UserCreateView)
        

    def test_edit_user_url_is_resolved(self):
        url = reverse('edit_user', args=[1])
        self.assertEquals(resolve(url).func.view_class, UserUpdateView)
        

    def test_delete_user_url_is_resolved(self):
        url = reverse('delete_user', args=[1])
        self.assertEquals(resolve(url).func.view_class, UserDeleteView)
        

    def test_add_todo_url_is_resolved(self):
        url = reverse('add_todo')
        self.assertEquals(resolve(url).func.view_class, TodoCreateView)
    

    def test_update_todo_url_is_resolved(self):
        url = reverse('update_todo', args=[1])
        self.assertEquals(resolve(url).func.view_class, TodoUpdateView)


    def test_delete_todo_url_is_resolved(self):
        url = reverse('delete_todo', args=[1])
        self.assertEquals(resolve(url).func.view_class, TodoDeleteView)


    def test_task_create_url_is_resolved(self):
        url = reverse('task_create')
        self.assertEquals(resolve(url).func.view_class, TaskCreateView)


    def test_task_todo_create_url_is_resolved(self):
        url = reverse('task_todo_create', args=[1])
        self.assertEquals(resolve(url).func, add_task_reminder)


    def test_task_update_url_is_resolved(self):
        url = reverse('task_update', args=[1])
        self.assertEquals(resolve(url).func.view_class, TaskUpdateView)


    def test_task_delete_url_is_resolved(self):
        url = reverse('task_delete', args=[1])
        self.assertEquals(resolve(url).func.view_class, TaskDeleteView)


    def test_reminder_add_url_is_resolved(self):
        url = reverse('reminder_add', args=[1])
        self.assertEquals(resolve(url).func, add_reminder)


    def test_reminder_update_url_is_resolved(self):
        url = reverse('reminder_update', args=[1])
        self.assertEquals(resolve(url).func.view_class, ReminderUpdateView)


    def test_reminder_delete_url_is_resolved(self):
        url = reverse('reminder_delete', args=[1])
        self.assertEquals(resolve(url).func.view_class, ReminderDeleteView)


    def test_search_task_url_is_resolved(self):
        url = reverse('search_tasks')
        self.assertEquals(resolve(url).func, search_task)


    def test_search_todo_url_is_resolved(self):
        url = reverse('search_todos')
        self.assertEquals(resolve(url).func, search_todo)


    def test_search_user_url_is_resolved(self):
        url = reverse('search_users')
        self.assertEquals(resolve(url).func, search_user)
        

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home')
        self.register_url = reverse('register')
        self.reminders_url = reverse('reminders')
        self.tasks_url = reverse('tasks')
        self.user_todos_url = reverse('user_todos', args=['some-user'])
        self.todos_url = reverse('todos')
        self.user_url = reverse('user', args=['some-user'])
        self.users_url = reverse('users')

        self.add_user_url = reverse('add_user')
        self.edit_user_url = reverse('edit_user', args=[1])
        self.delete_user_url = reverse('delete_user', args=[1])
        self.add_todo_url = reverse('add_todo')
        self.update_todo_url = reverse('update_todo', args=[1])
        self.delete_todo_url = reverse('delete_todo', args=[1])
        self.task_create_url = reverse('task_create')
        self.task_todo_create_url = reverse('task_todo_create', args=[1])
        self.task_update_url = reverse('task_update', args=[1])
        self.task_delete_url = reverse('task_delete', args=[1])
        self.reminder_add_url = reverse('reminder_add', args=[1])
        self.reminder_update_url = reverse('reminder_update', args=[1])
        self.reminder_delete_url = reverse('reminder_delete', args=[1])
        self.search_tasks_url = reverse('search_tasks')
        self.search_todos_url = reverse('search_todos')
        self.search_users_url = reverse('search_users')


    def test_project_home_GET(self):
        client = Client()

        response = client.get(self.home_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base_generic.html')


    def test_project_user_GET(self):
        client = Client()

        response = client.get(self.user_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/user_list.html')


    def test_project_users_GET(self):
        client = Client()

        response = client.get(self.users_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/user_list.html')

    
    def test_project_todos_GET(self):
        client = Client()

        response = client.get(self.todos_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/todo_list.html')

    
    def test_project_user_todos_GET(self):
        client = Client()

        response = client.get(self.user_todos_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/todo_list.html')

    
    def test_project_tasks_GET(self):
        client = Client()

        response = client.get(self.tasks_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/task_list.html')

    
    def test_project_reminders_GET(self):
        client = Client()

        response = client.get(self.reminders_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/reminder_list.html')

    
    def test_project_register_GET(self):
        client = Client()

        response = client.get(self.register_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/register.html')

    
    def test_project_add_user_GET(self):
        client = Client()
        response = client.get(self.add_user_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/add_user.html')


    def test_project_add_todo_GET(self):
        client = Client()
        response = client.get(self.add_todo_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/add_todo.html')


    def test_project_task_create_GET(self):
        client = Client()
        response = client.get(self.task_create_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/add_task.html')

    
    def test_project_search_tasks_GET(self):
        client = Client()
        response = client.get(self.search_tasks_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/search_task.html')


    def test_project_search_todos_GET(self):
        client = Client()
        response = client.get(self.search_todos_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/search_todo.html')

    
    def test_project_search_users_GET(self):
        client = Client()
        response = client.get(self.search_users_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/search_user.html')


class Testmodels(TestCase):

    def setUp(self):
        self.some_time = timezone.now()

        self.user1 = User.objects.create(
            user_name = "some-name",
            user_surname = "some-surname",
            user_email = "some-email",
            user_join_time = self.some_time
        )

        self.todo1 = Todo.objects.create(
            todo_name = "some-name",
            todo_created = self.some_time
        )
        self.todo1.todo_users.set([self.user1])

        self.reminder1 = Reminder.objects.create(
            reminder_time = self.some_time,
            reminder_sound = True,
            reminder_vibrate = True
        )

        self.task1 = Task.objects.create(
            task_name = "some-name",
            task_completed = True,
            task_todo = self.todo1,
            task_time = self.some_time,
            task_reminder = self.reminder1
        )


    def test_user(self):
        self.assertEquals(self.user1.user_name, "some-name")
        self.assertEquals(self.user1.user_surname, "some-surname")
        self.assertEquals(self.user1.user_email, "some-email")
        self.assertEquals(self.user1.user_join_time, self.some_time)


    def test_todo(self):
        self.assertEquals(self.todo1.todo_name, "some-name")
        self.assertEquals(self.todo1.todo_users.first(), self.user1)
        self.assertEquals(self.todo1.todo_created, self.some_time)

    
    def test_reminder(self):
        self.assertEquals(self.reminder1.reminder_time, self.some_time)
        self.assertEquals(self.reminder1.reminder_sound, True)
        self.assertEquals(self.reminder1.reminder_vibrate, True)

    
    def test_task(self):
        self.assertEquals(self.task1.task_name, "some-name")
        self.assertEquals(self.task1.task_completed, True)
        self.assertEquals(self.task1.task_todo, self.todo1)
        self.assertEquals(self.task1.task_time, self.some_time)
        self.assertEquals(self.task1.task_reminder, self.reminder1)