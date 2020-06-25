# codebyabhishek772-make_whatsapp_bot-using_python3_and_twilioo_package-
make whatsapp bot using python 3.8 and twilioo package 

Before doing this project follow this command first

$ mkdir whatsapp-bot


$ cd whatsapp-bot


$ python3 -m venv whatsapp-bot-venv


$ source whatsapp-bot-venv/bin/activate


(whatsapp-bot-venv) $ pip install twilio flask requests


$ python bot.py


$ sudo apt install ngnix


$ ngrok http 5000


Go back to the Twilio Console, click on Programmable SMS, then on WhatsApp, and finally on Sandbox. Copy the https:// URL from the ngrok output and then paste it on the “When a message comes in” field. Since our chatbot is exposed under the /bot URL, append that at the end of the root ngrok URL. Make sure the request method is set to HTTP Post. Don’t forget to click the red Save button at the bottom of the page to record these changes.


Now you can start sending messages to the chatbot from the smartphone that you connected to the sandbox. You can type any sentences that you like, and each time the words “quote” and “cat” appear in messages the chatbot will invoke the third party APIs and return some fresh content to you. In case you missed it at the top of the article, here is an example session that I held with the chatbot:


thank you for more details contact abhishekbiswas772@gmil.com
