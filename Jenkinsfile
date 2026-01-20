pipeline {
    agent any

    environment {
        SMTP_USER = credentials('smtp-user')   // Jenkins credential ID
        SMTP_PASS = credentials('smtp-pass')   // Jenkins credential ID
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Ajinathp/E-Mail.git'
            }
        }

        stage('Run Script') {
            steps {
                bat '''
                python -m pip install --upgrade pip
                python email.py
                '''
            }
        }
    }
}
