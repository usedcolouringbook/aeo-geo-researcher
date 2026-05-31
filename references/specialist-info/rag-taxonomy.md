# RAG Taxonomy Reference

For the agentic-discovery specialist and for any research touching how AI systems retrieve, process, and generate answers. Understanding RAG architecture helps diagnose why a client's content is or isn't being cited.

---

## The 16 RAG Types

Source: Medium/aingineer — T3 practitioner guide. Framework names are industry-standard; implementation frameworks are current as of mid-2026.

| # | Name | Core Mechanism | Best For |
|---|---|---|---|
| 1 | **Standard RAG** | RAG-Sequence: conditions on each retrieved doc independently. RAG-Token: incorporates tokens at each generation step | QA systems, conversational AI, summarization |
| 2 | **Agentic RAG** | Autonomous agents with dynamic retrieval, real-time API/database queries, tool integration | Personal assistants, research automation, customer service bots |
| 3 | **Graph RAG** | Knowledge graphs with nodes (entities) and edges (relationships); relational reasoning across connected entities | Semantic search, expert systems, knowledge management |
| 4 | **Modular RAG** | Retrieval, reasoning, and generation as independent microservices; can be upgraded independently | Large-scale enterprise, agile development |
| 5 | **Memory-Augmented RAG** | Persistent memory layer stores historical interactions; dynamic recall for continuity across sessions | Multi-session chatbots, personalized recommendations |
| 6 | **Multi-Modal RAG** | Retrieves and integrates text, images, audio; cross-modal matching | Image captioning, video summarization, accessibility |
| 7 | **Federated RAG** | Decentralized data sources; data stays local; privacy-preserving | Healthcare, cross-enterprise collaboration, GDPR/HIPAA contexts |
| 8 | **Streaming RAG** | Real-time data streams; low-latency retrieval; continuous fresh data | Financial markets, social media monitoring, live news |
| 9 | **ODQA RAG** | Open-Domain QA; broad, unrestricted queries across extensive corpora | Search engines, educational platforms |
| 10 | **Contextual Retrieval RAG** | Uses conversation history to refine retrieval; session-based personalization | Multi-turn chatbots, support systems |
| 11 | **Knowledge-Enhanced RAG** | Integrates structured knowledge bases, ontologies, curated datasets; validation layer | Legal research, clinical decision support |
| 12 | **Domain-Specific RAG** | Specialized corpora; field-specific terminology; regulatory compliance built in | Financial analysis, healthcare, legal tools |
| 13 | **Hybrid RAG** | Combines sparse (BM25/keyword) and dense (embedding) retrieval; adaptive weighting | Advanced search, complex QA, research systems |
| 14 | **Self-RAG** | Self-reflection mechanisms; iterative output refinement; error correction loop | Content creation, decision support |
| 15 | **HyDE RAG** | Generates a hypothetical document from the query; uses it as embedding to retrieve real documents | Implicit query handling, knowledge discovery |
| 16 | **Recursive/Multi-Step RAG** | Multiple retrieval-generation rounds; sequential refinement; step-by-step reasoning chains | Analytical workflows, complex problem-solving |

---

## RAG Decision Framework

When a client or research question involves recommending or evaluating a RAG architecture:

| Requirement | Recommended type |
|---|---|
| Large data volume | Modular RAG |
| Multi-format data (text + images) | Multi-Modal RAG |
| Real-time data required | Streaming RAG |
| Low latency critical | Streaming RAG or Standard RAG |
| Highest accuracy required | Self-RAG or Knowledge-Enhanced RAG |
| Complex multi-step reasoning | Recursive/Multi-Step RAG |
| Privacy-preserving across organizations | Federated RAG |
| Relational entity reasoning | Graph RAG |

**Scoring formula for RAG type selection:**
(Core Requirements × 0.4) + (Use Case Fit × 0.3) + (Implementation Feasibility × 0.3)

---

## Key RAG Concepts for AEO/GEO Research

### Chunking — Why It Determines Citability
The RAG pipeline's chunking stage is where most content visibility is won or lost. Boundary types:
- **Paragraph-based** (most common): each paragraph = one chunk
- **Heading-based**: each H2/H3 section = one chunk
- **Token-based**: fixed token count (512–1024 tokens), regardless of content structure
- **Hybrid**: heading-based with token cap fallback

Content that chunks cleanly gets retrieved. Content where key facts straddle chunk boundaries gets retrieved as partial context and may not cite correctly.

### Contextual Retrieval (Anthropic)
Anthropic research technique: prepend chunk-specific context to each chunk before embedding. Example: "This is from a 2026 guide to GEO. The following section covers FAQ architecture." This context travels with the chunk and improves retrieval precision. Relevant when a client asks why their well-structured content isn't being retrieved accurately.

### Hybrid Search (BM25 + Dense)
Most production RAG systems now use hybrid retrieval — combining keyword matching (BM25) with vector similarity (dense embeddings). Implication: traditional SEO keyword signals still matter inside RAG systems, not just for organic search. Content that is both keyword-rich and semantically dense retrieves better than either alone.

### HyDE — Practical Implication
If a platform uses HyDE, it generates a hypothetical "ideal answer" before retrieving. Content that matches what an ideal answer looks like — clear, definitive, fact-dense — will retrieve better than content that requires context to make sense.

---

## RAG Evaluation Metrics

When evaluating whether a RAG system is producing good output:

| Metric | What it measures |
|---|---|
| Context precision | Are the retrieved chunks actually relevant to the query? |
| Answer relevancy | Does the generated answer address what was asked? |
| Faithfulness | Does the answer accurately reflect the retrieved content without hallucination? |
| Hallucination rate | How often does the model add claims not in the retrieved context? |

**Evaluation tools:** ragas, Trulens, Phoenix, Deepchecks, AutoRAG, Vectara HHEM (hallucination evaluation model), langfuse, evalmy.ai

---

## RAG Ecosystem Reference

### Frameworks
LangChain, LlamaIndex, Haystack, DSPy, LightRAG, Langroid, mem0, RAGLite, cognee (GraphRAG)

### Engines
RAGFlow, Dify, R2R ("Elasticsearch for RAG"), Embedchain, txtai, dsRAG, FlashRAG, pgai, Vectara

### Data Preparation
Chonkie (chunking), pdfmux (PDF→Markdown with confidence scoring), Unstructured.io, LlamaParse, Reducto, Chunkr (vision-model OCR), CocoIndex (ETL)

### Vector Databases
ChromaDB, Qdrant, Pinecone, Weaviate, PostgreSQL (pgai/PostgresML extensions), Azure AI Search, Cosmos DB

### Local Deployment
Ollama, vLLM, LM Studio, LocalAI

### Benchmark Leaderboards
- Artificial Analysis: LLM comparison
- HuggingFace MTEB: embedding models
- Vectara Hallucination Leaderboard

Source: RAGHub (GitHub, 1.7k stars, actively maintained) — T3 aggregator. Use as a starting point for tool discovery; verify individual tools independently before recommending.
