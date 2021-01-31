from sqlalchemy import (
    Table, Text, Integer, VARCHAR, MetaData, Column
)

meta = MetaData()
post = Table(
    'post', meta,
    Column('id', Integer, primary_key=True),
    Column('title', VARCHAR, nullable=True),
    Column('body', Text,)
)