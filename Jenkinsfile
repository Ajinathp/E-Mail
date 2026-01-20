pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Ajinathp/E-Mail.git'
            }
        }

        stage('Run Email Script') {
            steps {
                bat '''
                python -m pip install --upgrade pip
                python email_2.py
                '''
            }
        }
    }
}

