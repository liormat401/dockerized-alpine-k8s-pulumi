# Dockerized-alpine-k8s-pulumi
This project demonstrates deploying a simple Dockerized Nginx server on a Kubernetes (k8s) cluster using Pulumi.

## Goal

The goal of this project is to create a Dockerfile based on Alpine Linux with an Nginx server, build it, and deploy it on a Kubernetes cluster using Pulumi.

## Technologies

- Kubernetes (k8s)
- Docker
- Pulumi

## Instructions

### 1. Setting up the enviroment

Install:

- Kubernetes cluster,Minikube 
- Docker cli
- kubectl
- pulumi cli
- Nginx engine

### 2. Dockerfile

Create a simple Dockerfile based on Alpine Linux that includes an Nginx server.

### 3. Build Docker Image

Build the Docker image using the Dockerfile.

### 4. Pulumi Deployment

Created Pulumi deployment using a language of Python,that will:

a. Create a Kubernetes Deployment for Nginx with 4 pods, specifying resources requests & limits, and volume mount for persistent volume.

b. Create a Kubernetes Service to expose the Nginx ports with HTTP & HTTPS.

used NodePort.

### 5. Deploy Pulumi Stack

Deployed the Pulumi stack on the Kubernetes cluster and verify that it's running correctly.



### 6. Serve HTML Web Page

Configured the Nginx server to serve a static HTML webpage.

Access the webpage using port forwarding locally or by minikube ip:nodeport ip

kubectl port-forward svc/nginxweb-b37dce79 8080:80


## Troubleshooting

### ImagePullBackOff Error: ###

Cause: Kubernetes had trouble pulling the nginx-alpine image.

Solution: Double-check the image name (nginx:alpine) and verify Docker Hub credentials for private repositories.

### ReplicaSet Timed Out Error: ###

Cause: The ReplicaSet timed out progressing, possibly due to resource limitations or network issues.

Solution: Ensure sufficient resources in the Kubernetes cluster (CPU, memory) and verify network connectivity.

Commands:

kubectl get pods

kubectl describe deployment <deployment-name>

### NodeNotReady ###
Cause: 
- Insufficient Resources: The node might not have enough resources (CPU, memory) to run additional pods, causing it to be in a "NotReady" state.

- System Overload: The node might be overloaded with processes or applications, causing it to become unresponsive or slow in accepting new workloads.

- Network Issues: Network problems, such as difficulty communicating with the Kubernetes control plane or other nodes, can lead to a "NodeNotReady" status.

- Node Failure: The node might have experienced a failure or crash, rendering it unable to accept new pods.

Solution: View Node Events, Check Resource Utilization on a Node,Restart Node/Minikube(if all nodes in NodeNotReady)

Commands:

kubectl get nodes

kubectl describe node <node-name>

kubectl get events --field-selector type=Warning

- Check Node Resource Utilization:
  
kubectl top node <node-name>

- Modify your Minikube configuration to allocate more resources:
  
minikube config set memory (size)

minikube config set cpus (count)

- Restart Minikube for changes to take effect
  
minikube stop

minikube start

