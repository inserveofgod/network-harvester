import requests as req
import datetime


def connect(address: str) -> bool:
    try:
        header_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
                        'referer': address}
        uri = req.post(address, headers=header_agent)
        print(uri.status_code)

        if uri.status_code < 403:
            return True

    except req.ConnectTimeout:
        print("Connection timed out with this URL!")

    except req.ConnectionError:
        print("Provided URL is not found!")
    return False


url = input("Enter URL : ")
file = input("Provide any file to perform dictionary attack : ")
funds = []
no_funds = []

if connect(url):
    try:
        with open(file) as f:
            for line in f:
                link = url + '/' + line.replace('\n', '')
                print("Working on {} --- {}".format(link, datetime.datetime.now()))

                if connect(link):
                    funds.append(link)
                else:
                    no_funds.append(link)

            if funds:
                print("\n")
                print("-"*30)
                print("\n")
                print("We found these links : ")

                for fund in funds:
                    print("[+]", fund)

            if no_funds:
                print("\n")
                print("-"*30)
                print("\n")
                print("These links are not valid : ")

                for no_fund in no_funds:
                    print("[!]", no_fund)

    except FileNotFoundError:
        print("File is not found!")
        exit(-1)

    except PermissionError:
        print("Permission denied for this file!")
        exit(-1)

else:
    print("We could not connect to {}".format(url))
