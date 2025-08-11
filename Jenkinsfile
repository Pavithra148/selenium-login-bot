pipeline {
    agent any

    triggers {
        githubPush()
    }

    tools {
        git 'TestG'
        jdk 'jdk-17'
        allure 'Allure-CLI'
    }

    stages {
        stage('Clean Workspace') {
            steps {
                cleanWs()
            }
        }

        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/Pavithra148/selenium-login-bot.git', changelog: false, poll: false
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install --upgrade pip'
                bat 'pip install pytest allure-pytest selenium'
            }
        }

        stage('Prepare Allure Results Folder') {
            steps {
                bat 'if not exist allure-results mkdir allure-results'
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    dir("${WORKSPACE}") {
                        def exitCode = bat(script: 'python -m pytest test_salesforce.py --alluredir=allure-results', returnStatus: true)
                        if (exitCode != 0) {
                            error "Tests failed with exit code ${exitCode}"
                        }
                    }
                }
            }
        }

        stage('Debug Allure Results Folder') {
            steps {
                bat 'echo ===== Contents of allure-results ====='
                bat 'dir allure-results'
                bat 'echo ===== File details ====='
                bat 'dir allure-results /s'
            }
        }

        stage('Generate Allure Report') {
            steps {
                script {
                    if (fileExists('allure-results') && !isFolderEmpty('allure-results')) {
                        allure includeProperties: false, results: [[path: 'allure-results']]
                    } else {
                        echo "⚠ No Allure results found — skipping report generation"
                    }
                }
