node {
  stage('SCM') {
    checkout scm
  }
  // stage('SonarQube Analysis') {
  //   def scannerHome = tool 'SonarScanner';
  //   withSonarQubeEnv() {
  //     sh "${scannerHome}/bin/sonar-scanner"
  //   }
  // }
  stage('run python') {
      withEnv(["HOME=${env.WORKSPACE}"]) {
          sh 'pip3 install --user -r requirements.txt'
          sh 'python3 main.py > log.txt 2>&1 &'
      }
  } 
}
