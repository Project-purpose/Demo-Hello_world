pipeline {
   agent any
   stages {
      stage('Code Checkout') {
         steps {
               git credentialsId: 'GithubID', url: 'https://github.com/Project-purpose/Demo-SUM.git' 
         }
      }
   
      stage('Docker Build') {
     def app = docker.build "ashhh24/newsum"
    }
   
   stage("Tag & Push image"){
      withDockerRegistry([credentialsId: 'dockerID',url: "https://hub.docker.com/u/ashhh24"]) {
          sh 'docker tag ashhh24/newsum ashhh24/newsum:dev'
          sh 'docker push ashhh24/newsum:dev'
          sh 'docker push ashhh24/newsum:latest'
                    
      }
    }
  }
}
