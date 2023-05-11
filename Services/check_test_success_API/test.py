import requests

BASE = "http://127.0.0.1:5000/"

data = [{"test_id": "0"}, {"test_id": "1"}, {"test_id": "2"}, 
        {"test_id": "3"}, {"test_id": "4"}, {"test_id": "5"}, {"test_id": "6"}]

for i in range(len(data)):
    response = requests.get(BASE + "check_test_success/test" + str(i))
    print(response.json())

# response = requests.get(BASE + "check_test_success/test0")
# print(response.json())