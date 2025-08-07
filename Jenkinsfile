pipeline {
  agent any

  tools {
    allure 'Allure' // This must match the name configured in Jenkins -> Global Tool Configuration
  }

  stages {
    stage('Checkout Code') {
      steps {
        git branch: 'main', url: 'https://github.com/Pavithra148/selenium-login-bot.git'
      }
    }

    stage('Install Dependencies') {
      steps {
        bat 'python -m pip install --upgrade pip'
        bat 'pip install pytest pytest-html selenium allure-pytest'
      }
    }

    stage('Run Tests') {
      steps {
        bat 'pytest test_salesforce.py --alluredir=allure-results'
      }
    }

    stage('Archive HTML Report') {
      steps {
        archiveArtifacts artifacts: 'report.html', onlyIfSuccessful: true
      }
    }

    stage('Archive Allure Results') {
      steps {
        archiveArtifacts artifacts: 'allure-results/**', allowEmptyArchive: true
      }
    }

    stage('Copy Report to Deployment Folder') {
      steps {
        bat '''
        if not exist selenium_Practice\\Deployment mkdir selenium_Practice\\Deployment
        copy report.html selenium_Practice\\Deployment\\report.html
        '''
      }
    }
  }

  post {
    always {
      allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
    }
  }
}
