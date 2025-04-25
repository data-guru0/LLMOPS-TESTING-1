pipeline{
    agent any

    environment {
        AWS_REGION = 'us-east-1'
        ECR_REPO = 'lllmops-repo'
        IMAGE_TAG = 'latest'
	}

    stages{
        stage('Cloning Github repo to Jenkins'){
            steps{
                script{
                    echo 'Cloning Github repo to Jenkins............'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/data-guru0/LLMOPS-TESTING-1.git']])
                }
            }
        }
        
    }
}