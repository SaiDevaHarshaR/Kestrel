## GenAI Engineer – AthenTech

- Designed, developed, and deployed Sahasra AI, a multi-tenant healthcare AI chatbot replacing the company's existing Zoho chatbot.
- Built LLM-powered agents using Python, FastAPI, and LangChain, integrating with live hospital and laboratory databases (HIS/LIS).
- Implemented intent routing, database-aware agent workflows, RAG, and multi-provider LLM failover.
- Developed secure database interaction with read-only SQL execution, role-based access control, prompt-injection protection, and tenant isolation.
- Built multiple chatbot modes for hospital analytics, premium medical reports, B2B client assistance, and company FAQs.
- Implemented Redis caching, token usage tracking, Langfuse observability, and automated evaluation pipelines.
- Developed an admin panel with client onboarding, license management, permissions, monitoring, and human-in-the-loop answer review.
- Implemented multilingual support across 11 Indian languages.
- Built automated testing and accuracy evaluation harnesses, improving performance from 231/280 to 277/280 on a 280-question, 9-language test suite.
- Deployed and maintained the application on Windows IIS, ensuring production readiness and operational reliability.




I want to join Anthropic because I see AI development moving beyond chatbots and simple LLM integrations towards highly advanced agents, autonomous systems, and I want to contribute to that evolution.

What interests me about Anthropic is its approach to building AI that is not just powerful, but also reliable, interpretable, and safe.

In my current role, I independently built and deployed a multi-tenant healthcare AI agent, where accuracy, security, access control, and reliability were critical. That experience made me realize that building useful AI systems requires much more than choosing a good model.

I see Anthropic as an environment where I can work on challenging AI engineering problems, deepen my understanding of frontier AI, and contribute to technology that has a meaningful impact.






I want to join Anthropic because I am genuinely interested in the direction where AI is heading, particularly the transition from simple LLM powered applications to capable, autonomous AI Agent systems that can solve complex real world problems.

What attracts me to Anthropic is its work on building AI that is not only powerful but also reliable, interpretable, and safe. I believe these qualities are essential as AI becomes increasingly integrated into critical business operations and everyday decision making.

In my current role as a GenAI Engineer at AthenTech, I independantly designed, developed, and deployed Sahasra AI, a multi-tenant healthcare AI assistant that replaced the company's existing chatbot. Working on a real-world healthcare product taught me that building useful AI goes far beyond connecting an application to an LLM. Accuracy, security, reliability, and responsible access to information are equally important.

I worked on agentic workflows, database connected AI agents, multi provider LLM failover, prompt injection protection, role-based access control, evaluation pipelines, and human-in-the-loop review systems. These experiences made me particularly interested in the engineering challenges involved in making AI systems dependable and safe in production environments.

I also want to challenge myself by working alongside people who are pushing the boundaries of AI research and engineering. I am particularly excited by the opportunity to learn from Anthropic's approach to frontier AI development while contributing my hands-on experience in building and deploying agentic applications.

Ultimately, I see Anthropic as a place where I can grow as an AI engineer while contributing to a larger mission of making increasingly capable AI systems genuinely useful, trustworthy, and beneficial to people all over the world.





I am looking for an opportunity to take on more challenging engineering problems, work with larger datasets, and grow alongside experienced engineers. My current experience has given me end to end exposure to building and deploying production AI systems. I now want to broaden my expertise in large scale data engineering and analytics while contributing to products that operate at significant scale.









I want to work at Sarvam AI because I am genuinely excited about building AI technology from India that can compete on a global scale. Sarvam's focus on developing foundation models, voice AI, and multilingual AI systems aligns closely with my interests and experience in agentic AI and LLM engineering.

Having independently built and deployed Sahasra AI, a multilingual healthcare AI assistant supporting 11 Indian languages, I have experienced the challenges of making AI useful in real world environments, particularly around accuracy, language understanding, reliability, and scalability.

I see Sarvam AI as an opportunity to work on challenging AI engineering problems, contribute to products with meaningful real-world impact, and deepen my expertise in building production-grade AI systems. I would love to contribute my experience in agentic AI, backend engineering, and LLM systems to a team working towards making AI more accessible and capable for India.
















On Sahasra, the pain wasn’t raw QPS as much as high latency under concurrent premium questions - LLM + MSSQL paths often sat 10–20s while a burst of users stacked up on a single Windows/IIS node. I cut load and wait time by pushing high-frequency asks (bills, collections, dashboards) onto an intent/fixed-SQL fast path so they never hit the LLM, added an answer cache for repeated questions, and kept `/health` cheap so the proxy could still see the process as alive under load. On the data side we stayed on per-institution MSSQL with read-only logins, strict SELECT-only execution, and scoped tools instead of wide ad-hoc access; multi-tenant isolation was by activation code -> one DB, not one shared schema. We load-tested with concurrent clients and used caching off/on to see the cliff; full horizontal scale (second node, shared Redis queue, hard LLM concurrency caps) is the next architectural step we identified when traffic grows past one box.












































