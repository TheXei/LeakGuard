from flask import Flask
from flask_restful import Resource, Api, abort
import check_test_success_script as check_test_success

app = Flask(__name__)
api = Api(app)

tests = {"test0", "test1", "test2", "test3", "test4", "test5"}

def abort_if_test_doesnt_exist(test_id):
    if test_id not in tests:
        abort(404, message="Test {} doesn't exist".format(test_id))

class CheckTestSuccess(Resource):
    def get(self, test_id):
        abort_if_test_doesnt_exist(test_id)
        return {"TestName" : test_id, "Response": check_test_success.check_test_success(test_id)}

api.add_resource(CheckTestSuccess, '/check_test_success/<string:test_id>')

if __name__ == '__main__':
    app.run(debug=True)
