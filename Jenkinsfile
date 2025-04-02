pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Set up Python') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }
        
        stage('Run Tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    python -m pytest test_hello_world.py -v
                '''
            }
        }
        
        stage('Run Application') {
            steps {
                sh '''
                    . venv/bin/activate
                    python hello_world.py
                '''
            }
        }
    }
    
    post {
        always {
            cleanWs()
        }
    }
} 