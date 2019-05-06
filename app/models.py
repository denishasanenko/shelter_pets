from sqlalchemy import Column, String, Table, MetaData
from sqlalchemy.dialects.postgresql import UUID

metadata = MetaData()
Shelters = Table(
    'shelters',
    metadata,
    Column('shelter_uuid', UUID, primary_key=True),
    Column('name', String(50), nullable=False),
    Column('description', String(200))
)
