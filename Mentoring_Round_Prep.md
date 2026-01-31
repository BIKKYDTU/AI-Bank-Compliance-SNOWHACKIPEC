# Online Mentoring Round – BankGuard (AI Bank Compliance)

**Evaluation prep for:** Idea & Feasibility | USP & Impact | Novelty | Pitch | Research & Revenue | Technical Complexity

---

## 1. Idea & Feasibility

### The Idea (30 seconds)
**BankGuard** is an agentic AI platform that helps banks comply with **RBI and FEMA** regulations. Banks upload regulatory PDFs (circulars, master directions) and internal policy documents; the system ingests them, retrieves relevant text using RAG, and runs four AI agents to produce:
- **Executive summary** with obligations and deadlines  
- **Impact mapping** (departments and products affected)  
- **Evidence-backed validation** with page citations  
- **Prioritized action plan** with owners and deadlines  

### Feasibility
| Aspect | How we demonstrate it |
|--------|------------------------|
| **Technical** | Working prototype: Streamlit UI, ChromaDB + HuggingFace embeddings, LangChain, 4-agent pipeline, DOCX report export. |
| **Data** | Uses publicly available RBI/FEMA PDFs and banks’ own policy PDFs—no proprietary data dependency. |
| **Regulatory fit** | Targets real pain: RBI circulars, FEMA amendments, and internal policy alignment. |
| **Scope** | MVP is document-centric (PDF in → report out); can extend to more doc types and workflows later. |

**One-liner:** *“Regulatory PDF in → structured obligations, impact, evidence, and action plan out—with a working agentic RAG pipeline and UI.”*

---

## 2. USP & Impact

### Unique Selling Points
1. **Agentic pipeline, not just chat:** Four specialized agents (Summarization, Impact Mapping, Validation, Action Planner) in a defined workflow—reproducible and auditable.
2. **RBI & FEMA focus:** Built for Indian banking regulation (RBI circulars, FEMA) and internal policy alignment from day one.
3. **Evidence and citations:** Every obligation is linked to source text and page numbers—critical for audits and legal review.
4. **Actionable output:** Not only “what changed” but “who does what by when” (action plan with department and priority).
5. **Private policy repository:** Banks can upload internal policies; retrieval can combine regulatory + policy context for gap analysis.

### Impact
| Stakeholder | Impact |
|-------------|--------|
| **Compliance teams** | Less manual reading of long PDFs; structured obligations and deadlines; ready-made evidence for audits. |
| **Risk / Legal** | Clear impact mapping (departments, products) and validation status. |
| **Operations** | Action plan with owners and priorities; DOCX report for internal distribution. |
| **Banks (institution)** | Faster regulatory adoption, better audit trail, reduced compliance risk. |

**Impact statement:** *“We reduce time-to-understand and time-to-act on RBI/FEMA updates, and give compliance teams a single place to see obligations, evidence, and next steps.”*

---

## 3. Novelty / Uniqueness

### What’s different
- **Multi-agent design:** Separate agents for summarization, impact mapping, validation, and action planning—each with a clear contract—rather than one monolithic LLM call. This improves interpretability and allows swapping/improving agents independently.
- **Banking-domain impact mapping:** Predefined keyword mappings for Indian banking (Compliance, Risk, Treasury, Legal, IT, Retail/Corporate, and products like Accounts, Loans, Cards, Payments, Forex, KYC)—tuned for RBI/FEMA language.
- **Regulatory + policy in one flow:** Same pipeline can ingest both regulatory PDFs and internal policy PDFs; retrieval modes (regulatory only / policy only / both) support gap analysis and policy alignment.
- **Structured output for compliance:** Obligations, deadlines, departments, products, evidence snippets, and action items—all in a fixed schema that fits audit and reporting needs, plus DOCX export.

### Differentiation vs generic tools
- **vs generic RAG chatbots:** We don’t just answer questions; we run a fixed compliance workflow and produce a standardized report with evidence and action plan.
- **vs manual reading:** Automated extraction + citations + impact + actions in one run.
- **vs single-model summarizers:** Multi-agent pipeline with validation and action planning, and banking-specific impact mapping.

---

## 4. Pitch / Presentation

