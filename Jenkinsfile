pipeline {
  agent {
    docker {
      image 'python:windowsservercore-ltsc2016'
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

    stage('Build') {
      steps {
        sh 'pyinstaller hello.py'
      }
    }

  }
}