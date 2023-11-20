from core.rest_client import RestClient


class Api(RestClient):
    def __init__(self):
        super().__init__()

    def get_mobile_belong(self, **kwargs):
        return self.get("/shouji1/query", **kwargs)

    def post_data(self, **kwargs):
        return self.post("/posts", **kwargs)

    # 项目实战方法
    def get_code(self, **kwargs):
        return self.post("/code/", **kwargs)

    def register_mobile(self, **kwargs):
        return self.post("/users/", **kwargs)

    def user_login(self, **kwargs):
        return self.post("/login/", **kwargs)

    def shopping_add(self, **kwargs):
        return self.post("/shopcarts/", **kwargs)

    def add_message(self, **kwargs):
        return self.post("/messages/", **kwargs)

    def banner(self, **kwargs):
        return self.get("/banners/", **kwargs)


api_util = Api()
