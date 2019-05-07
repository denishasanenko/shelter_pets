from sqlalchemy import Column, String, Table, MetaData
from sqlalchemy.dialects.postgresql import UUID
import uuid

metadata = MetaData()
Shelter = Table(
    'shelters',
    metadata,
    Column('shelter_uuid', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4()),
    Column('name', String(50), nullable=False),
    Column('description', String(200))
)
