stage('Check Python') {
    steps {
        bat 'python --version'
        bat 'where python'
    }
}
