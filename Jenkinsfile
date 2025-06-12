pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'docker build -t emmanuel-services:latest .'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
            }
        }
    }
}
