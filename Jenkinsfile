pipeline {
  agent any

  environment {
    JAVA_HOME = 'C:\\Program Files\\Eclipse Adoptium\\jdk-17.0.9.0-hotspot'
    PATH = "${env.JAVA_HOME}\\bin;${env.PATH}"
  }

  tools {
    allure 'Allure-CLI' // This must match the name in Jenkins > Global Tool Configuration
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
        bat 'python -m pytest test_salesforce.py --alluredir=allure-results'
      }
    }

    stage('Allure Report') {
      steps {
        allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
      }
    }

    stage('Archive Allure Report') {
      steps {
        archiveArtifacts artifacts: 'allure-report/**', allowEmptyArchive: true
      }
    }

    stage('Clean Workspace') {
      steps {
        cleanWs()
      }
    }
  }

  post {
    always {
      echo 'Pipeline finished'
    }
    success {
      echo 'Pipeline succeeded'
    }
    failure {
      echo 'Pipeline failed'
    }
  }
}
