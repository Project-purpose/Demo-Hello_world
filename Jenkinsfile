pipeline {
   agent any
   stages {
      stage('Code Checkout') {
         steps {
               git credentialsId: 'GithubID', url: 'https://github.com/Project-purpose/Demo-SUM.git' 
         }
      }
   
      stage('Docker Build') {
         steps {
                 def app = docker.build "ashhh24/newsum"
      }
    }
  }
}
