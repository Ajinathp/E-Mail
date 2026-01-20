pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Ajinathp/E-Mail.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install --upgrade pip'
                bat 'pip install pywin32'
                // If you have requirements.txt in repo:
                // bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Script') {
            steps {
                bat 'python email.py'
            }
        }
    }
}
