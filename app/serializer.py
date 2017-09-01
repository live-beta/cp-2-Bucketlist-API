from flask_restful import fields

# conversion of model attributes to fields

Itemformat = {"id": fields.Integer,
              "name": fields.String,
              "date_created": fields.DateTime(dt_format = "rfc822"),
              "date_modified": fields.DateTime(dt_format="rfc822"),
              "done": fields.Boolean(attribute="status")

}

bucketlistformat ={"id": fields.Integer,
                    "name": fields.String,
                    "items":fields.List(fields.Nested(Itemformat)),
                    "date_created": fields.DateTime(),
                    "date_modified": fields.DateTime(),
                    "creator": fields.String(attribute="user.username")}
