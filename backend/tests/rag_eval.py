
import asyncio

import instructor
from openai import AsyncOpenAI
from google import genai

from ragas.dataset_schema import SingleTurnSample
from ragas.metrics.collections import (
    AnswerRelevancy,
    Faithfulness,
    ContextPrecision,
)
from ragas.llms import llm_factory
from ragas.embeddings import GoogleEmbeddings

from ..app.core.config import settings


# 1. API key
api_key = settings.gemini_api_key.get_secret_value()


# 2. Gemini embeddings client
embedding_client = genai.Client(api_key=api_key)

embeddings = GoogleEmbeddings(
    client=embedding_client,
    model="gemini-embedding-001",
)


# 3. Async Gemini evaluator client
llm_client = AsyncOpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

llm = llm_factory(
    model="gemini-3.8-flash",
    provider="openai",
    client=llm_client,
    adapter="instructor",
    mode=instructor.Mode.JSON,
)


# 4. Initialize metrics
scorer = AnswerRelevancy(
    llm=llm,
    embeddings=embeddings,
)

scorerF = Faithfulness(llm=llm)

scorerCP = ContextPrecision(llm=llm)


# 5. Evaluation sample
sample = SingleTurnSample(
    user_input="What framework does Kestrel use for its backend?",
    retrieved_contexts=[
        "Kestrel uses FastAPI framework for the backend."
    ],
    response="It uses FastAPI framework.",
    reference="FastAPI",
)


# 6. Reusable evaluation function
async def evaluate_sample(sample: SingleTurnSample):

    faithfulness = await scorerF.ascore(
        user_input=sample.user_input,
        response=sample.response,
        retrieved_contexts=sample.retrieved_contexts,
    )

    context_precision = await scorerCP.ascore(
        user_input=sample.user_input,
        retrieved_contexts=sample.retrieved_contexts,
        reference=sample.reference,
    )

    answer_relevancy = await scorer.ascore(
        user_input=sample.user_input,
        response=sample.response,
    )

    return {
        "faithfulness": faithfulness.value,
        "context_precision": context_precision.value,
        "answer_relevancy": answer_relevancy.value,
    }


# 7. Execute evaluation
async def main():
    try:
        scores = await evaluate_sample(sample)
        print("\nRAG Evaluation Results:")
        for metric, score in scores.items():
            print(f"{metric}: {score:.4f}")
    finally:
        await llm_client.close()


if __name__ == "__main__":
    asyncio.run(main())
