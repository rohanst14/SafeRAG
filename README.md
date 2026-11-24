# SafeRAG

### Evidence-grounded retrieval

![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white) ![Tests](https://github.com/rohanst14/SafeRAG/actions/workflows/tests.yml/badge.svg) ![Stage](https://img.shields.io/badge/stage-research%20prototype-64748b)

Retrieve a supporting passage instead of inventing an answer when the corpus does not contain relevant evidence.

## Design

Tokenize and count terms → rank by cosine similarity → apply threshold → return evidence or abstain.

## Quick start

```bash
git clone https://github.com/rohanst14/SafeRAG.git
cd SafeRAG
python -m venv .venv
# Activate .venv for your operating system.
python -m pip install -e .
python examples/demo.py
python -m unittest discover -s tests -v
```

## Usage

```python
from saferag import answer
result = answer('reactor pressure', {'manual': 'reactor pressure rises', 'other': 'ocean waves'})
print(result)
```

## API contract

| Field | Description |
|---|---|
| Entry point | `answer(question, documents, threshold=.2)` |
| Inputs | A mapping from stable document IDs to text; threshold in [0,1]. |
| Outputs | A verbatim passage, source ID, cosine score and abstention flag; no generated answer. |

## Repository map

| Path | Role |
|---|---|
| [src/saferag/](src/saferag/) | Python implementation |
| [examples/demo.py](examples/demo.py) | Reproducible synthetic demo |
| [tests/test_core.py](tests/test_core.py) | Regression checks |
| [docs/methodology.md](docs/methodology.md) | Evaluation design and limitations |
| [ROADMAP.md](ROADMAP.md) | Milestones and planned work |
| [CI workflow](.github/workflows/tests.yml) | Automated tests and demo |

## Evaluation and limitations

Compare coverage and retrieval precision on a labeled question–document corpus; tune threshold on a separate validation set.

Lexical overlap is not entailment, semantic similarity or calibrated confidence. No LLM is invoked. The current demonstration is synthetic; no real-world performance claims are made.

## Project status

AI-assisted research prototype. See [roadmap](ROADMAP.md) for planned extensions.
