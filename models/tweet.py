from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.sql.sqltypes import Integer, String, DateTime
from config.db import meta, engine
from datetime import datetime

tweets = Table("tweets", meta, Column("id", Integer, primary_key=True), 
            Column("content", String(255)),
            Column("created_at", DateTime(timezone=True)),
            Column("by", Integer, ForeignKey("users.id")))

meta.create_all(engine)