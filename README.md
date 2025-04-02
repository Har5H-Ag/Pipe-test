# Hello World Python Project with Jenkins CI/CD

This is a simple Python project that demonstrates Jenkins CI/CD integration with GitLab.

## Project Structure

- `hello_world.py`: Main application file
- `test_hello_world.py`: Test cases
- `requirements.txt`: Project dependencies
- `Jenkinsfile`: Jenkins pipeline configuration

## Local Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run tests:
```bash
python -m pytest test_hello_world.py -v
```

4. Run the application:
```bash
python hello_world.py
```

## Jenkins Setup

1. Create a new Jenkins pipeline project
2. Configure GitLab integration:
   - Add GitLab credentials in Jenkins
   - Configure webhook in GitLab to trigger Jenkins builds
3. Point to your GitLab repository
4. Set the pipeline script to use the Jenkinsfile from SCM

## GitLab Webhook Configuration

1. Go to your GitLab project settings
2. Navigate to Webhooks
3. Add a new webhook:
   - URL: `http://your-jenkins-url/project/your-project-name`
   - Trigger on: Push events
   - Secret token: (if configured in Jenkins)

## Pipeline Stages

1. Checkout: Clones the repository
2. Set up Python: Installs dependencies
3. Run Tests: Executes pytest
4. Run Application: Runs the hello world script 