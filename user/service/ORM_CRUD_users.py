from db_connection import Session
from models import User
from sqlite3 import OperationalError, IntegrityError
from sqlalchemy.exc import IntegrityError



#Database Interface to allow server to manipulate db tables
#Returns the user or None
class DatabaseInterface:
    def __init__(self):
        pass


    #returns user or None
    def get_user(self, email):
        with Session() as session:
            try: 
                result = (session.query(User).filter(User.email == email).first())
                if result:
                    user = User(user_id=result.user_id, name=result.name, email=result.email, hashed_password=result.hashed_password)
                    return user
                else: 
                    return None
            except OperationalError as e:
                print('an error occured' + str(e))

    def get_user_by_id(self, user_id):
        with Session() as session:
            try: 
                result = (session.query(User).filter(User.user_id == user_id).first())
                if result:
                    user = User(user_id=result.user_id, name=result.name, email=result.email, hashed_password=result.hashed_password)
                    return user
                else: 
                    return None
            except OperationalError as e:
                print('an error occured' + str(e))


    #returns inserted user or None       
    def post_user(self, name, email, hashed_password):
        with Session() as session:
            try: 
                #Check if user already exists
                result = (session.query(User).filter(User.email == email).first())
                if result:
                    return None
                user = User(name=name, email=email, hashed_password=hashed_password)
                session.add(user)
                session.commit()
                user = self.get_user(email=email)
                return user
            except OperationalError as e:
                print('an error occured' + str(e))
            

    # Delete user with ID or email
    def delete_user(self, id=None, email=None):
        with Session() as session:
            try: 
                user = (session.query(User).filter(User.email == email).first())
                if user:
                    session.delete(user)
                    session.commit()
                    return user
                else: 
                    return 'not found'
            except Exception as e: 
                print('an error occured' + str(e))

    def test(self):
        with Session() as session:
            try: 
                result = (session.query(User).limit(2).all())
                print(result)
            except OperationalError as e:
                print('an error occured' + str(e))

     # Queries database users, first with ID, then with email. 
    # Returns  user or None
    def get_user_depr(self, id=None, email=None):
        with Session() as session:
            try: 
                result = (session.query(User).filter(User.user_id == id).first())
                if not result:
                    result = (session.query(User).filter(User.email == email).first())
                    if result:
                        user = User(user_id=result.user_id, name=result.name, email=result.email, hashed_password=result.hashed_password)
                        return user
                    else: 
                        return 'not found'

                user = User(user_id=result.user_id, name=result.name, email=result.email, hashed_password=result.hashed_password)
                return user
            except OperationalError as e:
                print('an error occured' + str(e))
    

    # Inserts new user into table
    def post_user_depr(self, name, email, hashed_password):
        with Session() as session:
            try: 
                user = User(name=name, email=email, hashed_password=hashed_password)
                session.add(user)
                session.commit()
                return self.get_user(email=email)
            except IntegrityError: 
                return 'user already exists'
            except OperationalError as e:
                print('an error occured' + str(e))
            
# Create:
#user = User(user_id=10, name='test_name', email='test_mail', hashed_password='$½¡@£#¤øæåÅØÆEOL')