pipeline {
    agent any
    environment {
        VENV_DIR = "${WORKSPACE}/venv"
    }
    stages {
        stage('Setup') {
            steps {
                script {
                    // Create a virtual environment
                    if (!fileExists(VENV_DIR)) {
                        sh 'python -m venv ${VENV_DIR}'
                    }
                    // Activate the virtual environment and install dependencies
                    sh '. ${VENV_DIR}/bin/activate && pip install -r requirements.txt'
                }
            }
        }
        stage('Train') {
            when {
                anyOf {
                    branch 'development'
                    branch 'staging'
                }
            }
            steps {
                script {
                    sh '. ${VENV_DIR}/bin/activate && python train.py'
                }
            }
        }
        stage('Test') {
            when {
                anyOf {
                    branch 'development'
                    branch 'staging'
                }
            }
            steps {
                script {
                    sh '. ${VENV_DIR}/bin/activate && python evaluate.py'
                }
            }
        }
        stage('Deploy to Staging') {
            when {
                branch 'staging'
            }
            steps {
                script {
                    sh '. ${VENV_DIR}/bin/activate && python deploy.py'
                }
            }
        }
        stage('Deploy to Production') {
            when {
                branch 'production'
            }
            steps {
                script {
                    sh '. ${VENV_DIR}/bin/activate && python deploy.py'
                }
            }
        }
    }
    post {
        always {
            cleanWs()
        }
    }
}

<<<<<<< HEAD
      stage('Deploy') {
          steps {
              echo 'Testing in development branch'
              //Test Steps Here
          }
      }
     
      stage('Post-Deployment Tests') {
          steps {
             echo 'Running post-deployment tests in production'
          }
      }
   }
}

=======
>>>>>>> 45c3b45 (commit)