# **Complete Knowledge, Skills & Work Profile**

Compiled from our conversations and saved memory · Updated November 18, 2026

## **1. Education & Professional Background**

- **Degree:** B.Tech in Computer Science / Data Science.
- **Graduation:** 2025.
- **Location:** Hyderabad, India.
- **Experience:** Approximately 1–2 years, including internship and professional project work.
- **Current professional direction:** AI Engineer, Agentic AI Engineer, AI Forward Deployed Engineer (FDE), AI Architect, AI Data Engineer and LLMOps Engineer.

## **2. Certifications — Passed**

**NVIDIA NCA-GENL**

Passed

**NVIDIA NCP-AAI**

Passed

**Databricks Data Engineer Associate**

Passed

## **3. Technical Knowledge & Skills**

### **Programming & Backend**

- Python
- Java
- SQL
- FastAPI
- REST APIs
- Async programming
- React.js
- Vite
- Streamlit

### **Artificial Intelligence & LLM Engineering**

- Generative AI
- Agentic AI
- Multi-Agent Systems
- AI Agent Architecture
- AI FDE concepts
- AI Architect concepts
- LLMOps
- Retrieval-Augmented Generation (RAG)
- Agentic RAG
- Local LLMs (Llama / Ollama)
- Tool Calling
- Function Calling
- Hybrid Retrieval
- BM25
- Vector Search
- Reranking
- RAGAS Evaluation
- FAISS
- Redis-based AI memory
- AI-powered Root Cause Analysis
- Autonomous AI agents

### **Data Engineering & Databricks**

- Databricks
- Delta Lake
- Medallion Architecture (Bronze, Silver, Gold)
- Unity Catalog
- Data ingestion and transformation
- Data quality
- Schema detection and mapping
- PII detection concepts
- Databricks SQL Warehouse
- Lakehouse architecture
- SQL analytics

### **Cloud & DevOps**

- AWS
  - EC2
  - Auto Scaling Groups
  - Elastic Load Balancers
  - ECS / Fargate
  - ECR
  - EKS
  - ElastiCache
- Microsoft Azure
- Docker
- Kubernetes
- Terraform
- Git / GitHub
- CI/CD pipelines
- Linux / Ubuntu
- VMware
- OpenVPN
- SSH tunnelling
- Infrastructure as Code

### **Monitoring & Observability**

- Prometheus
- Grafana
- Logging and metrics
- AI-powered incident analysis
- SRE concepts
- Application monitoring

### **Databases & Storage**

- MySQL
- Microsoft SQL Server (MSSQL)
- SQLite
- Redis
- FAISS
- Delta Lake

## **4. Professional Experience**

### **CloudAngles — Cloud/DevOps Internship (2024)**

Hands-on experience with:

1. AWS EC2 instance provisioning.
2. High availability using Auto Scaling Groups.
3. Elastic Load Balancer configuration.
4. VMware Workstation and Ubuntu.
5. LAMP stack deployment.
6. WordPress deployment.
7. Separating Apache and MySQL across EC2 instances.
8. AWS Security Groups.
9. SSH tunnelling and PuTTYgen (PEM to PPK).
10. OpenVPN deployment on EC2.
11. MySQL Master-Master replication.

## **5. Professional Project Work**

### **A. Sahasra LIS GenX — AI Agentic Chatbot**

Deployed project

Developed an AI-powered chatbot for hospital and diagnostic laboratory operations under AthenTech.

**Product capabilities and scope:**

- Conversational AI for diagnostic centres.
- Patient-related queries.
- Centre confirmation and OTP workflows.
- Branch and location handling.
- Test booking workflows.
- Laboratory status tracking.
- Radiology status tracking.
- Report delivery and authorization status.
- Turnaround Time (TAT) tracking.
- Referral doctor information.
- Revenue analytics (cash, card, UPI).
- Multi-tenant architecture.

**Technical work:**

- Python and FastAPI backend.
- React and Vite frontend.
- MSSQL integration.
- SQLite platform database.
- Multi-tenant database configuration.
- Dynamic database connection configuration.
- Schema mapping and management.
- REST API development.
- Admin dashboard architecture.

**Database knowledge gained:**

- `mstPatientRegistration`
- `trnINVLABPRI`
- `View_TestCode`
- `trnInvStatus`
- `mstDoctor`
- `LISBRANCH`

Important implementation requirement: Konnect Diagnostics integration must remain strictly read-only.

### **B. Autonomous Multi-Agent AI DevOps System**

Built an AI-driven DevOps/SRE automation project.

- Log and metric analysis.
- Autonomous multi-agent architecture.
- Root Cause Analysis (RCA).
- Remediation recommendations.
- Redis-based memory.
- FAISS-based vector retrieval.
- Asynchronous agent execution.
- AI-powered operational troubleshooting.

