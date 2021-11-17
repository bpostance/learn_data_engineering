# Budibase


## Installation
[docs](https://docs.budibase.com/self-hosting/hosting-methods/kubernetes)

'''
helm repo add budibase https://budibase.github.io/budibase/
helm repo update
helm install --create-namespace --namespace budibase budibase budibase/budibase
'''