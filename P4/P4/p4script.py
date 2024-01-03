import sys, subprocess
from signal import pause
import time

version = input("Introduce versión de reviews (1, 2 o 3): \n")

if version != "1" and version != "2" and version != "3":
    sys.exit(1)

subprocess.run(["kubectl", "apply", "-f", "productpage/productpage.yaml"])
subprocess.run(["kubectl", "apply", "-f", "details/details.yaml"])
subprocess.run(["kubectl", "apply", "-f", "ratings/ratings.yaml"])
subprocess.run(["kubectl", "apply", "-f", "reviews/reviews-svc.yaml"])
if version == "1":
    subprocess.run(["kubectl", "apply", "-f", "reviews/reviews-v1-deployment.yaml"])
if version == "2":
    subprocess.run(["kubectl", "apply", "-f", "reviews/reviews-v2-deployment.yaml"])
if version == "3":
    subprocess.run(["kubectl", "apply", "-f", "reviews/reviews-v3-deployment.yaml"])

subprocess.run(["kubectl", "get", "pods"])
subprocess.run(["kubectl", "get", "service/productpage-external"])
#time.sleep(5)
#subprocess.run(["kubectl", "scale", "deployments.apps/details-v1", "--replicas=3"])
#subprocess.run(["kubectl", "scale", "deployments.apps/ratings-v1", "--replicas=2"])
#subprocess.run(["kubectl", "get", "service/productpage-external"])