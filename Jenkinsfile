pipeline {
    agent any

    stages {
        stage('Run Email Script') {
            steps {
                bat '''
                python -m pip install --upgrade pip
                bat send_email.py
                '''
            }
        }
    }
}
