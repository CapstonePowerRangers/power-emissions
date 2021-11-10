import sqlalchemy

class Database:
    # Create SQL database connection object
    def __init__(self):
        self.host = "sg1-ss19.a2hosting.com"
        self.port = "5432"
        self.db = "madsahos_capstone2021fall"
        self.name = "madsahos_capstone2021co2"
        self.pw = "FQU2kSfSoCo9mFJmGstvEa5HD1gSqPhh3b3vqU0yOoRk2L61wjKQcuqyB5Vs"
        self.config = f"postgresql://{self.name}:{self.pw}@{self.host}:{self.port}/{self.db}"
        self.engine = sqlalchemy.create_engine(self.config)
        self.connection = self.engine.connect()
        self.metadata = sqlalchemy.MetaData()
