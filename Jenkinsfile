pipeline {
    agent any

    stages {
        stage('Run Outlook Script') {
            steps {
                bat '''
                python email.py
                '''
            }
        }
    }
}

