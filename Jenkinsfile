pipeline {
    agent any

    triggers {
        githubPush() // Run on GitHub webhook push
    }

    tools {
        jdk 'jdk-17'               // Your configured JDK
        allure 'Allure-CLI'        // Your configured Allure CLI tool
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

        stage('Debug Allure Results') {
            steps {
                bat 'dir allure-results'
            }
        }

        stage('Generate Allure Report') {
            steps {
                allure includeProperties: false, results: [[path: 'allure-results']]
            }
        }

        stage('Debug Allure Report Folder') {
            steps {
                bat 'dir allure-report'
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
        echo "Build result at end: ${currentBuild.currentResult}"
    }
    success {
        echo 'Pipeline succeeded'
    }
    failure {
        echo 'Pipeline failed'
    }
    unstable {
        echo 'Pipeline is unstable'
    }
}

}
