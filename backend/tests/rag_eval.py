from ragas.dataset_schema import SingleTurnSample
question = "What framework does Kestrel use for its backend?"
retrieved_contexts = ["Kestrel uses fastAPI framework for the backend."]
response = "It uses fastAPI framework."
reference = "fastAPI"
sample = SingleTurnSample(
    user_input=question,
    retrieved_contexts=retrieved_contexts,
    response=response,
    reference=reference
)