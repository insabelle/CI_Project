pipeline {

    agent any

    stages {

        stage('Clonage') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/insabelle/CI_Project.git'
            }
        }

        stage('Vérification Python') {
            steps {
                bat 'python --version'
                bat 'pip --version'
            }
        }

        stage('Installation des dépendances') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Tests unitaires') {
            steps {
                bat 'pytest'
            }
        }
    }

    post {

        always {
            echo 'Pipeline terminé'
        }

        success {
            echo 'Tous les tests ont réussi'
        }

        failure {
            echo 'Des erreurs ont été détectées'
        }
    }
}