from __future__ import unicode_literals
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import TextMessage
import configparser
from linebot.models import (
    MessageEvent,
    TextSendMessage,
    TemplateSendMessage,
    ImageCarouselColumn,
    ImageCarouselTemplate,
    PostbackTemplateAction
)

from youtube_crawler import stream_check
from db_crud import *

app = Flask(__name__)

config = configparser.ConfigParser()
config.read('config.ini')
line_bot_api = LineBotApi(config.get('line-bot', 'channel_access_token'))
handler = WebhookHandler(config.get('line-bot', 'channel_secret'))

members = ['Watson Amelia', "Ninomae Ina'nis", 'Gawr Gura', 'Mori Calliope', 'Takanashi Kiara']

ame_gif = 'https://walfiegif.files.wordpress.com/2021/09/out-transparent-1.gif?w=1000'
gura_gif = 'https://walfiegif.files.wordpress.com/2021/09/out-transparent-2.gif?w=1000'
ina_gif = 'https://walfiegif.files.wordpress.com/2021/09/out-transparent-3.gif?w=1000'
kiara_gif = 'https://walfiegif.files.wordpress.com/2021/09/out-transparent-4.gif?w=1000'
mori_gif = 'https://walfiegif.files.wordpress.com/2021/09/out-transparent-5.gif?w=1000'


@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)

    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def echo(event):
    if event.source.user_id != "Udeadbeefdeadbeefdeadbeefdeadbeef":

        if event.message.text == 'Go':

            Image_Carousel = TemplateSendMessage(
                alt_text='目錄',
                template=ImageCarouselTemplate(
                    columns=[
                        ImageCarouselColumn(
                            image_url=gura_gif,
                            action=PostbackTemplateAction(
                                label='Gawr Gura',
                                text='Gawr Gura',
                                data='action=buy&itemid=1'
                            )
                        ),
                        ImageCarouselColumn(
                            image_url=ina_gif,
                            action=PostbackTemplateAction(
                                label="Ninomae Ina",
                                text="Ninomae Ina",
                                data='action=buy&itemid=2'
                            )
                        ),
                        ImageCarouselColumn(
                            image_url=ame_gif,
                            action=PostbackTemplateAction(
                                label='Amelia',
                                text='Watson Amelia',
                                data='action=buy&itemid=1'
                            )
                        ),
                        ImageCarouselColumn(
                            image_url=mori_gif,
                            action=PostbackTemplateAction(
                                label="Calliope",
                                text="Mori Calliope",
                                data='action=buy&itemid=2'
                            )
                        ),
                        ImageCarouselColumn(
                            image_url=kiara_gif,
                            action=PostbackTemplateAction(
                                label='Kiara',
                                text='Takanashi Kiara',
                                data='action=buy&itemid=1'
                            )
                        ),

                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token, Image_Carousel)

        elif event.message.text == 'Gawr Gura':

            status_code = check_stream('gura')

            if status_code:

                stream_title, live_url = stream_url_title('gura')

                res_arr = [TextSendMessage(text='Gura 開台中!'), TextSendMessage(text=live_url)]

                line_bot_api.reply_message(event.reply_token, res_arr)

            else:

                line_bot_api.reply_message(event.reply_token, TextSendMessage(text='Gura 關台中'))

        elif event.message.text == 'Watson Amelia':

            status_code = check_stream('ame')

            if status_code:

                stream_title, live_url = stream_url_title('ame')

                res_arr = [TextSendMessage(text='Watson 開台中:'), TextSendMessage(text=live_url)]

                line_bot_api.reply_message(event.reply_token, res_arr)

            else:

                line_bot_api.reply_message(event.reply_token, TextSendMessage(text='Ame 關台中'))

        elif event.message.text == "Ninomae Ina":

            status_code = check_stream('ina')

            if status_code:

                stream_title, live_url = stream_url_title('ina')

                res_arr = [TextSendMessage(text='Ina 開台中'), TextSendMessage(text=live_url)]

                line_bot_api.reply_message(event.reply_token, res_arr)

            else:

                line_bot_api.reply_message(event.reply_token, TextSendMessage(text='Ina 關台中'))

        elif event.message.text == "Mori Calliope":

            status_code = check_stream('cali')

            if status_code:

                stream_title, live_url = stream_url_title('cali')

                res_arr = [TextSendMessage(text='Calli 開台中'), TextSendMessage(text=live_url)]

                line_bot_api.reply_message(event.reply_token, res_arr)

            else:

                line_bot_api.reply_message(event.reply_token, TextSendMessage(text='Calli 關台中'))

        elif event.message.text == "Takanashi Kiara":

            status_code = check_stream('kiara')

            if status_code:

                stream_title, live_url = stream_url_title('kiara')

                res_arr = [TextSendMessage(text='Kiara 開台中!'),TextSendMessage(text=live_url) ]

                line_bot_api.reply_message(event.reply_token, res_arr)

            else:

                line_bot_api.reply_message(event.reply_token, TextSendMessage(text='Kiara 關台中'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
