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
        stage('Run Docker Image') {
            steps {
                script {
                    echo "Running Docker image..."
                    sh "docker run -d --name mytestapp -p 5000:5000 itaygoren/myapp:${env.BUILD_NUMBER}"
                }
            }
        }
        stage('Testing the app') {
            steps {
                script {
                    echo "Testing the application..."
                    sh """
		    sleep 2
		    curl http://localhost:5000 | grep good
		    """
                }
            }
        }
       stage('Push Docker Image') {
    steps {
        script {
            echo "Logging in to Docker Hub..."
            withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                sh '''
                echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                docker push itaygoren/myapp:${BUILD_NUMBER}
                '''
            }
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
	post {
        	success {
            	   echo 'Pipeline succeeded.'
        	}
        	failure {
            	   echo 'Pipeline failed.'
        	}
        	always {
            	   echo "Clean up."
	    	   sh """
	    	   echo "Checking for running Docker containers..."
            	   docker ps -q | xargs -r docker stop || echo "No running containers to stop."
            	   docker ps -aq | xargs -r docker rm || echo "No containers to remove."
            	   echo "Docker cleanup completed."
	    	   """
        }
    }
}

