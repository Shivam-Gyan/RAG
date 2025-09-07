# MediBot Chat & Backend

A modern, interactive chatbot platform with **Next.js frontend** and **Python backend**.
Users can chat, upload PDFs, and interact with a dynamic UI powered by **Framer Motion**. The backend handles AI responses and file processing.
---

## Table of Contents

1. [Features](#features)
2. [Tech Stack](#tech-stack)
3. [Frontend Setup](#frontend-setup)
4. [Backend Setup](#backend-setup)
5. [Usage](#usage)
6. [Contributing](#contributing)
7. [Media](#media)
8. [License](#license)

---

## Features

* **Interactive Chat UI** with animated message bubbles
* **File Upload Support** (PDFs)
* **Dynamic Animations**: Navbar, chat, and messages with Framer Motion
* **Professional Design**: Rounded containers, clean colors, responsive layout
* **Backend AI Handling**: Processes messages and files for bot responses

---

## Tech Stack

**Frontend:** Next.js, React, Tailwind CSS, Framer Motion
**Backend:** Python 3.12, Flask / FastAPI (or your choice)
**Others:** Conda for virtual environment, pip for dependencies

---

## Frontend Setup

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/medibot-chat.git
cd medibot-chat
```

### 2. Install Dependencies

```bash
npm install
```

### 3. Run Development Server

```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) in your browser.

### 4. Optional Build for Production

```bash
npm run build
npm start
```

### 5. Project Structure

```
/app
  ├─ page.tsx          # Main page with navbar and chat
  └─ globals.css       # Tailwind CSS styles
/components
  ├─ ChatUI.tsx
  ├─ FileUpload.tsx
  └─ MessageBubble.tsx
/hooks
  └─ useChat.ts
/public
  └─ assets
```

---

## Backend Setup

### 1. Create Conda Virtual Environment

```bash
conda create -p venv python==3.12
```

### 2. Activate Environment

```bash
conda activate ./venv
```

### 3. Deactivate Environment

```bash
conda deactivate
```

### 4. Install Requirements

```bash
pip install -r requirements.txt
```

### 5. Run Backend Server

```bash
# Example using Flask
export FLASK_APP=app.py
export FLASK_ENV=development
flask run

# Or using FastAPI with uvicorn
uvicorn main:app --reload
```

The backend will run at [http://localhost:8000](http://localhost:8000).

---

## Usage

1. Open the frontend in your browser: [http://localhost:3000](http://localhost:3000)
2. Chat with MediBot using the input box.
3. Upload PDF files via drag-and-drop or click.
4. Messages appear dynamically with smooth animations.

---

## Contributing

1. Fork the repository.
2. Create a new branch:

```bash
git checkout -b feature/your-feature
```

3. Make changes and commit:

```bash
git commit -m "Add feature XYZ"
```

4. Push to your fork:

```bash
git push origin feature/your-feature
```

5. Create a Pull Request.

---

## Media

### Screenshots

![Chat UI](https://drive.google.com/uc?id=1M24POZbdxPdGFEwHSQEf_Nf4ipbbYW-Y)


---

