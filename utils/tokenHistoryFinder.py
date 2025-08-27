from groq import Groq
from dotenv import load_dotenv
from utils.sheets_utils import sheet
import os

load_dotenv()

def isTokenRepeated(token):
    sheet1=sheet()
    tokens=sheet1.col_values(2)
    tokens.pop(0)
    client=Groq(api_key=os.environ.get("GROQ_API_KEY"))

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"is this token {token} is similar to tokens present in {tokens}?",
            },{
                "role":"system",
                "content":"if the given token present or a similar kind of token present then return True along with the index of the token for example True, 0 else return False,-1"
            }
        ],
        model="openai/gpt-oss-20b",
        temperature=0.6,
        stream=False,
    )
    
    mssg=chat_completion.choices[0].message.content
    mssg=mssg.split(",")
    # print(mssg)
    if bool(mssg[0]):
        retToken=sheet1.row_values(int(mssg[1])+2)
        print("we have a simialr kind of question has been asked previously if you found it useful go through it!!")
        print("Question Raised : ",retToken[1])
        print("Date & Time : ",retToken[3],"Asked by :",retToken[4])
    return
    
    

# isTokenRepeated("i am facing trouble with my tablet")