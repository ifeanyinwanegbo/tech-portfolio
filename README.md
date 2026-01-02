# 👋 Hi, I'm Ifeanyi Martins Nwanegbo  
# Data Engineer | Data Scientist | Cloud Engineer | Analytics Professional  

Welcome to my technical portfolio, a curated collection of the projects, systems, and tools I build across data engineering, data science, cloud computing, analytics, and machine learning. I am passionate about designing scalable pipelines, solving real-world problems with data, and building intelligent systems that create business impact.

---

## Featured Projects

### 🔹Analytics Engineering – Supply Chain Cost Optimization (Python)

Designed and implemented an operations analytics model to determine optimal shipment quantities from two factories to three customer regions. The model minimizes total logistics and production cost under real-world constraints, enforcing exact demand fulfillment, factory capacity limits, non-negative flows, and nonlinear production cost functions using SciPy’s SLSQP algorithm.

### What this project does
- Models a two-factory, three-customer supply network with capacity-constrained production
- Optimizes shipment flows to minimize combined shipping and nonlinear production costs
- Enforces exact customer demand satisfaction and factory capacity limits
- Uses constrained nonlinear optimization (SLSQP) to compute optimal flows
- Outputs shipment plans, factory utilization, and minimum total cost

#### Tech used
- Python, NumPy, SciPy
- Nonlinear constrained optimization (SLSQP)

#### Code
- [`optimize_supply_chain.py`](src/optimize/optimize_supply_chain.py)

**Results Summary**
- All customer demand was met exactly while respecting factory capacity constraints
- Optimization minimized total logistics and production cost to **657,494.94**
- Factory B handled most shipments due to lower unit costs for C1 and C2
- Model validated through successful local execution

#### Sample Output

Optimization successful

Optimal shipment quantities (units):
A -> C1: 0.00
A -> C2: 0.00
A -> C3: 267.89
B -> C1: 300.00
B -> C2: 200.00
B -> C3: 32.11

Factory totals:
Total from A: 267.89 / 500.00
Total from B: 532.11 / 700.00

Minimum total cost: 657,494.94

---

### 🔹 GPU Market Pulse — End-to-End Data Engineering & Analytics Pipeline

**Problem:**
GPU prices and availability fluctuate rapidly, making it difficult to understand market trends, brand pricing gaps, and supply conditions from raw listings.

**Solution:**
Built an automated, script-driven data pipeline that ingests raw GPU pricing data, cleans and standardizes it, computes pricing deviations and availability metrics, and generates a structured market report without manual intervention.

### End-to-End Data Pipeline Architecture
The diagram below illustrates the complete data flow of the GPU Market Pulse project, from raw data ingestion to analytics and reporting.
![GPU Market Pulse Pipeline](diagrams/gpu_market_pipeline.png)

**Tech Stack**
- Python (pandas)
- Modular pipeline design (ingestion → processing → analytics → reporting)
- Markdown reporting
- Git / GitHub

**What I Built**
- Raw data ingestion from CSV sources
- Data cleaning and normalization
- Price deviation calculations (actual price vs MSRP)
- Brand-level pricing and availability aggregation
- Automated Markdown market summary generation

**Outcome (Measured Results)**

- Analyzed 6 GPU listings across NVIDIA and AMD
- Found NVIDIA average price: $1,275.67, AMD average price: $732.33
- 83% of listings in stock, indicating short-term supply stability
- Generated a reusable market report (market_summary.md) automatically from code

This pipeline is reusable and can be extended to larger datasets or scheduled data collection.


**Why This Matters?**
Demonstrates real-world data engineering skills: modular design, automation, reproducibility, and translating raw market data into business-ready insights.

#### Code
- [`load_gpu_prices.py`](https://github.com/ifeanyinwanegbo/gpu-market-pulse/blob/main/src/ingestion/load_gpu_prices.py)
- [`clean_gpu_prices.py`](https://github.com/ifeanyinwanegbo/gpu-market-pulse/blob/main/src/processing/clean_gpu_prices.py)
- [`analyze_gpu_market.py`](https://github.com/ifeanyinwanegbo/gpu-market-pulse/blob/main/src/analytics/analyze_gpu_market.py)

#### Output
- [`market_summary.md`](https://github.com/ifeanyinwanegbo/gpu-market-pulse/blob/main/docs/market_summary.md)

---

## Planned & In-Progress Projects
> *(Projects currently under development. Repositories will be added as they are completed.)*

### 🔹 **Machine Learning Classification System**  
Built and evaluated predictive models for real-world decision-making.  
**Skills:** Python (pandas, scikit-learn), model evaluation, data preprocessing.

### 🔹 **Cloud-Based Analytics Architecture**  
Designed a scalable cloud architecture for analytics workloads.  
**Skills:** Cloud services, data warehousing, dashboards, automation.

---

# 🛠️ Technical Skills

### **Programming & Data Tools**
- Python, SQL, R  
- Pandas, NumPy, Scikit-learn  
- Jupyter Notebook, VS Code, Git/GitHub  

### **Data Engineering**
- ETL/ELT Pipelines  
- Data Modeling  
- API Integration  
- Automation & Orchestration  
- Batch and Streaming Data  

# **Machine Learning**
- Classification & Regression  
- Feature Engineering  
- Model Optimization  
- Evaluation Metrics  

# **Cloud & Analytics**
- Cloud Architecture (general)  
- Data Warehousing Concepts  
- Dashboarding & Reporting  
- Storage, Compute, Deployment Concepts  

---

# 🎓 Certifications and Credentials   
- **Amazon Web Services Solutions Architect – Professional**  
- **Amazon Web Services Data Engineer – Associate**  
- **Certified Analytics Professional (CAP)**
- **Project Management Professional (PMP)**  

---

# About Me  
I am a graduate of **Texas State University**, where I earned a Master of Science in Data Analytics and Information Systems (Class of December 2025). I enjoy solving complex problems, building data-driven systems, and developing scalable solutions in AI, cloud engineering, data engineering, and data science.

---

## Contact
- **Portfolio:** https://github.com/ifeanyinwanegbo/tech-portfolio
- **GitHub Profile:** https://github.com/ifeanyinwanegbo
- **LinkedIn:** https://www.linkedin.com/in/ifeanyinwanegbo/
- **Email:** ifeanyimart@gmail.com
 

---

### ⭐ Thank you for viewing my portfolio — more projects will be added soon!
