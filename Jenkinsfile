pipeline {
   agent any
   stages{
      stage("Code Checkout") {
         steps {
               echo 'App build started..'
               git credentialsId: 'githubID', url: 'https://github.com/Project-purpose/Demo-SUM.git' 
         }
      }
   
      stage('Docker Build') {
         steps {
                 def app = docker build .
         }
      }
   }
}
