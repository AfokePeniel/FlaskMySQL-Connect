# Flask Redis Visit Counter

A simple Flask web application that counts visits using Redis as a counter storage.

## Description

This application demonstrates a basic integration between Flask and Redis, where each visit to the homepage increments a counter stored in Redis. It's containerized using Docker and orchestrated with Docker Compose.

## Prerequisites Installation

### Install Python (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install python3
python3 --version  # Verify installation
```

### Install Docker
1. Update package index and install prerequisites:
```bash
sudo apt update
sudo apt install apt-transport-https ca-certificates curl software-properties-common
```

2. Add Docker's official GPG key:
```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
```

3. Add Docker repository:
```bash
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

4. Install Docker:
```bash
sudo apt update
sudo apt install docker-ce docker-ce-cli containerd.io
```

5. Verify Docker installation:
```bash
sudo docker --version
```

### Install Docker Compose
1. Download Docker Compose:
```bash
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```

2. Apply executable permissions:
```bash
sudo chmod +x /usr/local/bin/docker-compose
```

3. Verify installation:
```bash
docker-compose --version
```

### Additional Resources
- [Official Python Installation Guide](https://www.python.org/downloads/)
- [Official Docker Installation Documentation](https://docs.docker.com/engine/install/)
- [Official Docker Compose Installation Documentation](https://docs.docker.com/compose/install/)

## Project Structure

FlaskRedis-Counter/
├── app.py # Main Flask application
├── requirements.txt # Python dependencies
├── Dockerfile # Docker container configuration
├── docker-compose.yml # Docker services orchestration
└── README.md # Documentation

## Installation & Setup

### Using Docker (Recommended)

1. Build and run the containers:
```bash
docker-compose up --build
```

2. Access the application at `http://localhost:5000`

### Local Development Setup

1. Create and activate virtual environment:
```bash
sudo apt install python3-venv  # For Ubuntu/Debian
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Visit `http://localhost:5000` in your web browser. Each visit will increment a counter, and the page will display the total number of visits.

## Dependencies

```
Flask==2.0.1
redis==4.5.1
Werkzeug==2.0.1
```

## Docker Services

The application uses two Docker containers:
- **web**: Flask application container
- **redis**: Redis database container

## Troubleshooting

If you encounter any issues:

1. Check if containers are running:
```bash
docker-compose ps
```

2. View application logs:
```bash
docker-compose logs
```

3. Restart services:
```bash
docker-compose down
docker-compose up --build
```