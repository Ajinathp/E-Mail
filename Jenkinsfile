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
                echo SMTP_USER=%SMTP_USER%
                echo SMTP_PASS=%SMTP_PASS%
                python -m pip install --upgrade pip
                python email.py
                '''
            }
        }
    }
}
