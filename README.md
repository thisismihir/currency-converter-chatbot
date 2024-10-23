## currency-converter-chatbot

- Step 1: Create an account with DialogFlow
- Step 2: Set up new Intent by setting up Training Phases as in which all ways conversions can be asked, assign the two different currency codes as tags. 
This can be enhanced more by giving the chatbot personalities by answering the tags in the small talk section.
- Step 3: Download ngrok and take API key from https://freecurrencyapi.com/.
Create a Flask API given in the repo and place the API key there. Run the query.
Note: Make sure you've tested your chatbot and it's functioning.
- Step 4: Run the `ngrok config add-authtoken [API_KEY]` first and then `ngrok http 5000`.
You're good to run the chatbot and once done with it. Your chatbot is ready!
- Step 5: Host the chatbot on Telegram for instance by setting up new chatbot in BotFather and then adding the Key present there in the DialogFlow platform and you're good to go.

In case of any queries, do raise an issue and I'd be happy to help.
Looking forward to many such applications. Open to Ideas.

This helps create a chatbot which can be hosted live on Telegram and other platforms as well.
