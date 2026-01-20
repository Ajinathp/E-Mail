pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Ajinathp/E-Mail.git'
            }
        }

        stage('Run Script') {
            steps {
                // Replace script.py with your actual Python file
                sh 'email.py'
            }
        }
    }
}
