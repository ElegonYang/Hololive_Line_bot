import requests
from flask import Flask, request

app = Flask(__name__)

'''
使用者訂閱網址：
https://notify-bot.line.me/oauth/authorize?response_type=code&client_id=2BfD1zVZALM2ZUuJ83adLW&redirect_uri=https://2ca4-2001-b011-2005-e88d-444a-80b0-dd5e-67e3.jp.ngrok.io&scope=notify&state=NO_STATE
'''


def getNotifyToken(AuthorizeCode):
    body = {
        "grant_type": "authorization_code",
        "code": AuthorizeCode,
        "redirect_uri": 'https://2ca4-2001-b011-2005-e88d-444a-80b0-dd5e-67e3.jp.ngrok.io',
        "client_id": '2BfD1zVZALM2ZUuJ83adLW',
        "client_secret": '2NRwpYEQzQmj6BLeKolS8BvvgisSDTtCQc7G0APlF7a'
    }
    r = requests.post("https://notify-bot.line.me/oauth/token", data=body)
    return r.json()["access_token"]


def lineNotifyMessage(token, msg):
    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    payload = {'message': msg}
    r = requests.post("https://notify-api.line.me/api/notify", headers=headers, data=payload)
    return r.status_code

# 1oaGORmn1lfwqXCY9bhSy865mQQD149glzSRBAWB4HG
# hF056xoezcqGQScCnOhwHmix64q9V358vOlUVAo8FZ0
# mmYXx8gejUEjXTfjM1XjOL9MpTIaA0TOaELLF7pouht


@app.route('/', methods=['POST', 'GET'])
def hello_world():
    authorizeCode = request.args.get('code')
    token = getNotifyToken(authorizeCode)
    print(token)
    lineNotifyMessage(token, "恭喜!!!!!!!連動完成")
    return f"恭喜你，連動完成"


if __name__ == '__main__':
    lineNotifyMessage("mmYXx8gejUEjXTfjM1XjOL9MpTIaA0TOaELLF7pouht", "蕉流一下!")
    app.debug = True
    app.run(port=5004)
