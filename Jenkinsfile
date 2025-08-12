pipeline {
    agent any

    tools {
        jdk 'jdk-17'
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
                pytest --maxfail=1 --disable-warnings -q \
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
