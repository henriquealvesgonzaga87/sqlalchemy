from main import engine
from models.base import Model
from models.user import *

Model.metadata.create_all(engine)
