# Methodology

## Objective
Retrieve a supporting passage instead of inventing an answer when the corpus does not contain relevant evidence.

## Algorithm
Tokenize and count terms → rank by cosine similarity → apply threshold → return evidence or abstain.

## Interface
answer(question, documents, threshold=.2)

Inputs: A mapping from stable document IDs to text; threshold in [0,1].

Outputs: A verbatim passage, source ID, cosine score and abstention flag; no generated answer.

## Evaluation protocol
Compare coverage and retrieval precision on a labeled question–document corpus; tune threshold on a separate validation set.

Report test corpus provenance, exact revision, configuration, failures and uncertainty. The included regression tests are not a benchmark.

## Threats to validity
Lexical overlap is not entailment, semantic similarity or calibrated confidence. No LLM is invoked.
