from models.user import UserModel as User



def authenticate(username, password): # \auth
    user = User.find_by_username(username) 
    if user and (user.password == password):
        return user # get the key 

def identity(payload): # payload is token
    user_id = payload['identity'] 
    return User.find_by_id(user_id) 