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
                bat '''
                    call "selenium Practice\\.venv\\Scripts\\activate.bat"
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Pytest') {
            steps {
                bat '''
                    call "selenium Practice\\.venv\\Scripts\\activate.bat"
                    pytest --html=reports/Salesforce.html --self-contained-html
                '''
            }
        }

        stage('Archive Report') {
            steps {
                archiveArtifacts artifacts: 'reports/*.html', onlyIfSuccessful: true
            }
        }
    }
}
