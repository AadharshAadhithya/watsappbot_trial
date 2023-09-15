## Whatsapp Trial Chatbot with Twilio

To quickly try the bot, here are the steps to follow
1) Make sure you have NGROK and Docker installed locally
2) Pull the image from dockerhub `docker pull aadharsh/watsapp_bot_trial:latest`
3) run the container locally `docker run -p 8000:8000 aadharsh/watsapp_bot_trial:latest`
4) Expose port 8000 using NGROK. `./ngrok http 8000`
5) Create Twilio account and configure sandbox. In the sandbox settings, configure the `on message comes in` link to
`<your ngork link>/bot`. for example, `https://0256-115-111-177-226.ngrok-free.app/bot`
6) Join sandbox from whatsapp and test the bot.