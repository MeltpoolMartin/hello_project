pipeline {
  agent {
    docker {
      image 'python:3.7.3'
    }

  }
  stages {
    stage('Requirements') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }

    stage('Exec') {
      steps {
        sh 'python3 hello.py'
      }
    }

  }
}