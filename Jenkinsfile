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
        bat 'pip install pytest pytest-html selenium'
      }
    }
    stage('Run Tests') {
      steps {
        bat 'python -m pytest test_salesforce.py --html=report.html'
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
    cd selenium_Practice
    if not exist Deployment mkdir Deployment
    copy report.html Deployment\\report.html
    '''
  }
}
  }
}
