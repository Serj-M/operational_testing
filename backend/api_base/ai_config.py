import os
from typing_extensions import TypedDict
from langchain.chat_models import init_chat_model
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv


load_dotenv()


LANGSMITH_API_KEY = os.getenv("LANGSMITH_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
PROXY_CONNECT = os.getenv("PROXY_CONNECT")


if (not os.environ.get("LANGSMITH_TRACING") 
    or not os.environ.get("LANGSMITH_API_KEY") 
    or not os.environ.get("LANGSMITH_ENDPOINT") 
    or not os.environ.get("LANGSMITH_PROJECT")
):
    os.environ["LANGSMITH_TRACING"] = "true"
    os.environ["LANGSMITH_API_KEY"] = LANGSMITH_API_KEY
    os.environ["LANGSMITH_ENDPOINT"] = "https://api.smith.langchain.com"
    os.environ["LANGSMITH_PROJECT"] = "operational_testing"


llm = init_chat_model("gpt-4o-mini", model_provider="openai")
llm = ChatOpenAI(
    temperature=0,
    model_name="gpt-4o-mini",
    streaming=True,
    openai_api_key=OPENAI_API_KEY,
    openai_proxy=PROXY_CONNECT,
)
