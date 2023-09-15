import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_APIKEY")

print(os.getenv("OPENAI_API_KEY"))


system_prompt = """
You are an assistant who texts all the customers and asks about the feedback of a product which is watch. Just have the below as an example and you have to talk in a similar way.
As a common procedure, this is the question you have to start with always.
Hey ! How are you doing? How is the product you recently purchased ?
You have to ask this only in the first convo and NOT in all messages.

Also take information from the user to understand about their problem. Ask if they have any problem or not.

If problem is there, tell that we will work on it and offer them a discount coupon of SORRY10 to avail 10% off on their next purchase.
If they dont have any problem, tell thank you for the purchase and ask them to visit again.

Finally, stop the convo and end it if they tell thank yoy or tell that they dont have any more concerns
"""

messages_ledger= {}


def get_gpt_response(prompt,ph_no):
    try:
        if prompt.lower() in ["quit", "exit", "thank you", "okay thanks", "bye"]:
            messages_ledger[ph_no]=[] #clear msgs cache
            return "Goodbye! have a wonderful day!"
        if ph_no not in messages_ledger.keys():
            messages_ledger[ph_no] = [
                {"role": "system", "content": system_prompt},
               {"role": "user", "content": prompt} 
            ]
        if ph_no in messages_ledger.keys():
            messages_ledger[ph_no].append({"role": "user", "content": prompt} )
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages = messages_ledger[ph_no]
             )
        
        response_text = response['choices'][0]['message']['content']
        messages_ledger[ph_no].append({"role": "assistant", "content": response_text})
        
        
        return response_text
    except Exception as e:
        return str(e)
    

