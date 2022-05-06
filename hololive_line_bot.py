from __future__ import unicode_literals
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import configparser
import random


app = Flask(__name__)


class LineBot:

    config = configparser.ConfigParser()
    config.read('config.ini')
    line_bot_api = LineBotApi(config.get('line-bot', 'channel_access_token'))
    handler = WebhookHandler(config.get('line-bot', 'channel_secret'))

    @classmethod
    @app.route("/callback", methods=['POST'])
    def callback(cls):
        signature = request.headers['X-Line-Signature']
        body = request.get_data(as_text=True)
        app.logger.info("Request body: " + body)
        try:
            print(body, signature)
            cls.handler.handle(body, signature)

        except InvalidSignatureError:
            abort(400)

        return 'OK'

    @classmethod
    @handler.add(MessageEvent, message=TextMessage)
    def echo(cls, event):

        if event.source.user_id != "Udeadbeefdeadbeefdeadbeefdeadbeef":

            # Phoebe 愛唱歌
            pretty_note = '♫♪♬'
            pretty_text = ''

            if event.message.text == '我':
                cls.line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text="yu chen is gay")
                )
            else:

                for i in event.message.text:
                    pretty_text += i
                    pretty_text += random.choice(pretty_note)

                cls.line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=pretty_text)
                )


if __name__ == "__main__":

    app.run(host='0.0.0.0', port=5001, debug=True)