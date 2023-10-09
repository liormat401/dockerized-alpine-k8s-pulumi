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

Installed
Kubernetes cluster,Minikube 
Docker cli
kubectl
pulumi cli
Nginx engine

### 2. Dockerfile

Create a simple Dockerfile based on Alpine Linux that includes an Nginx server.

### 3. Build Docker Image

Build the Docker image using the Dockerfile.

### 4. Pulumi Deployment

Created Pulumi deployment using a language of Python,that will:

a. Create a Kubernetes Deployment for Nginx with 4 pods, specifying resources requests & limits, and volume mount for persistent volume.
b. Create a Kubernetes Service to expose the Nginx ports with HTTP & HTTPS.

used nodeport instead of loadbalancer to have external ip.

### 5. Deploy Pulumi Stack

Deployed the Pulumi stack on the Kubernetes cluster and verify that it's running correctly.

### 6. Serve HTML Web Page

Configured the Nginx server to serve a static HTML webpage.
Access the webpage using port forwarding locally or by minikube ip:nodeport ip

