from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base
# To create tables in the db
from models.patient import Patient
from models.encounter import Encounter
from models.observation import Observation
from models.procedure import Procedure

from settings import config


engine = create_engine(
    'postgresql+psycopg2://'
    f'{config("USER_DB")}:{config("PASS_DB")}@'
    f'{config("HOST_DB")}:{config("PORT_DB")}/{config("DB_NAME")}'
)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
