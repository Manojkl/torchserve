from locust import HttpUser, task


class FastAPIUser(HttpUser):
    @task
    def get_root(self):
        self.client.get("/")

    @task
    def get_items(self):
        self.client.get("/items")
