node {
  stage('SCM') {
    checkout scm
  }
  stage('SonarQube Analysis') {
    def scannerHome = tool 'SonarScanner';
    withSonarQubeEnv() {
      sh "${scannerHome}/bin/sonar-scanner"
    }
  }
  stage('build') {
        sh 'pip install requirements.txt'
}
  stage('build') {
        sh 'python main.py &'
    
}
}