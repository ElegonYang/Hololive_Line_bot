import requests


def go():

    a = 100
    if a< 500:  # 將爬取的價格字串轉型為整數
        headers = {
            "Authorization": "Bearer " + "GQOxLdLdvSwedE5ZCMKcrgQxqiUdus2jgflDPBj9JWT",
            "Content-Type": "application/x-www-form-urlencoded"
        }

        params = {"message": "a test"}

        r = requests.post("https://notify-api.line.me/api/notify",
                          headers=headers, params=params)
        print(r.status_code)  # 200

go()
