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
                sh 'python -m pip install --upgrade pip'
                sh 'pip install -r requirements.txt'
            }
        }
        
        stage('Run Tests') {
            steps {
                sh 'python -m pytest test_hello_world.py -v'
            }
        }
        
        stage('Run Application') {
            steps {
                sh 'python hello_world.py'
            }
        }
    }
    
    post {
        always {
            cleanWs()
        }
    }
} 