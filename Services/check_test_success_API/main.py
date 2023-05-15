from flask import Flask
from flask_restful import Resource, Api, abort
from flask_cors import CORS
import check_test_success_script as cts

app = Flask(__name__)
api = Api(app)
CORS(app)

tests = {"test0", "test1", "test2", "test3", "test4", "test5"}

def abort_if_test_doesnt_exist(test_id):
    if test_id not in tests:
        abort(404, message="404! Test {} doesn't exist".format(test_id))

class CheckTestSuccess(Resource):
    def get(self, test_id):
        abort_if_test_doesnt_exist(test_id)
        return {"TestName" : test_id, "Response": cts.check_test_success(test_id)}

api.add_resource(CheckTestSuccess, '/check_test_success/<string:test_id>')

if __name__ == '__main__':
    app.run(debug=True)