### **C. SRE-AI-CoPilot**

- Near-real-time log analysis.
- FAISS and Redis integration.
- Docker containerization.
- CI/CD automation.
- Zero-downtime deployment architecture.
- AI-assisted SRE workflows.

### **D. Local RAG System**

GitHub: `SaiDevaHarshaR/Local-Rag`

- Local LLM integration.
- Llama 3 / Ollama.
- Hybrid search.
- BM25 retrieval.
- Vector retrieval.
- Reranking.
- FAISS.
- Redis.
- RAGAS evaluation.
- FastAPI.
- Streamlit.
- Docker.

### **E. Custom Grok-Inspired AI Bot**

- Custom conversational AI.
- LLM integration.
- AI chatbot development.
- Backend/API integration.

### **F. DevOps AI Chatbot / Terraform IaC Generator**

- Conversational DevOps assistance.
- Terraform Infrastructure as Code generation.
- AI-powered infrastructure assistance.

## **6. AI Architecture & Advanced Engineering Knowledge**

You have also studied and developed knowledge in:

- AI Forward Deployed Engineering (FDE).
- AI Architect responsibilities and system design.
- Agent orchestration.
- AI-to-database integration.
- MCP architecture and tool gateways.
- Secure database access for AI agents.
- SQL validation and query restrictions.
- Authentication and authorization.
- Rate limiting and audit logging.
- Repository and semantic layers.
- PostgreSQL/MySQL and Databricks integration patterns.

You have explored advanced LLM engineering topics:

- KV Cache.
- Speculative Decoding.
- Quantization.
- vLLM.
- SGLang.
- GraphRAG.
- Agentic RAG.
- RLHF.
- DPO.

These are areas of learning and exploration, not necessarily all production implementations.

## **7. Flagship Enterprise Project — Aegis AI Platform**

Your planned enterprise-grade AI platform combines data engineering, AI agents and analytics.

**Architecture**

**CSV / Enterprise Data Ingestion**

**Schema Detection · PII · Data Quality**

**Databricks Lakehouse**

Bronze → Silver → Gold · Delta Lake · Unity Catalog

**AI Agent / RAG / SQL Analytics**

**Dashboard · Monitoring · RCA**

Planned technologies:

- Python, FastAPI.
- Databricks Free Edition.
- Ollama local LLMs.
- Vector database.
- Redis.
- Streamlit.
- Docker and Kubernetes.
- Terraform.
- GitHub Actions.
- Prometheus and Grafana.

## **8. Other Technical Areas You've Worked With**

- AWS infrastructure provisioning.
- High-availability architecture.
- Database replication.
- Multi-cloud concepts.
- Container orchestration.
- Microservices and APIs.
- CI/CD.
- Infrastructure automation.
- Enterprise database connectivity.
- Multi-tenant SaaS architecture.
- Healthcare/LIS integrations.
- AI-powered business automation.
- Production-oriented application deployment.

## **9. GitHub & Development**

Your known portfolio includes:

| Project                       | Focus                  |
| ----------------------------- | ---------------------- |
| Local-Rag                     | Local LLM + RAG        |
| Autonomous Multi-Agent DevOps | Autonomous AI + DevOps |
| SRE-AI-CoPilot                | AI-powered SRE         |
| Custom Grok-inspired Bot      | Conversational AI      |
| Terraform AI Chatbot          | DevOps + IaC           |
| Sahasra LIS GenX              | Healthcare Agentic AI  |

## **10. Career Direction & Target Roles**

Your target roles include:

1. AI Engineer
2. Agentic AI Engineer
3. AI Forward Deployed Engineer
4. AI Architect
5. AI Data Engineer
6. LLMOps Engineer
7. AI Platform Engineer
8. MLOps / DevOps Engineer
9. Cloud Infrastructure Engineer
10. AI Solutions Engineer

**Companies you've expressed interest in:**

- OpenAI
- Anthropic
- xAI
- NVIDIA
- Databricks
- Snowflake
- AWS
- Microsoft
- Google DeepMind
- Meta

You prefer high-growth AI startups, including smaller engineering teams, and opportunities offering international remote work or visa sponsorship.

## **Overall assessment of your knowledge profile**

# **AI + Cloud + Data Engineering**

Your profile combines three major engineering domains:

**AI Engineering**

Agents, RAG, LLMOps, FDE

**Data Engineering**

Databricks, SQL, Delta Lake

**Cloud & DevOps**

AWS, Kubernetes, Terraform

**Your strongest differentiator:** Combining AI agents with enterprise data systems, cloud infrastructure and actual business workflows, rather than focusing exclusively on chatbot development.

**One important distinction:** Your certifications are passed, your Sahasra project is deployed, and your other portfolio projects demonstrate hands-on development. Your advanced architecture and model-serving topics include both practical experience and ongoing learning; they shouldn't all be represented as production-level expertise without further evidence.





