import requests
fetchURL = "https://script.google.com/macros/s/AKfycby1jPcLUng-UMQyvwOnqwbkIBh5zDg2ysIVihHHK9XWqSZbwXk/exec"
def postData():
    serchperson = input()
    url = fetchURL+"?text="+serchperson
    r = requests.get(url)
    data = list(map(str,r.text.split(",")))
    for i in range(len(data)):
        print(data[i])    

if __name__ == "__main__":
    postData()