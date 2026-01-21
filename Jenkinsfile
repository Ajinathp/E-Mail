pipeline {
    agent any

    stages {
        stage('Run Email Script') {
            steps {
                bat 'python smtp_mailer.py'
            }
        }
    }
}
