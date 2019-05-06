from marshmallow import Schema, fields, pprint

class SheltersSchema(Schema):
    shelter_uuid = fields.UUID()
    name = fields.Str()
    description = fields.Str()

shelter_chema = SheltersSchema()
shelters_chema = SheltersSchema(many=True)