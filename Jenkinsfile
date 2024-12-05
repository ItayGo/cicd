pipeline {
    agent any
    environment {
        DOCKER_CREDENTIALS = credentials('docker-hub-credentials')
    }
    triggers {
    githubPush()
    }
    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/ItayGo/cicd.git', credentialsId: 'github-credentials'
            }
        }

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    echo "Building Docker image..."
                    sh "docker build -t itaygo/cicd-app:latest ."
                }
            }
     stage('Push Docker Image') {
            steps {
                script {
                    echo "Logging in to Docker Hub..."
                    sh """
                    echo $DOCKER_CREDENTIALS_PSW | docker login -u $DOCKER_CREDENTIALS_USR --password-stdin
                    docker push itaygo/cicd-app:latest
                    """
                }
            }
        }
    }
}

