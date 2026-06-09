# Travel AI Call Assistant

An AI-powered virtual travel agent built with FastAPI, LangChain, OpenAI, and SQLAlchemy.

The project simulates a real travel agency phone assistant capable of identifying customers, retrieving reservations, checking payments, and answering travel-related questions through natural language conversations.

The long-term goal is to evolve this prototype into a production-ready voice agent integrated with telephony providers, external travel APIs, knowledge bases, and workflow orchestration.

---

## Features

### Customer Lookup

Search customers by phone number and retrieve registered information.

### Reservation Lookup

Search reservations using a unique reservation code.

### Payment Lookup

Retrieve payment status, due dates, and reservation-related financial information.

### AI Agent

Natural language agent powered by OpenAI and LangChain.

The agent can:

* Understand customer requests
* Decide which tool to use
* Access customer data
* Access reservation data
* Access payment data
* Maintain conversational context

### Web Interface

Simple FastAPI frontend for testing conversations directly in the browser.

---

## Current Technology Stack

### Backend

* FastAPI

### AI

* LangChain
* OpenAI GPT-4o Mini

### Database

* SQLite
* SQLAlchemy ORM

### Frontend

* HTML
* JavaScript
* Jinja2 Templates

### Environment Management

* Python Dotenv

---

## Project Structure

```text
Project-ia-call/
│
├── app/
│   ├── agent/
│   │   └── travel_agent.py
│   │
│   ├── database/
│   │   ├── connection.py
│   │   ├── models.py
│   │   └── seed.py
│   │
│   ├── services/
│   │   └── agent_service.py
│   │
│   ├── tools/
│   │   ├── cliente_tool.py
│   │   ├── reserva_tool.py
│   │   └── pagamento_tool.py
│   │
│   ├── state/
│   │
│   ├── static/
│   │
│   ├── templates/
│   │
│   └── main.py
│
├── data/
│   └── travel.db
│
├── tests/
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Database Model

### Customers

Stores customer information:

* Name
* Phone number
* Email

### Reservations

Stores travel reservations:

* Reservation code
* Destination
* Origin
* Travel date
* Number of passengers
* Reservation status
* Total value

### Payments

Stores payment information:

* Reservation reference
* Amount
* Status
* Due date

---

## Installation

### Clone the repository

```bash
git clone <repository-url>
cd Project-ia-call
```

### Create virtual environment

```bash
python -m venv venv
```

### Activate virtual environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_api_key_here
```

---

## Create Database

```bash
python -m app.criar_db
```

---

## Seed Sample Data

```bash
python -m app.database.seed
```

---

## Run Application

```bash
uvicorn app.main:app --reload
```

Application will be available at:

```text
http://127.0.0.1:8000
```

---

## Example Requests

### Customer Lookup

```text
My phone number is 88999998888
```

### Reservation Lookup

```text
Check reservation 12000001
```

### Payment Lookup

```text
Check payment for reservation 12000001
```

---

## Project Goal

The objective of this project is to build a production-grade AI travel assistant capable of handling customer interactions over phone calls, accessing company data sources, consulting travel information, answering policy questions, and managing reservations autonomously while maintaining a natural conversational experience.
