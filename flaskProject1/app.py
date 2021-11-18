from flask import Flask, jsonify

app = Flask(__name__)
users = [
      {
        "userid": 1,
        "name": "Leanne Graham",
        "username": "Bret",
        "email": "Sincere@april.biz"
    },
    {
        "userid": 2,
        "name": "Leanne Graham",
        "username": "Bret",
        "email": "Sincere@april.biz"
    },
    {
        "userid": 3,
        "name": "Leanne Graham",
        "username": "Bret",
        "email": "Sincere@april.biz"
    },
    {
        "userid": 4,
        "name": "Leanne Graham",
        "username": "Bret",
        "email": "Sincere@april.biz"
    },
    {
        "userid": 5,
        "name": "Leanne Graham",
        "username": "Bret",
        "email": "Sincere@april.biz"
    }

]


@app.route('/')
def index():
    return 'Welcome first python api!'


@app.route('/users', methods=['GET'])
def get():
    return jsonify({'users': users})


@app.route('/users/<int:userid>', methods=['GET'])
def get_user(userid):
    return jsonify({'user': users[userid]})


@app.route('/users', methods=['POST'])
def create():
    user = {
        "userid": 6,
        "name": "Clementina DuBuque",
        "username": "Moriah.Stanton",
        "email": "Rey.Padberg@karina.biz"
    }
    users.append(user)
    return jsonify({'created': user})


@app.route('/users/<int:userid>', methods=['PUT'])
def user_update(userid):
    users[userid]['name'] = "xxxx"
    return jsonify({'user': users[userid]})


@app.route('/users/<int:userid>', methods=['DELETE'])
def delete(userid):
    users.remove(users[userid])
    return jsonify({'result': True})


if __name__ == '__main__':
    app.run(debug=True)
