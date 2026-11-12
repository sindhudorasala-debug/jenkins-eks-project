pipeline {
    agent any

    stages {

        stage('Git Checkout') {
            steps {
                checkout scm
            }
        }

        stage('SonarQube Analysis') {
            steps {
                echo 'Running SonarQube Analysis'
            }
        }

        stage('OWASP Dependency Check') {
            steps {
                echo 'Running OWASP Dependency Check'
            }
        }

        stage('Trivy Security Scan') {
            steps {
                echo 'Running Trivy Scan'
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t movie-website:latest .'
            }
        }
        
        stage('ECR Login') {
    steps {
        sh '''
        aws ecr get-login-password --region ap-southeast-2 | docker login --username AWS --password-stdin 692436514545.dkr.ecr.ap-southeast-2.amazonaws.com
        '''
    }
}

        
stage('Docker Tag') {
    steps {
        sh '''
        docker tag movie-website:latest 692436514545.dkr.ecr.ap-southeast-2.amazonaws.com/my-appliction-ecr:latest
        '''
    }
}
        
       stage('Docker Push to ECR') {
            steps {
                echo 'ECR Push configuration pending'
            }
        }

        stage('Deploy to EKS') {
            steps {
             sh '''
        docker push 692436514545.dkr.ecr.ap-southeast-2.amazonaws.com/my-appliction-ecr:latest
        '''
            }
        }
    }
} 
