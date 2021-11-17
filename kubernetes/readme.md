# Setting up a local Kubernetes cluster with Minikube

Why Minikube? You can run a local kubernetes intance from docker-desktop or Kind too but minikube seems to be "clostest" to a production scenario.

## installation steps

>Windows
 - install [chocolatey](https://chocolatey.org/install)
 - '''choco install kubernetes-helm'''
 

### 1. Install Docker
[see steps here for debian systems](https://techviewleo.com/how-to-install-and-use-docker-in-linux-mint/). Once complete you should see your docker version with:

```
docker -v
```

### 2. install minikube and kubectl

```
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube_latest_amd64.deb
sudo dpkg -i minikube_latest_amd64.deb
```

Now lets [install kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/). "KubeControl" is a command line tool lets you control Kubernetes clusters. #

```
sudo apt-get update && sudo apt-get install -y apt-transport-https gnupg2 curl
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
echo "deb https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee -a /etc/apt/sources.list.d/kubernetes.list
sudo apt-get update
sudo apt-get install -y kubectl
```

### 3. Start and Configure Cluster

Now we can start and interact with our cluster:

```
minikube start

# use kubectl to view
kubectl get po -A

# or using built in minikube dash
minikube dashboard

# stop 
minikube stop
```

### 4. Deploy an application

All deployed Applications are formed of one or more deployed workloads comprised of volumes, services, networks, and containers. Workloads and there interactions are described in yaml. Here is a simple hellow world example:

- see [/yaml/hello.yaml](/yaml/hello.yaml) based on [hello-world.yaml](https://github.com/paulbouwer/hello-kubernetes)

There are two key parts here:
- the container application
- a service that exposes the service on node port 8080 mapped to cluster port 30006

```
# deploy the workload
kubectl apply -f yaml/hello.yaml 

# details of the service
kubectl get service hello-kubernetes

# get cluster ip address
minikube ip

# visit
http://[minikube ip]:30006
```

Note in the Service, there is also some commented out code which changes the service from type=NodePort to type=LoadBalancer. NodePort is the simplest method and is fine for testing. Whereas load balancer is more robust. See the documentation [accessing containers](https://minikube.sigs.k8s.io/docs/handbook/accessing/).
