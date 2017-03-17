BucketList Application API

Problem Description
According to Merriam-Webster Dictionary,  a Bucket List is a list of things that one has not done beforebutwantstodo  before dying.
This is an application programming interface for an online Bucket List service using the Flask framework

Specifications for the API are shown below.

Functionality
POST /auth/login
Logs a user in
POST /auth/register
Register a user
POST /bucketlists/
Create a new bucket list
GET /bucketlists/
List all the created bucket lists
GET /bucketlists/<id>
Get single bucket list
PUT /bucketlists/<id>
Update this bucket list
DELETE /bucketlists/<id>
Delete this single bucket list
POST /bucketlists/<id>/items/
Create a new item in bucket list
PUT /bucketlists/<id>/items/<item_id>
Update a bucket list item
DELETE /bucketlists/<id>/items/<item_id>
