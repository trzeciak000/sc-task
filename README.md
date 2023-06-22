# Test project sc-task

Sc-task is simple project, API for downloading laster 100 jokes from sitebash.org.pl and return them in JSON.
<br />How to run project:
    
    cd /path/to/project/app
    python3 app.py
    #### Go to localhost:5000/jokes and check if it works

Build docker image:

    cd /path/to/project/
    docker build .

Use docker-compose to build and run deployment:

    cd /path/to/project/deployment/docker
    docker-compose build
    docker-compose up -d
    #### Go to localhost:5000/jokes and check if it works

Kubertnetes deployments:<br />
Basic deployment:

    cd /path/to/project/deployment/k8s
    kubectl apply -f base
    ## Port forward to test:
    kubectl port-forward sc-task-${ID} 5000:5000
    #### Go to localhost:5000/jokes and check if it works

Staging deployment (change namespace with kustomize):

    ## Create namespace staging:
    kubectl create ns staging
    cd /path/to/project/deployment/k8s
    kubectl apply -f environments/stagins
    ## Port forward to test:
    kubectl port-forward sc-task-${ID} 5000:5000
    #### Go to localhost:5000/jokes and check if it works

Helm deployment:

    cd /path/to/project/deployment
    helm install sc-task-chart helmsctask/ --values helmsctask/values.yaml
    ## Verify with kubectl command