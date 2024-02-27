from main import session
from models.user import User

user = User.query.first()

session.delete(user)
session.commit()
