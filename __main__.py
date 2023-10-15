import pulumi
import pulumi_kubernetes as k8s

app_name = "nginxweb"

# Create a ConfigMap to define the mount path
nginx_config_map = k8s.core.v1.ConfigMap(
    "nginx-config",
    metadata={
        "name": app_name + "-config",
    },
    data={
        "mount-path": "/usr/share/nginx/html",
    },
)

# Create a Deployment without volume mounts
nginx_deployment = k8s.apps.v1.Deployment(
    app_name,
    spec={
        "selector": {
            "matchLabels": {"app": app_name},
        },
        "replicas": 4,
        "template": {
            "metadata": {"labels": {"app": app_name}},
            "spec": {
                "containers": [
                    {
                        "name": app_name,
                        "image": "nginx:alpine",
                        "resources": {
                            "requests": {
                                "cpu": "100m",
                                "memory": "128Mi",
                            },
                            "limits": {
                                "cpu": "250m",
                                "memory": "256Mi",
                            }
                        },
                    }
                ],
            },
        },
    },
)

# Create a Service
nginx_service = k8s.core.v1.Service(
    app_name,
    spec={
        "selector": {"app": app_name},
        "ports": [
            {"port": 80, "targetPort": 80, "name": "http"},
            {"port": 443, "targetPort": 80, "name": "https"},
        ],
        "type": "NodePort",
    },
)

pulumi.export("deployment_name", nginx_deployment.metadata["name"])
pulumi.export("http_port", nginx_service.spec["ports"][0]["port"])
pulumi.export("https_port", nginx_service.spec["ports"][1]["port"])

