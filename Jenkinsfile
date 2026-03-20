pipeline {
    agent {
        docker {
            image 'python:3.11'
            args '-v /var/run/docker.sock:/var/run/docker.sock'
        }
    }
    stages {
        stage('Clone') {
            steps {
                git branch: 'main', url: 'https://github.com/01aadii/playwright_demo.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
                bat 'python -m playwright install'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'python test.py'
            }
        }
    }
}
