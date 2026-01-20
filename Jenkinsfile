pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Ajinathp/E-Mail.git'
            }
        }

        stage('Run Script') {
            steps {
                bat 'python main.py'
            }
        }
    }
}
