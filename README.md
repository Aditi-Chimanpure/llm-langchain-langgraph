# LLM · Langchain · LangGraph · Vector DB · Streamlit

A collection of hands-on notebooks and apps covering large language models, Langchain pipelines, agentic workflows with LangGraph, vector database search with Pinecone, and Streamlit-based AI applications.

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

### 🎙️ Speech Recognition (`/Speech Recognition`)

| Project | Description |
|---|---|
| **Speech Recognition** | Audio waveform analysis with `librosa`, transcription via Google Web Speech API and OpenAI Whisper, batch transcription to CSV, and Text-to-Speech with `gTTS` |

---

### 🖥️ Streamlit Fundamentals (`/Streamlit`)

| File | Description |
|---|---|
| `app.py` | Core UI elements — titles, headers, markdown, and displaying data with `st.write` |
| `session_state.py` | Managing state across reruns with `st.session_state` and nested button logic |
| `chat_elements.py` | Chat UI basics using `st.chat_message` and `st.chat_input` |

---

### 🚀 Mini Project — PrepAI (`/PrepAI`) · [Live Demo](https://prep-ai-tool.streamlit.app/)

An AI-powered mock interview app built with Streamlit and GPT-4o.

- User fills in their **name, experience, skills, target level, position, and company**
- GPT-4o acts as an HR interviewer and conducts a **5-question mock interview**
- After the interview, generates a **score (1–10) and written feedback** on performance
- Built with `streamlit`, `openai`, and `streamlit-js-eval` for session reset

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
- Speech recognition with Google Web Speech API and OpenAI Whisper
- Audio processing with `librosa` and Text-to-Speech with `gTTS`
- Streamlit — UI elements, session state, chat interface
- Building end-to-end AI apps with Streamlit + OpenAI

## Stack

`Python` · `Jupyter Notebooks` · `OpenAI` · `HuggingFace Transformers` · `Langchain` · `LangGraph` · `Pinecone` · `SentenceTransformers` · `Whisper` · `librosa` · `Streamlit`
