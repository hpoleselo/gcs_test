

""" http://127.0.0.1:5000/

{
"field1": "Test1",
"field2": "Test2",
"field3": "Test3",
"field4": {
"field4_1": "Test4",
"field4_2": "Test5"
}
"""
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def parse_json():
    if request.method == 'POST' or request.method == 'GET':
        payload = request.get_json(silent=False)
        if payload['field1']:
            field1 = payload.get('field1')
        field2 = payload.get('field2')
        field3 = payload.get('field3')
        field4 = payload.get('field4')
        field4_1 = field4.get('field4_1')
        field4_2 = field4.get('field4_2')

        print(field1)
        print(field2)
        print(field3)
        print(field4)
        print(field4_1)
        print(field4_2)

        return jsonify(request.json)

    else:
        return 'Expecting GET or POST methods.', 405


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)