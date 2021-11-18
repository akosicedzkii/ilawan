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
    steps {
        sh 'python -m pip install requirements.txt'
    }
}
  stage('build') {
    steps {
        sh 'python main.py'
    }
}
}