### Opening (15–20 sec)
*“Banks spend huge time reading RBI and FEMA circulars and mapping them to internal policies. BankGuard is an agentic AI platform that takes regulatory and policy PDFs, runs a four-agent pipeline, and delivers a compliance report with obligations, deadlines, impact by department and product, evidence with page numbers, and a prioritized action plan—so compliance teams can act faster with full audit trail.”*

### Problem → Solution (30 sec)
- **Problem:** Regulatory PDFs are long and dense; manual extraction of obligations, deadlines, and impact is slow and error-prone; linking to internal policies and producing evidence for audits is tedious.
- **Solution:** One upload (and optional internal policies). RAG retrieves relevant chunks; four agents produce summary, impact map, validation with citations, and action plan. Output: dashboard + downloadable DOCX report.

### Demo flow (if showing live)
1. Show **BankGuard** UI (Streamlit).  
2. Upload a **regulatory PDF** (e.g. sample RBI/FEMA circular).  
3. Optionally add **internal policy** PDFs in sidebar.  
4. Click **Analyze Document** → show pipeline steps (ingest → RAG → 4 agents).  
5. Open **Results Dashboard**: obligations, deadlines, impact (departments/products), action plan table, evidence expanders with page refs.  
6. **Download Report (DOCX)** to show shareable output.

### Closing (10 sec)
*“We have a working prototype focused on RBI and FEMA, with a clear path to more regulations and deeper integration. We’re here to refine the idea and technical roadmap with your feedback.”*

### Anticipated Q&A (short answers)
- **“Who is the user?”** Compliance officers and risk teams in Indian banks and NBFCs.  
- **“How do you ensure accuracy?”** Validation agent ties obligations to source text and page; we position output as “assist and draft” for human review.  
- **“What about sensitive data?”** Can be deployed on-prem or in bank’s VPC; we don’t store customer data—only regulatory and policy documents.  
- **“Why four agents?”** Clear separation of tasks (summarize, map impact, validate, plan) improves transparency and lets us tune or replace each part independently.

---

## 5. Research & Revenue Model

### Research / Market context
- **Regulatory volume:** RBI and other regulators issue numerous circulars, master directions, and FAQs; FEMA amendments and clarifications add more. Banks must read, interpret, and implement in time.
- **Pain points:** Manual extraction, inconsistent interpretation across teams, slow policy updates, and audit requests for “evidence” of how a rule was read and applied.
- **Precedent:** RegTech and compliance automation are growing globally; Indian banking is digitizing rapidly (e.g. account aggregator, UPI, CBDC). Tools that reduce regulatory burden and improve traceability have clear demand.

### Revenue model (options to discuss)
| Model | Description |
|-------|-------------|
| **SaaS subscription** | Per-bank or per-user monthly/annual fee for platform access (tiers: number of documents, users, or regulations). |
| **Usage-based** | Per-document or per-report pricing (e.g. X rupees per analyzed circular or per generated report). |
| **Enterprise license** | One-time or annual license for on-prem or dedicated deployment; includes customization and support. |
| **Consulting / implementation** | Setup, integration with bank systems, and training; recurring support retainer. |

**Position for mentoring:** *“We’re exploring SaaS and enterprise licensing; we’d like feedback on pricing and which features (e.g. more regulations, API, integrations) would justify premium tiers.”*

### TAM / opportunity (talking points)
- **TAM:** All RBI-regulated entities (banks, NBFCs, payment operators) that must comply with RBI and FEMA.
- **Initial focus:** Mid to large banks and NBFCs with dedicated compliance teams.
- **Expansion:** More regulations (SEBI, IRDAI, etc.), more document types (notices, court orders), and API for embedding in existing GRC tools.

---

## 6. Technical Complexity

### Architecture (high level)
```
[User] → Streamlit UI → Orchestration Service
                              ↓
         PDF → Document Ingestion (pypdf, chunking) → ChromaDB (HuggingFace embeddings)
                              ↓
         Query → Vector search (RAG) → Retrieved chunks
                              ↓
         Agent 1: Summarization (obligations, deadlines)
         Agent 2: Impact Mapping (departments, products)
         Agent 3: Validation (evidence, page refs)
         Agent 4: Action Planner (tasks, owners, priority)
                              ↓
         Aggregated result → UI + DOCX report
```

