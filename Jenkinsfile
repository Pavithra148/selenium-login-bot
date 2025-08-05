pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/Pavithra148/selenium-login-bot.git'
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                call "selenium Practice\\.venv\\Scripts\\activate.bat"
                pytest test_salesforce.py --html=report.html
                '''
            }
        }

        stage('Archive Report') {
            steps {
                archiveArtifacts artifacts: 'report.html', onlyIfSuccessful: true
            }
        }

        stage('Copy Report to Deployment Folder') {
            steps {
                bat '''
                mkdir "Deployment"
                copy report.html "Deployment\\report.html"
                '''
            }
        }
    }
}
