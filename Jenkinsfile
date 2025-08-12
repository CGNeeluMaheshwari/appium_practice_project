pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
        REPORT_FILE = 'report.html'
        DEVICE_NAME = 'Android Emulator' // Customize as needed
        PLATFORM_NAME = 'Android'
        APP_PATH = 'C:/Users/nmaheshw/app/mda-2.2.0-25.apk' // Update with actual path
    }

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/CGNeeluMaheshwari/appium_practice_project.git', branch: 'master'
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                    python3 -m venv $VENV_DIR
                    source $VENV_DIR/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Start Appium Server') {
            steps {
                sh '''
                    nohup appium > appium.log 2>&1 &
                    sleep 10
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    source $VENV_DIR/bin/activate
                    pytest tests/ --html=$REPORT_FILE --self-contained-html -n auto
                '''
            }
        }

        stage('Stop Appium Server') {
            steps {
                sh '''
                    kill $(lsof -t -i:4723)
                '''
            }
        }

        stage('Publish Report') {
            steps {
                publishHTML([
                    reportDir: '.',
                    reportFiles: "$REPORT_FILE",
                    reportName: 'Test Report'
                ])
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            sh 'rm -rf $VENV_DIR'
        }
    }
}
