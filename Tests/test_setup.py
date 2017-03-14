from flask_testing import TestCase
import json
from app import create_app, db, api
from app.views import LoginUser, RegisterUser,BucketAction, EntryAction
from app.models import User,Bucketlist,Entry

class BaseTestClass(TestCase):
    "Test for testing the base case configuration"

    def create_app(self):
        # Instanciatin the applicateion
        app = create_app("Testing")
        return app

    def setUp(self):
        self.app = self.create_app().test_client()
        db.create_all()
        # defining the type of JSOn that is being passed
        self.mime_type = "application/json"

        #  Adding route resources for testing the information flow of the application
        api.add_resource(LoginUser,"/auth/login", endpoint="token")
        api.add_resource(RegisterUser,"/auth/register", endpoint ="register")
        api.add_resource(BucketAction, "/bucketlists","/bucketlists/<id>", endpoint="bucketlist")
        api.add_resource(EntryAction,"/bucketlists/<id>/entry","/bucketlists/<id>/entries/<entry_id>", endpoint="entries")

        # Registring a dummy user for testing
        details = json.dumps({"username":"sammy","password":"swanjala","email":"swanjala009@example.com"})

        self.app.post("api/v1/auth/register", data = details, content_type=self.mime_type)

        # Dealing with the response data requested by user
        response = self.app.post("/api/v1/auth/login", data= details,content_type=self.mime_type)
        response_data = json.loads(response.data)
        self.token = "Bearer " + response_data["token"]
        self.header = {"Authorization": self.token}

        # Creating a sample bucketlist for testing
        name = json.dumps({"name":"bucket_test_list"})
        self.app.post("/api/v1/bucketlists", data= name, headers= self.header,
                content_type= self.mime_type)

        # Creting a dummy backet list entry for testing
        bucket_list_entry = json.dumps({"name":"testlist"})

        self.app.post("/api/v1/bucketlists/1/entries",data=bucket_list_entry,headers=self.header, content_type=self.mime_type)

        def tearDown(self):
            """Destroys all contents of the testing database that has been created during testing"""
            db.session.remove()
            db.drop_all()
