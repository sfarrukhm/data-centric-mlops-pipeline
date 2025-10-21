# 🧠 Data-Centric MLOps Pipeline

An end-to-end, data-first MLOps project built around the NYC Green Taxi dataset.  
I’m building this pipeline publicly to document how data flows from raw ingestion → cleaning → versioning → model training → deployment.

---

> 🚧 **Project Status:** Actively under development    

---

## 📖 Overview

This project is part of my journey to understand and implement MLOps from the ground up.  
I’m focusing on *data-centric* principles — treating data as the main product, not just a step before modeling.

The goal is to build a minimal, reproducible pipeline that can:
- Ingest monthly NYC taxi trip data automatically  
- Clean and preprocess it using consistent rules  
- Version and validate data as it evolves  
- Eventually train and deploy ML models using modern MLOps tools  

---

## 🧩 Current Progress

### ✅ Completed
- FastAPI service for downloading monthly datasets  
- Logging and directory structure for reproducibility  
- Continuous Integration pipeline (pytest + Docker build + push to DockerHub)  
- Data cleaning and preprocessing script (`scripts/clean_data.py`)  

### 🔜 Next Steps
- Add **data versioning** with DVC  
- Implement **data validation**  
- Integrate **MLflow** for experiment tracking  
- Automate deployment to AWS (ECR + ECS)

---



## ⚙️ How to Run

### 🔹 Local Setup

```bash
# 1. Install dependencies
uv sync

# 2. Download raw dataset (example: Jan 2025)
uv run python src/data/ingest.py -y 2025 -m 1

# 3. Clean the downloaded data
uv run python scripts/clean_data.py
````

### 🔹 Run FastAPI Service (Locally)

```bash
uv run fastapi dev main.py
```

### 🔹 Run with Docker

```bash
docker build -t data-mlops:v0.1.0 .
docker run -p 8080:8080 data-mlops:v0.1.0
```

---

## 🧪 Continuous Integration

This repository includes a CI pipeline that:

* Runs tests using **pytest**
* Builds and pushes Docker images to **DockerHub**
* Uses **GitHub Actions** for automation

File: `.github/workflows/ci.yml`

---

## 📊 Learning Log

| Date         | Update                     | Notes                                       |
| ------------ | -------------------------- | ------------------------------------------- |
| Oct 18, 2025 | Repo initialized           | Set up FastAPI app and folder structure     |
| Oct 19, 2025 | Added ingestion module     | Downloads raw NYC taxi parquet files        |
| Oct 20, 2025 | Added CI/CD workflow       | Automated testing + Docker image push       |
| Oct 21, 2025 | Added data cleaning script | First version of reproducible data pipeline |

---

## 🧰 Tech Stack

**Core Tools:** FastAPI · Docker · uv · GitHub Actions · Pandas · Parquet · Pytest
**Next Phase:** DVC · MLflow · AWS (ECR/ECS)

---

## 🪪 License

MIT License © 2025 [Your Name]

---

## ✍️ Note

This repository is part of my **Learning in Public** journey.
I’m intentionally documenting every phase — the good, the bad, and the refactors — so others can follow a realistic path into MLOps.

