# Set up postgres sql in minikube
I choose the Minikube environment to set up and test the installation of PostgreSQL 

## 1. Set up tool kubectl:


The Kubernetes command-line tool, kubectl, allows you to run commands against Kubernetes clusters. You can use kubectl to deploy applications, inspect and manage cluster resources, and view logs.

Install according to the link: https://kubernetes.io/docs/tasks/tools/install-kubectl-windows/

## 2. Set up minikube environment:

- minikube is local Kubernetes, focusing on making it easy to learn and develop for Kubernetes.
- All you need is Docker (or similarly compatible) container or a Virtual Machine environment, and Kubernetes is a single command away: minikube start
- Install according to the link: https://minikube.sigs.k8s.io/docs/start/


## 3. Deployment a postgres in minikube:
- From a terminal start cluster:
  ```
     minikube start
  ```
- Create a namespace to contain postgres named postgres:
  ```
     kubectl create ns postgres
  ```
- Apply files .yaml to deploy postgres:
  ```
     kubectl apply -f configmap.yaml -n postgres
     kubectl apply -f PersistentVolume.yaml -n postgres
     kubectl apply -f PersistentVolumeClaim.yaml -n postgres
     kubectl apply -f StatefulSet.yaml -n postgres
     kubectl apply -f service.yaml -n postgres
  ```

## 4. Write data to postgres in minikube:


Run connect.py in code environment to write data to postgres (Note: Correct the csv file path and ip address postgres)


