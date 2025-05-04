# Esops-course
This is a course for Barista team.

What is SRE? What technologies do we use?:
https://docs.google.com/presentation/d/14lZw6EWNdbgEsl14Lg7Vtc6gwGIbPTeOR_QTC_Su2cY/edit?usp=sharing

---

# Your assignment

### Main Goal

Your main goal in the end is to deploy the whole monitoring stack.
Each folder has instructions on how to deploy the technology and use it.

In the end, each of you will have its own monitoring stack and will understand each
component of it. 

### Before Everything (DO NOT SKIP!)

In this repo, there is a monitoring-demo-app. This application demonstrates a basic python application that generates metrics, logs and traces.

It uses flask for API and contains endpoints to help demonstrate a real application's data and behaviour.
Go ahead and read its README, and if you're curious check its code :)

The app includes everything you need to deploy it to openshift (a helm chart including of deployment, service and route).
Before starting, Make sure you understand EVERYTHING in each of the components that are in the helm chart, as it essential for the exercises.

The app **does not** include instrumentation at all, **you** will need to instrument it using opentelemetry.

After deploying, click on the route's link to see the app's UI and check that everything works.

From this point, you are ready to start your main mission (YAY :D)
Go to otel-collector's README that in this repo and continue from there.

**Notice**: openshift's sandbox can sometimes delete your pods, as it is a free version and we are broke.

