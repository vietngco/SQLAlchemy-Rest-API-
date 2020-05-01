from flask_restful import Resource, reqparse
from models.user import UserModel as User

class UserRegister(Resource): # /register
    parser = reqparse.RequestParser()
    parser.add_argument('username', 
        type = str, 
        required = True,
        help = 'this can not be left empty'
        )
    parser.add_argument('password', 
        type = str,
        required = True,
        help = 'this can not be left empty'
    )
    def post(self):
        data = UserRegister.parser.parse_args()
        new_user = User.find_by_username(data['username'])
        if new_user:
            return {'message': f"This username {data['username']} has been existed"}
        else:
            new_user = User(**data) # unpack the data (dictionary), take the value of each key
            new_user.save_to_db()
            return {'message': "new user created successfully "}
        
class USERS(Resource):
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * from users"
        rows = cursor.execute(query)
        users = []
        for i,row in enumerate(rows):
            users.append( {'name': row[1], 'price': row[2]})
        return {'users': users}