pipeline {
    agent any

    stages {
        stage('Run Email Script') {
            steps {
                bat '''
                python -m pip install --upgrade pip
                python send_email.py
                '''
            }
        }
    }
}
