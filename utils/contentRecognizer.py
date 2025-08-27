from groq import Groq
from dotenv import load_dotenv
import os
load_dotenv()

def categorizationBuilder(tc,categories:list):
    # tc=data.get("ticket_content")


    client = Groq(
        api_key=os.environ.get("GROQ_API_KEY"),
    )

    # chat_completion = client.chat.completions.create(
    #     messages=[
    #         {
    #             "role": "user",
    #             "content": "Explain the importance of fast language models",
    #         },{
    #             "role":"system",
    #             "content":"You are financial advisor"
    #         }
    #     ],
    #     model="openai/gpt-oss-20b",
    #     temperature=0.6,
    #     stream=False,
    # )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"""This is ticket content {tc}""",
            },{
                "role":"system",
                "content":f"""You are experienced ticket categorization analyst 
                           Based on the user's ticket content 
                           you will categorize the ticket 

                           Notes:
                           you will categorize from the mentioned categories

                           -only return category no nuance explaination
                           for example refund

                           return only the category that is present in {categories}

                """
            }
        ],
        model="llama-3.1-8b-instant",
        temperature=0.3,
        stream=False,
    )

    return chat_completion.choices[0].message.content
