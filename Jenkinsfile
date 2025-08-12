pipeline {
    agent any

    tools {
        python 'Python3' // Configure this in Jenkins → Manage Jenkins → Tools → Python Installations
    }

    environment {
        PATH = "$PATH:/usr/local/bin"
    }

    stages {
        stage('Install Python Dependencies') {
            steps {
                sh '''
                python3 -m pip install --upgrade pip
                pip install pytest selenium webdriver-manager allure-pytest
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                pytest --maxfail=1 --disable-warnings \
                --alluredir=allure-results
                '''
            }
        }

        stage('Generate Allure Report') {
            steps {
                allure([
                    includeProperties: false,
                    jdk: '',
                    results: [[path: 'allure-results']]
                ])
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished!'
        }
        failure {
            echo 'Pipeline failed! Check logs.'
        }
    }
}
