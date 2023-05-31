import requests

BASE = "http://127.0.0.1:5000/"

data = [{"test_id": "0"}, {"test_id": "1"}, {"test_id": "2"}, 
        {"test_id": "3"}, {"test_id": "4"}, {"test_id": "5"}, {"test_id": "6"}]

while True:
    usrInput = input("Which test would you like to run? Press enter to run all tests, or 0 through 6 to run a specific test, then press enter again. Or enter 'exit' to exit. ")
    if usrInput == "":
        for i in range(len(data)):
            response = requests.get(BASE + "check_test_success/test" + str(i))
            print(response.json())
    elif usrInput == "exit":
        exit()
    else:
        response = requests.get(BASE + "check_test_success/test" + usrInput)
        print(response.json())