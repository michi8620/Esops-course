# Instructions for Prometheus + VictoriaMetrics Setup

## Prometheus: Beginner Starter Questions

Welcome to the beginner's guide for Prometheus!  
Before you start installing or working with Prometheus, it's important to understand the basics. Answer these fundamental questions to get a solid grasp of the core concepts.

1. What is the purpose of Prometheus in an observability stack?
2. How does Prometheus collect metrics from applications?
3. What is the Prometheus data model (e.g., time series, labels, metrics)?
4. What are exporters in Prometheus? Give an example.
5. What’s the role of a scrape configuration in Prometheus?
6. How does Prometheus store data? What are some limitations of this approach?
7. What is VictoriaMetrics, and how is it related to Prometheus?

---

## Step 1: Deploying Prometheus

- add this helm chart to your local helm repo: https://github.com/open-telemetry/opentelemetry-helm-charts/tree/main/charts/opentelemetry-collector
- pull the chart to your desired folder and untar it.
- create an additional values file and call it "values-openshift-sandbox.yaml". DO NOT CHANGE DEFAULT VALUES FILE.
- Copy and paste the configuration from values.yaml here to values-openshift-sandbox.yaml.
This is your starting point, we:
1. Provided the image you will use which is opentelemetry-collector-contrib, read about how 
it is different from the ordinary opentelemetry collector image.
2. Configured the resources for the collector, read on the difference between "limits" and "requests".
3. Gave you the basic configuration for pipelines in the collector. If you don't understand something in it,
ask google. 

Some **important** points for the learning process:
- When installing the helm chart, override the default values using --values:
```
helm install <release_name> ./path/to/chart --values <values_override>.yaml -n <namespace>
```
This flag will make sure that the default configuration will not change unless you override it
with new values. 

The reason we create a seperate values file is to easily see how our teammates changed
the default configuration, and to make different values files for different environments (openshift, AWS, Azure...)
as they require different configurations.


- **DO NOT HARDCODE!** helm charts are built to be as generic and modular as possible. 
The only thing you will change is your custom values.yaml. helm will do the work and inject it in the deployment
files, you can check how by entering the files in 'templates'.
- **Don't create a route this time.** The app-demo should be in the same namespace as the collector so
the app will send data to the Service instead using NodePort as the type.
In real life you **will** need to create a route for the collector, so apps from other namespaces could 
send data to you, but for learning purposes and because of issues with using gRPC protocol with routes we will skip it.

---

## Step 2: Instrumenting the App

- Instrument using ZERO-CODE based instrumentation. chatgpt will tell you to change the code inside main.py, as Joe
Biden said: DON'T. find the right documentation and don't give in to AI. You DON'T need to change the python code.
- Install the necessary libraries inside the **Dockerfile**, don't write them in requirements.txt
- Define environment variables inside a **ConfigMap** and mount them into deployment.yaml
(https://kubernetes.io/docs/concepts/configuration/configmap/), don't add them in the Dockerfile.
**ConfigMap should be generic and take its variables from the values file.**
- Send data using gRPC protocol.
- Make sure to disable tls.

---

## Step 3: Succeeded or Failed?

### Success: 

Check inside the collector's pod's logs. The debug configuration in the collector we gave you in the start should print
all the data that is sent to the collector. If you see the data flowing that means that you succeeded! :D

### Failure:

- There is only startup logs in the collector's pod.
- There are errors or warnings in the demo-app logs.

---
## Bonus: Route

- Create a Route  for the collector so other apps could send data to it.
https://docs.redhat.com/en/documentation/openshift_container_platform/4.11/html/networking/configuring-routes#nw-creating-a-route_route-configuration

---

### Congratulations on finishing this task! 
#### This is a great start for your SRE and DevOps journey, now go to the prometheus folder's README to continue.

---


Copyright © 2025 Barista.


