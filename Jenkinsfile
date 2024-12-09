pipeline {
    agent any
    environment {
        DOCKER_CREDENTIALS = credentials('docker-hub-credentials')
    }
    triggers {
        githubPush()
    }
    stages {
        stage('Check out') {
            steps {
               checkout scm
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    echo "Building Docker image..."
                    sh "docker build -t itaygoren/myapp:${env.BUILD_NUMBER} ."
                }
            }
        }
        stage('Push Docker Image') {
            steps {
                script {
                    echo "Logging in to Docker Hub..."
                    sh """
                    echo $DOCKER_CREDENTIALS_PSW | docker login -u $DOCKER_CREDENTIALS_USR --password-stdin
                    docker push itaygoren/myapp:${env.BUILD_NUMBER}
                    """
                }
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                sh '''
                sed -i 's/BUILD_NUMBER_PLACEHOLDER/'"${BUILD_NUMBER}"'/g' deployment.yaml
		kubectl apply -f deployment.yaml
                '''
            }
        }
    }
}
