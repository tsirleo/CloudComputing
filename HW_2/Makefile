all: minikube/install kubectl/install minikube/start app/deploy/all get_link

minikube/install:
	curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
	sudo install minikube-linux-amd64 /usr/local/bin/minikube && rm minikube-linux-amd64

minikube/uninstall:
	sudo rm -rf /usr/local/bin/minikube
	rm -rf ~/.minikube

minikube/start:
	minikube start

minikube/stop:
	minikube stop

minikube/delete:
	minikube delete

minikube/dashboard:
	minikube addons enable metrics-server
	minikube dashboard

kubectl/install:
	curl -LO https://dl.k8s.io/release/`curl -LS https://dl.k8s.io/release/stable.txt`/bin/linux/amd64/kubectl
	chmod +x ./kubectl
	sudo mv ./kubectl /usr/local/bin/kubectl

kubectl/uninstall:
	sudo rm -rf /usr/local/bin/kubectl

cluster_info:
	@echo "$$(kubectl get nodes -o wide)"

get_link:
	@echo "$$(minikube service server-app --url)/docs"

svc_info:
	@echo "$$(kubectl get svc)"

pods_info:
	@echo "$$(kubectl get pods -A)"

app/deploy/all: ./kube-manifests/database-volume-pvc.yaml ./kube-manifests/env-local-configmap.yaml ./kube-manifests/mysql-db-service.yaml ./kube-manifests/mysql-db-deployment.yaml ./kube-manifests/server-app-service.yaml ./kube-manifests/server-app-deployment.yaml
	kubectl apply -f ./kube-manifests/database-volume-pvc.yaml
	kubectl apply -f ./kube-manifests/env-local-configmap.yaml
	kubectl apply -f ./kube-manifests/mysql-db-service.yaml
	kubectl apply -f ./kube-manifests/mysql-db-deployment.yaml
	kubectl apply -f ./kube-manifests/server-app-service.yaml
	kubectl apply -f ./kube-manifests/server-app-deployment.yaml

app/deploy/deployment: ./kube-manifests/mysql-db-deployment.yaml ./kube-manifests/server-app-deployment.yaml
	kubectl apply -f ./kube-manifests/mysql-db-deployment.yaml
	kubectl apply -f ./kube-manifests/server-app-deployment.yaml

app/remove/all:
	kubectl delete -n default deployment mysql-db
	kubectl delete -n default deployment server-app
	kubectl delete -n default service server-app
	kubectl delete -n default service mysql-db
	kubectl delete -n default persistentvolumeclaim database-volume
	kubectl delete -n default configmap env-local

app/remove/deployment:
	kubectl delete -n default deployment mysql-db
	kubectl delete -n default deployment server-app
