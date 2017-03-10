from Tests.test_setup import BaseTestClass
from app.models import User, bucket_name, bucket_list_entry

import json

class list_entry_test(BaseTestClass):
    """ Testing operations on bucket_list entries """

    def test_add_entry(self):
        "Test for adding an entry successfully"

        # Querying the initial and final counts of the entries
        initial_count = bucket_list_entry.query.count()

        entry_name = json.dumps({"name":"Rock Climbing"})
        response = self.app.post("/api/v1/bucketlists/23/items",
                                    data= entry_name, headers=self.header, content_type=self.mime_type)
        response_data =json.loads(response.data)

        response_control = self.app.post("/api/v1/bucketlists/23/items",data= entry_name, headers=self.header, content_type=self.mime_type)
        response_control_data = json.loads(response_control.data)

        second_count = Item.query.count()

        # Running asserts

        self.assertEqual(1,second_count-intial_count)
        self.assertListEqual([201,404], [response.status_code,response_control.status_code])
        self.assertIn("The Bucketlist cannot be found",response_control_data["message"])
        self.assertEqual("Entry successfully added to the list",response_data["message"])
