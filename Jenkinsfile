pipeline {
  agent any
  tools {
    allure 'Allure' // This must match the name in Jenkins > Global Tool Configuration
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
        bat 'pip install pytest allure-pytest selenium'
      }
    }
    stage('Run Tests') {
      steps {
        bat 'pytest test_salesforce.py --alluredir=allure-results'
      }
    }
    stage('Allure Report') {
      steps {
        allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
      }
    }
  }
}
