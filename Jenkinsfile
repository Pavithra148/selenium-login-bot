pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/Pavithra148/selenium-login-bot.git'
            }
        }

stage('Install Dependencies') {
            steps {
                bat 'python -m pip install --upgrade pip'
                bat 'pip install pytest pytest-html'
            }
        }
        stage('Run Tests') {
            steps {
                bat 'python -m pytest selenium_Practice/test_salesforce.py --html=selenium_Practice/report.html'
            }
        }

        stage('Archive Report') {
            steps {
                archiveArtifacts artifacts: 'selenium_Practice/report.html', onlyIfSuccessful: true
            }
        }

        stage('Copy Report to Deployment Folder') {
            steps {
                bat '''
                cd selenium_Practice
                mkdir Deployment
                copy report.html Deployment\\report.html
                '''
            }
        }
    }
}
