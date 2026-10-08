# Sahel Azzam — Software, AI & Automation Portfolio

**IT & Automation Engineer based in Amman, Jordan.** I have completed my **M.S. in Computer Science at Texas Tech University**, following a **B.S. in Computer Science from Texas Tech University**.

My professional experience includes industrial automation, PLC/SCADA integration, plant data visibility, and frontend development. My public projects cover web applications, LLM evaluation, machine learning, algorithms, and systems.

## Engineering experience

### IT & Automation Engineer — Amman, Jordan

- Work on plant digitalization through Ignition SCADA and PLC integration.
- Experience with Siemens S7-1200 and S7-200 SMART PLCs, tag mapping, Modbus communication, and monitoring/control workflows.
- Troubleshoot PLC/SCADA communication and OT network issues; support plant data visibility and operating workflows.

### Frontend Internship — June–August 2024

- Worked on a React frontend redesign.
- Used Axios to connect frontend components to REST APIs.

## Completed qualifications

- **M.S. in Computer Science — Texas Tech University, completed**
- **B.S. in Computer Science — Texas Tech University, completed**

## Selected technical projects

| Project | Implementation and technical focus |
|---|---|
| [DriftWatch](https://github.com/sahelmain/DriftWatch) | LLM evaluation and drift-monitoring project with a FastAPI backend, React/TypeScript dashboard, persisted evaluation runs, provider integrations, background-job configuration, tests, and a CI workflow. |
| [TruthfulQA LLM Evaluation Study](https://github.com/sahelmain/llm-hallucination-phoenix) | Co-authored study comparing local LLMs, prompt templates, and category-level results. Includes experiment scripts, deterministic reference scoring, saved analysis artifacts, and a report. |
| [AI vs Human Text Detection — Deep Learning](https://github.com/sahelmain/AI-Human-Text-Detection-Deep-Learning) | PyTorch CNN/LSTM/RNN models, token-sequence preprocessing, saved training outputs, model artifacts, and a Streamlit interface. |
| [Text Classification ML Pipelines](https://github.com/sahelmain/Advanced-Text-Classification-ML-Pipelines) | Notebook-based preprocessing and TF-IDF pipelines, SVM/decision-tree models, GridSearchCV, custom transformers, voting/stacking experiments, and prediction exports. |
| [Streaming Pattern Matching](https://github.com/sahelmain/streaming-pattern-matching-optimization) | Naive and KMP implementations on simulated character streams and network-flow-derived sequences, with comparison counters, timing experiments, CSV results, and visualization scripts. |
| [Heartbeat Protocol Simulation](https://github.com/sahelmain/csim-heartbeat-protocol) | C/CSIM discrete-event simulation of Hello/Hello_Ack messages, timeouts, retries, and packet loss. Includes local mock code, build targets, test scripts, and visualizations. |

Related work: [Streamlit ML text-detection app](https://github.com/sahelmain/AI-Human-Text-Detection-App) and [baseline text-classification notebook](https://github.com/sahelmain/Text-Classification-Human-vs-AI-).

The text-classification, streaming-algorithm, and heartbeat projects are academic work. DriftWatch is an engineering project, and the TruthfulQA study is collaborative research. Classification scores depend on the dataset and validation procedure; the TruthfulQA results use a deterministic word-overlap scoring heuristic. See the source and experiment context when interpreting results.

The application links directly to implementation evidence at the repository commits reviewed on **8 October 2026**. Its source dates identify those snapshots; they are not live activity statistics.

## Technical skills

| Area | Tools and experience |
|---|---|
| Backend and web applications | Python, FastAPI, React, TypeScript, REST APIs, PostgreSQL |
| AI and machine learning | PyTorch, scikit-learn, pandas, NLTK, Streamlit, Ollama |
| Industrial automation | Ignition, Siemens S7-1200 / S7-200 SMART, Modbus, PLC tag mapping, communication troubleshooting |
| Systems and engineering tooling | C, CSIM, Git, Docker, CI workflows, Python test suites |

## Run the portfolio locally

Use **Python 3.12**, the version used to check this update.

```bash
git clone https://github.com/sahelmain/Portfolio.git
cd Portfolio
python -m venv .venv
```

Activate the virtual environment:

```bash
# macOS / Linux
source .venv/bin/activate

# Windows PowerShell
.venv\Scripts\Activate.ps1
```

Install the existing dependencies and start the application:

```bash
python -m pip install -r requirements.txt
streamlit run app.py
```

Open `http://localhost:8501`. The app includes section navigation, project filters, a theme toggle, and source links. Its project information is curated locally; it does not query GitHub for live statistics.

## Connect

- **LinkedIn:** [Sahel Azzam](https://www.linkedin.com/in/sahel-azzam-0a0670223)
- **GitHub:** [sahelmain](https://github.com/sahelmain)
- **Email:** [saazzam@ttu.edu](mailto:saazzam@ttu.edu)
- **Location:** Amman, Jordan

Interested in software engineering, AI engineering, and industrial automation opportunities.
