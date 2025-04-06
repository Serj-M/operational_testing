from langgraph.graph import START, StateGraph
from langchain.prompts import PromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage

from backend.api_base.ai_config import llm



async def handler_question(human_message: str) -> str:
    # graph_builder = StateGraph(State).add_sequence([generate])
    # graph_builder.add_edge(START, "generate")
    # graph = graph_builder.compile()

    # result = await graph.ainvoke({"question": human_message})
    # return result["answer"]

    messages = [
        SystemMessage("Translate the following from English into Italian"),
        HumanMessage("hi!"),
    ]
    result = llm.invoke(messages)
    print(f"Result: {result}")
    return 'ok'


# def generate(state: State):
#     template: str = get_template()
#     print(f"Prompt: {template}")
#     preamble: PromptTemplate = PromptTemplate.from_template(template)
#     messages = preamble.invoke({"question": state["question"]})
#     response = llm.invoke(messages)
#     return {"answer": response.content}
