# Music Matcher

## Overview
Music Matcher is a web application that matches songs to user preferences using machine learning. It consists of a FastAPI backend and a React frontend.

## Tech Stack
- **Backend:** Python 3.10+, FastAPI, SQLAlchemy, psycopg2-binary, scikit-learn, pandas, python-dotenv
- **Frontend:** Node 18+, Vite, React, TypeScript

## Local Development
### Prerequisites
- Python 3.10 or newer
- Node.js 18 or newer
- Poetry (for Python dependencies)

### Setup
1. Install Python dependencies:
   ```bash
   cd backend
   poetry install
   ```
2. Install frontend dependencies:
   ```bash
   cd ../frontend
   npm install
   ```
3. Start development servers:
   ```bash
   # In one terminal
   cd backend
   poetry run uvicorn main:app --reload

   # In another terminal
   cd frontend
   npm run dev
   ```
