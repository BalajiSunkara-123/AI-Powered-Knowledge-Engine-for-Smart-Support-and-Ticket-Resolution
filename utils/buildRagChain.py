import os,sys
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain

CHAT_MODEL=os.environ.get("CHAT_MODEL") or sys.exit('Unable to load CHAT_MODEL from local Environment')
TEMPERATURE=os.environ.get("TEMPERATURE") or sys.exit('Unable to load TEMPERATURE from local Environment')
def make_rag_chain(retriver):
    prompt=ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are a concise, careful assistant. Answer ONLY from the provided context."
                "If the answer is not in context, say you don't know. "
                "Cite sources by filename and, if present, page."
             ),
             ("human","Question:\n{input}\n\nContext:\n{context}"),
        ]
    )

    llm=ChatGoogleGenerativeAI(model=CHAT_MODEL,temperature=TEMPERATURE)

    doc_chain=create_stuff_documents_chain(llm,prompt)
    rag_chain=create_retrieval_chain(retriver,doc_chain)

    return rag_chain
