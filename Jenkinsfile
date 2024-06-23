pipeline {
   agent any
  
   stages {
      stage ('Build') {
          steps {
              echo 'Building in development branch'
              //Build Steps Here
          }
      }

      stage('Deploy') {
          steps {
              echo 'Testing in development branch'
              //Test Steps Here
      }
     
      stage('Post-Deployment Tests') {
          steps {
             echo 'Running post-deployment tests in production'
          }
      }
   }
  }
}
