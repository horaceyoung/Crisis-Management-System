from locust import HttpLocust, TaskSet, task

class UserActions(TaskSet):

    def on_start(self):
        self.initialize()

    def initialize(self):
        # login to the application
        response = self.client.get('/')
        csrftoken = response.cookies['csrftoken']

    @task(1)
    def index(self):
        self.client.get('/')



    class ApplicationUser(HttpLocust):
        task_set = UserActions
        min_wait = 0
        max_wait = 0