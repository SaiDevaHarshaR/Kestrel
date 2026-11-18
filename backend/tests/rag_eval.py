from ragas.dataset_schema import SingleTurnSample
from ragas.metrics.collections import AnswerRelevancy, Faithfulness, ContextPrecision
from ..app.core.config import settings
from ragas.llms import llm_factory
from google import genai
from ragas.embeddings import GoogleEmbeddings

client = genai.Client(api_key=settings.gemini_api_key.get_secret_value(),)
embeddings = GoogleEmbeddings(client=client, model="gemini-embedding-001")

question = "What framework does Kestrel use for its backend?"
retrieved_contexts = ["Kestrel uses FastAPI framework for the backend."]
response = "It uses FastAPI framework."
reference = "FastAPI"

llm = llm_factory("gemini-2.0-flash", provider="google", client=client)

scorer = AnswerRelevancy(llm=llm, embeddings=embeddings)
result = await scorer.ascore(
    user_input="What backend framework did Kestrel use?",
    response="Kestrel uses FastAPI framework.",
)
print(f"Answer Relevancy Score: {result.value}")


scorerCP = ContextPrecision(llm=llm)
resultCP = await scorerCP.ascore(
    user_input="What vectorDB does Kestrel use?",
    reference="Kestrel uses ChromaDB.",
    retrieved_contexts=[
        "Kestrel uses ChromaDB as a vector database.",
        "Kestrel uses FastAPI framweork fro backend.",
    ],
)
print(f"Context Precision Score: {resultCP.value}")

scorerF = Faithfulness(llm=llm)
resultF = await scorerF.ascore(
    user_input="What does Kestrel use for agent tool calling?",
    response="Kestrel uses LangGraph for agent tool calling.",
    retrieved_contexts=[
        "Kestrel uses LangGraph for agent tool calling, and it has technical_agent to answer about technical questions and general_agent which answers questions about general queries"
    ],
)
print(f"Faithfulness Score: {resultF.value}")


sample = SingleTurnSample(
    user_input=question,
    retrieved_contexts=retrieved_contexts,
    response=response,
    reference=reference
)

async def evaluate_sample(sample: SingleTurnSample):
    ans = await scorerF.ascore(user_input = sample.user_input,response = sample.response,retrieved_contexts = sample.retrieved_contexts)
    ans1 = await scorerCP.ascore(user_input = sample.user_input,retrieved_contexts = sample.retrieved_contexts, reference = sample.reference)
    ans2 = await scorer.ascore(user_input = sample.user_input,response = sample.response)
    return {
    "faithfulness": ans.value,
    "context_precision": ans1.value,
    "answer_relevancy": ans2.value
}
scores = await evaluate_sample(sample)
print(scores)