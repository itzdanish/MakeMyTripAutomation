pipeline {
    agent any  // run on any Jenkins agent

    stages {
        stage('Install Dependencies') {
            steps {
                echo 'Installing required Python packages...'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running Selenium + Pytest tests...'
                sh 'pytest tests/ --html=report.html --self-contained-html'
            }
        }
    }

    post {
        always {
            echo 'Publishing Test Report...'
            publishHTML(target: [
                allowMissing: false,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: '.',
                reportFiles: 'report.html',
                reportName: 'Test Report'
            ])
        }
    }
}
