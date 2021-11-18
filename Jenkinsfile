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
  stage('pip install') {
        sh 'pip install requirements.txt -i https://pypi.python.org/simple/'
}
  stage('run') {
        sh 'python main.py &'
    
}
}