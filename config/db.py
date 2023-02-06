from sqlalchemy import create_engine, MetaData

meta = MetaData()

engine = create_engine("mysql+pymysql://root:09052002@localhost:3306/storedb")
connection = engine.connect()