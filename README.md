# Research Assistant

This is a simple web application that acts as an AI research assistant. Users can submit research requests, and the system retrieves relevant information from the web.

## Tech Stack

- **Backend**: Python 3.10+ with FastAPI
- **Frontend**: Static HTML + JavaScript
- **Deployment**: Docker
- **AI/ML**: Google AI Search API

## Project Structure

```
research_assistant/
├── Dockerfile
├── README.md
├── main.py
├── requirements.txt
├── static/
│   ├── index.html
│   ├── services.html
│   ├── community.html
│   └── how-we-roll.html
└── .env
```

## Prerequisites

- Docker Desktop installed and running
- Google AI Search API key

## Setup

1. **Clone the repository** (if you haven't already):

   ```bash
   git clone <repository-url>
   cd research_assistant
   ```

2. **Create a `.env` file** in the root directory:

   ```bash
   touch .env
   ```

3. **Add your API key** to `.env`:

   ```env
   GOOGLE_API_KEY="your-api-key-here"
   ```

## Running the Application

### Using Docker

1. **Build the Docker image**:

   ```bash
   docker build -t research-assistant .
   ```

2. **Run the container**:

   ```bash
   docker run -p 8000:8000 --env-file .env research-assistant
   ```

3. **Access the application**: Open [http://localhost:8000](http://localhost:8000) in your browser.

## API Endpoints

- **GET /** - Serves the homepage
- **GET /how-we-roll** - Serves the "How We Roll" page
- **GET /services** - Serves the "Services" page
- **GET /community** - Serves the "Community" page
- **POST /research** - Accepts research requests

## License

MIT © 2026 Adapting Minds
