# Placement Intelligence Assistant

Advanced Multimodal Retrieval-Augmented Generation (RAG) system built for placement intelligence, semantic retrieval, grounded response generation, and adversarial query handling.

---

# Overview

Placement Intelligence Assistant is an end-to-end modular RAG system designed to answer placement-related queries using structured and unstructured placement datasets.

The system supports:

* PDF ingestion
* Table extraction
* Semantic chunking
* Metadata-aware retrieval
* Hybrid search
* Reranking
* Conflict detection
* Grounded response generation
* Source citations
* Graceful fallback handling

---

# Features

## Advanced RAG Pipeline

* End-to-end Retrieval-Augmented Generation architecture

## PDF Ingestion

* Extracts textual data from placement datasets

## Structured Table Extraction

* Parses company eligibility and package tables

## Semantic Chunking

* Splits large documents into retrieval-friendly chunks

## Metadata-Aware Retrieval

* Supports filtering by:

  * company
  * section
  * eligibility criteria

## Hybrid Retrieval

* BM25 keyword retrieval
* Semantic vector retrieval

## Ollama Embeddings

* Local embedding generation using Ollama

## ChromaDB Vector Store

* Persistent vector storage and semantic search

## Reranking Pipeline

* Improves retrieval relevance

## Conflict Detection

* Detects contradictory information across sources

## Grounded Response Generation

* Generates answers strictly from retrieved context

## Source Citations

* Displays retrieval sources for transparency

## Graceful Fallback Handling

* Prevents hallucinations for out-of-domain queries

## Streamlit Interface

* Interactive chat-style frontend

---

# Architecture

```text
User Query
    ↓
PDF Ingestion
    ↓
Chunking + Metadata
    ↓
Embedding Generation
    ↓
ChromaDB Storage
    ↓
Hybrid Retrieval
    ↓
Metadata Filtering
    ↓
Reranking
    ↓
Grounded Generation
    ↓
Citations + Fallback Handling
```

---

# Tech Stack

| Component       | Technology             |
| --------------- | ---------------------- |
| Frontend        | Streamlit              |
| Embeddings      | Ollama                 |
| Vector Database | ChromaDB               |
| Retrieval       | BM25 + Semantic Search |
| PDF Processing  | pdfplumber             |
| Language        | Python                 |

---

# Project Structure

```bash
placement-intelligence-rag/
│
├── app.py
├── README.md
├── requirements.txt
│
├── data/
├── src/
│
│   ├── ingestion/
│   ├── preprocessing/
│   ├── chunking/
│   ├── embeddings/
│   ├── vectordb/
│   ├── retrieval/
│   ├── reranking/
│   ├── reasoning/
│   ├── generation/
│   └── utils/
```

---

# Installation

## Clone Repository

```bash
git clone <your_repo_url>
cd placement-intelligence-rag
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Ollama Setup

Install Ollama:

https://ollama.com/download

Pull embedding model:

```bash
ollama pull nomic-embed-text
```

Start Ollama:

```bash
ollama serve
```

---

# Run Application

```bash
streamlit run app.py
```

---

# Example Queries

* What is Amazon package?
* Compare Google and Microsoft.
* Which company allows backlogs?
* What are Microsoft interview topics?
* Which company offers highest package?
* What is dengue?

---

# Adversarial Query Handling

The system safely rejects unrelated or out-of-domain questions.

Example:

```text
Input: What is dengue?
Output: No relevant information found in the uploaded dataset.
```

---

# Future Improvements

* OCR integration
* Multimodal image retrieval
* Conversational memory
* LLM-based answer synthesis
* Agentic workflows
* Deployment-ready cloud inference

---

# Author

Developed as part of RAG-ATHON 24 hackathon challenge.
