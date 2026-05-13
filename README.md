# Nginx Log to CSV Automation

A DevOps tool to parse Nginx logs, generate CSV reports, and automate Git synchronization.

## How it works
1. *Parsing:* Uses Regex to extract IP, Time, Method, URL, Status, and Size.
3. *Processing:* Sorts data by IP address and applies optional HTTP status filters.
4. *Automation:* Automatically performs `git add`, `commit`, and `push` to keep your reports updated in the repository.

## Prerequisites
To ensure the automation works smoothly, prepare your environment:
- *Log File:* Ensure `nginx.log` is present in the root directory.
- *Git Setup:* Initialize the repo (`git init`) and set your identity:
```
git config user.name "Your Name"
git config user.email "your@email.com"
```
- *Authentication:* Use *SSH* for pushing without entering passwords manually.

## Local Execution
If you have Python 3 installed locally, you can run the script directly:
```
# Process all logs
python3 parser.py

# Filter by specific status (e.g., 200 or 404)
python3 parser.py 200
```

## Docker Production Mode
The preferred way to run this tool is via Docker.
1. Build the image
```
docker build -t log-parser .
```
2. Run with Secure Git Access
```
docker run -v $(pwd):/app -v ~/.ssh:/root/.ssh:ro log-parser
```