node {
   stage('Code Checkout') {
     git credentialsId: 'githubID', url: 'https://github.com/Project-purpose/Demo-SUM.git' 
   }
   stage('Docker Build') {
     def app = docker build .
    }
}
