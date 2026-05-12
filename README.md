# LLM · Langchain · LangGraph · Vector DB

A collection of hands-on notebooks covering large language models, Langchain pipelines, agentic workflows with LangGraph, and vector database search with Pinecone.

---

## Projects

### 🤖 LLM Foundations (`/LLM`)

| Project | Description |
|---|---|
| **OpenAI API Setup** | Connecting to the OpenAI API, managing keys via config, and making basic completions |
| **HuggingFace Transformers** | Using `pipeline()` for sentiment analysis and named entity recognition (NER) out of the box |
| **BERT Question Answering** | Loading `bert-large-uncased-whole-word-masking-finetuned-squad` to answer questions from a context passage |
| **XLNet Emotion Classifier** | Fine-tuning XLNet on an emotions dataset (train/val/test) for multi-class text classification |

---

### 🔗 Langchain (`/Langchain`)

| Project | Description |
|---|---|
| **OpenAI API with Langchain** | Wrapping the OpenAI API using `ChatOpenAI` and managing environment variables with `dotenv` |
| **Model I/O & Prompt Templates** | Building prompt templates, formatting inputs, and working with chat models |
| **Output Parsers** | Parsing LLM responses into strings, comma-separated lists, and structured formats |
| **LangChain Expression Language (LCEL)** | Composing chains using the `|` pipe operator — prompts, models, and parsers chained together |
| **RAG — Retrieval Augmented Generation** | Loading PDFs with `PyPDFLoader`, chunking documents, embedding into a vector store, and answering questions over private data |

---

### 🕸️ LangGraph (`/LangGraph`)

| Project | Description |
|---|---|
| **Stateful Conversational Agent** | Building a multi-turn agent using `StateGraph`, typed state with `TypedDict`, and `ChatOpenAI` as the backbone model |

---

### 🗄️ Vector DB (`/Vector-DB`)

| Project | Description |
|---|---|
| **Pinecone Introduction** | Connecting to Pinecone, creating serverless indexes, and upserting vectors |
| **Course Semantic Search** | Embedding course descriptions with `SentenceTransformer` and querying Pinecone for semantically similar courses |
| **Section Search with BERT** | Extending semantic search to course sections using BERT embeddings and weighted Pinecone queries |
| **FineWeb Vector Store** | Loading the FineWeb dataset from HuggingFace, embedding with `SentenceTransformer`, and indexing into Pinecone |

---

## Topics Covered

- Large Language Models (LLMs) & the OpenAI API
- HuggingFace Transformers & pre-trained models
- BERT, XLNet — fine-tuning transformer models
- Langchain: Model I/O, Prompt Templates, Output Parsers
- LangChain Expression Language (LCEL)
- Retrieval Augmented Generation (RAG)
- Agentic workflows with LangGraph
- Vector databases with Pinecone — indexing, upserting, semantic search

## Stack

`Python` · `Jupyter Notebooks` · `OpenAI` · `HuggingFace Transformers` · `Langchain` · `LangGraph` · `Pinecone` · `SentenceTransformers`
