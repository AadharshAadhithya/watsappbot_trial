from flask import Flask,request
from twilio.twiml.messaging_response import MessagingResponse
from llm import get_gpt_response

app = Flask(__name__)


@app.route("/home",methods=["GET"])
def home():
    return {"message": "Up and running"}

@app.route("/bot",methods=["POST"])
def bot():
    incoming_msg = request.values.get("Body","")
    phone_number = request.values.get("From", "")
    message_response = get_gpt_response(incoming_msg,phone_number)
    

    resp = MessagingResponse()
    msg = resp.message()
    msg.body(message_response)
    return str(resp)


if __name__ == "__main__":
    app.run(port=4000)