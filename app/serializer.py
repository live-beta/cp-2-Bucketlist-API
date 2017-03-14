from flask_restful import fields

# conversion of model attributes to fields

Entryformat = {"id": fields.Integer,"name": fields.String,"date_created": fields.DateTime(dt_format = "rfc822"),
"date_modified": fields.DateTime(dt_format="rfc822"),
"done": fields.Boolean(attribute="status")

}

bucketlistformat ={"id":fields.Integer,
                    "name":fields.String,
                    "Entries":fields.List(fields.Nested(Entryformat)),
                    "date_created": fields.DateTime(),
                    "date_modified": fields.DateTime(),
                    "creator": fields.String(attribute="user.username")}
