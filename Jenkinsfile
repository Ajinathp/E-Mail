pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Ajinathp/E-Mail.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                // If you have requirements.txt
                //#sh 'python -m pip install --upgrade pip'
                //#sh 'pip install -r requirements.txt'
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
