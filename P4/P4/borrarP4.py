import subprocess

subprocess.run(["kubectl", "delete", "-f", "details/details.yaml"])
subprocess.run(["kubectl", "delete", "-f", "ratings/ratings.yaml"])
subprocess.run(["kubectl", "delete", "-f", "reviews/reviews-svc.yaml"])
subprocess.run(["kubectl", "delete", "-f", "reviews/reviews-v1-deployment.yaml"])
subprocess.run(["kubectl", "delete", "-f", "reviews/reviews-v2-deployment.yaml"])
subprocess.run(["kubectl", "delete", "-f", "reviews/reviews-v3-deployment.yaml"])
subprocess.run(["kubectl", "delete", "-f", "productpage/productpage.yaml"])