### Technical highlights to mention
| Component | Technology / approach |
|-----------|------------------------|
| **Document ingestion** | pypdf for PDF parsing; page markers preserved for citations. |
| **Chunking** | LangChain RecursiveCharacterTextSplitter (configurable chunk size and overlap). |
| **Vector store** | ChromaDB (persistent); HuggingFace sentence-transformers for embeddings. |
| **RAG** | Similarity search with optional filters (e.g. document type, document ID). |
| **Agents** | Four Python agents with defined inputs/outputs; orchestration coordinates the pipeline. |
| **Structured output** | Pydantic-friendly dicts: summary (obligations, deadlines, summary_text), impact (departments, products), validation (status, evidence), action_plan (list of actions with owner and priority). |
| **UI** | Streamlit: upload, analyze, results dashboard, DOCX download. |
| **Report** | python-docx for Word report (summary, obligations, deadlines, impact, action plan, evidence). |

### Complexity points (for “technical depth”)
1. **RAG with metadata filtering:** Support for “regulatory only”, “policy only”, or “both” and by document ID—enables controlled retrieval for gap analysis.  
2. **Multi-agent orchestration:** Sequential flow with clear data contracts between agents; easy to add logging, versioning, or human-in-the-loop later.  
3. **Evidence traceability:** Validation agent maps obligations to retrieved chunks and page numbers—important for compliance and audit.  
4. **Banking-domain logic:** Impact mapping uses keyword sets for Indian banking departments and products—shows domain understanding.  
5. **Extensibility:** New document types, new agents (e.g. risk-scoring agent), or swap to OpenAI/other embeddings can be added without rewriting the whole pipeline.

### Possible next steps (technical roadmap)
- Replace or augment rule-based agents with LLM-based agents (e.g. LangChain + OpenAI/Open-source LLM) for better extraction.  
- Add authentication, audit logs, and role-based access for enterprise.  
- API layer (FastAPI) for integration with bank GRC/workflow tools.  
- Support for more file types (Word, HTML) and more regulations (SEBI, IRDAI).

### How RAG helps in BankGuard
| Step | What happens | Why RAG matters |
|------|----------------|------------------|
| **Ingest** | PDF text is chunked and embedded; chunks are stored in ChromaDB with metadata (document_id, type: regulatory_policy / internal_policy). | Builds a searchable “memory” of all documents so we can retrieve by meaning, not keywords. |
| **Retrieve** | A query (e.g. “foreign exchange drawal rules”) is embedded and used to run similarity search; top‑k chunks are returned, optionally filtered by type/document. | **Focus:** Long circulars are reduced to the most relevant passages, so agents work on signal, not noise. **Cross-doc:** With mode “both”, we pull from both the new circular and existing internal policies for gap analysis. |
| **Augment** | Retrieved chunks are concatenated and passed to Summarization, Impact Mapping, Validation, and Action Planner. | Agents get **grounded context**—they only use this retrieved text, so outputs can be tied back to specific pages and snippets. |
| **Evidence** | The Validation agent receives the same retrieved chunks (with page markers); it links each obligation to those chunks for citations. | RAG supplies the **exact source text** for “evidence” in the report—critical for audits and legal review. |

**One-line for pitch:** *“RAG lets us focus the agents on the most relevant parts of long documents and combine regulatory + policy context, and it provides the exact source chunks we need for evidence and page citations.”*

---

## Quick reference – Evaluation vs content

| Criterion | Where it’s covered |
|-----------|--------------------|
| **Idea & Feasibility** | Section 1 – idea, feasibility table, one-liner |
| **USP & Impact** | Section 2 – USPs, impact table, impact statement |
| **Novelty / Uniqueness** | Section 3 – what’s different, vs generic tools |
| **Pitch / Presentation** | Section 4 – opening, problem–solution, demo flow, closing, Q&A |
| **Research & Revenue** | Section 5 – research context, revenue options, TAM |
| **Technical Complexity** | Section 6 – architecture, tech table, complexity points, roadmap |

---

*Use this document to rehearse your pitch and to align talking points with your teammates before the Online Mentoring Round. Good luck!*
