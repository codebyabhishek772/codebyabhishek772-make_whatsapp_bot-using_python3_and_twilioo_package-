from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    if 'quote' in incoming_msg:
        # return a quote
        r = requests.get('https://api.quotable.io/random')
        if r.status_code == 200:
            data = r.json()
            quote = f'{data["content"]} ({data["author"]})'
        else:
            quote = 'I could not retrieve a quote at this time, sorry.'
        msg.body(quote)
        responded = True
    if 'Hii' in incoming_msg:
        # return a cat pic
        msg.body('Hi Buddy I am vega bot made by ABHISHEK BISWAS OF WEST BENGAL')
        responded = True
    if not responded:
        msg.body('sorry! I could not get you please repeat or use different keyword of same meaning')
    return str(resp)


if __name__ == '__main__':
    app.run()
