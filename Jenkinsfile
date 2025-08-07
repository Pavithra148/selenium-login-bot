pipeline {
  agent any

  tools {
    jdk 'jdk17'               // Replace 'jdk17' with your exact JDK name from Jenkins
    allure 'Allure-CLI'       // Should match the Allure tool name in Jenkins
  }

  environment {
    JAVA_HOME = "${tool 'jdk17'}"                     // Dynamically resolve the JDK path
    PATH = "${env.JAVA_HOME}\\bin;${env.PATH}"        // Append to PATH for CLI tools
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
