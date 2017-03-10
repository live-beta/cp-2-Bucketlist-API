from flask_testing import TestCase
import json
from app import create_app,db,api
from app.views import LoginUser, RegisterUser,BucketAction, ItemAction
from app.models import User,Bucketlist,Item

class BaseTestClass(TestCase):
    "Test for testing the base case configuration"

    def create_app(self):
        # Instanciatin the applicateion
        app= create_app("Testing")
        return app

    def setUp(self):
        self.app = self.create_app().test_client()
        db.create_all()
        # defining the type of JSOn that is being passed
        self.mime_type = "application/json"

        #  Adding route resources for testing the information flow of the application
        api.add_resource(LoginUser,"/auth/login", endpoint="token")
        api.add_resource(RegisterUser,"/auth/register", endpoint ="register")
        api.add_resource(BucketAction, "/bucketlists","/bucketlists/<id>", endpoint="items")

        # Registring a dummy user for testing
        details = json.dumps({"username":"sammy","password":"swanjala","email":"swanjala009@example.com"})
        self.app.post("api/v1/auth/register", data = reg, content_type=self.mime_type)

        reg = json.dumps({"username":"vivian","password":"vnash","email":"vivnash@example.com"})
        self.app.post("api/v1/auth/register",data=reg, content_type =self.mime_type)

        # Dealing with the response data requested by user
        response = self.app.post("/api/v1/auth/login", data= deatils,content_type=self.mime_type)
        response_data = json.loads(response.data)
        self.token = "Bearer " + response_data["token"]
        self.header = {"Authorization": self.token}

        # Creating a sample bucketlist for testing
        bucket_name = json.dumps({"name":"bucket_test_list"})
        self.app.post("/api/v1/bucketlists", data= bucket_name, headers= self.header,
                content_type= self.mime_type)

        # Creting a dummy backet list entry for testing
        bucket_list_entry = json.dumps({"name":"testlist"})
        self.app.post("/api/v1/bucketlists/1/items",data=iname,headers=self.header, content_type=self.mime_type)

        def tearDown(self):
            """Destroys all contents of the testing database that has been created during testing"""
            db.session.remove()
            db.drop_all()
