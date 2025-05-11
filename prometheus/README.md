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

# What are we doing?

After we managed to send telemetry data from our app to the collector, we now need to seperate this data to
the three data sources: prometheus/victoriaMetrics, loki and tempo.

In this assignment, you will first deploy prometheus, configure opentelemetry to expose its metrics and configure 
prometheus to scrape those metrics.

Then, you will change the data source to victoria metrics and make similar steps.

So let's start by deploying prometheus, good luck!


## Step 1: Deploying Prometheus

Compared to the last exercise, now we **have** to make a Route file, so we could access the UI of prometheus.

Let's do it!

1. Add this helm chart to your local helm repo: https://artifacthub.io/packages/helm/prometheus-community/prometheus
2. Pull the chart to your desired folder and untar it.
3. Create an additional values file and call it "values-openshift-sandbox.yaml". DO NOT CHANGE DEFAULT VALUES FILE. 
4. Copy and paste the configuration from values.yaml here to values-openshift-sandbox.yaml.
5. Try deploying it to openshift and based on the errors you encounter modify values-openshift-sandbox.yaml

Only after you succeeded deploying prometheus, continue to the next instructions.

6. Add a route.yaml file in templates with the right configuration. make sure it is pointing on the right Service.
7. Add its values in the values-openshift-sandbox.yaml file.
8. Try deploying it to openshift using the command you already know (look in the previous assignment).

### Oh no, that didn't work. Why?

In helm charts we have something called **'values.schema.json'**. go inside values.schema.json in your prometheus chart.
You'll see that the creators of this helm chart specified specifically what objects should be in the chart.
And guess what, route is not one of them :( So we can't actually just add whatever we want. 

We have two options:
1. modify values.schema.json to suit our needs and enable creating a route object.
2. create a **wrapper** chart that will act as the parent of the prometheus chart. It will be a chart inside a chart.
The child chart is called a subchart. 

#### We will use the second option, so you would learn a little bit about dependencies ;)
(And also, it is not recommended to change a chart's scheme,
as we want our work to be understandable for our coworkers and not change already built charts )


### Creating a wrapper chart

1. Create a folder named 'prometheus-wrapper' 
2. inside this folder, create:
- 'charts' folder
- 'templates' folder
- Chart.yaml file
- values.yaml file
3. In your charts folder, copy paste the prometheus chart you pulled earlier. 
4. Copy and delete values-openshift-sandbox.yaml, paste its content to the values.yaml you created under a 'prometheus' block. like this:

```
prometheus:
    server:
      resources:
        limits:
          cpu: 500m
          memory: 1Gi
        requests:
          cpu: 250m
          memory: 512Mi
## and so on...

## hint: define here the route configuration.
```

5. Copy and delete the route.yaml you created earlier, create route.yaml in the 'templates' folder and paste its content.
6. In your route.yaml you probably have something like '{{ include "prometheus.server.fullname" . }}' (If you did it the right way without hardcoding).
when executing this line, helm uses a file called **_helpers.tpl**. 

---

#### _helpers.tpl:

In Helm charts, _helpers.tpl is a template file typically used to define reusable template snippets—like labels, names, and annotations—that can be shared across other chart templates.

It usually contains Go template functions using define and template, helping keep the code DRY (Don't Repeat Yourself). For example:

```
{{- define "mychart.fullname" -}}
{{ printf "%s-%s" .Release.Name .Chart.Name }}
{{- end }}
```

You can then reuse it in other templates like this:

```
metadata:
  name: {{ include "mychart.fullname" . }}
```

---

Now that you understand why helm charts have _helpers.tpl, and you even went inside the one that in the
prometheus chart because you are a very curious person, **let's go back to the instructions**:

7. Because we are using a chart inside a chart, and we are only adding one file (route.yaml),
we don't necessarily need to create _helpers.tpl. Instead, write it inside values.yaml (for example,
the name of the service that the route points to which is usually pulled from _helpers.tpl)
8. Add the following to the Chart.yaml file:

```
apiVersion: v2
name: prometheus-wrapper
description: A wrapper chart around prometheus
type: application
version: 0.1.0
appVersion: "1.0"

dependencies:
  - name: prometheus
    version: "27.12.0"
    repository: "https://prometheus-community.github.io/helm-charts"
```
The documentation source: https://helm.sh/docs/helm/helm_dependency/
We also use this strategy when creating an **umbrella chart** (many charts under one chart).
Even prometheus uses it, and that's why we disabled all the subcharts in the values we gave you in the start.

#### So what should you have?

1. charts folder that contains the prometheus chart
2. templates folder that contains only route.yaml
3. Chart.yaml file that defines chart configuration and contains its dependencies.
4. values.yaml that contains values for the prometheus chart inside a 'prometheus' block,
and values for your wrapper chart (route values).

#### Try deploying!

##### Success:
everything runs smoothly, you can access prometheus UI by clicking on the route. AMAZING!

## Step 3: Configure prometheus exporter inside the collector

1. using your existing otel-collector helm chart, try to add the needed configuration for the collector
to expose a /metrics endpoint using prometheus exporter.
It should be two lines!!

Wait, why /metrics? what do you mean?
ask chatgpt, I didn't find a good source :\

2. To actually expose a /metrics endpoint, you will need to expose a port of your choice in your Service.yaml.
Add this port inside the values-openshift-sandbox.yaml Service ports configuration and name it 'metrics'.
   (A hint to understand it better: you have two main ports that are exposed: otlp and otlp-http. just add one more)

3. After making the changes, upgrade your otel-collector and check that the port is exposed.

If everything works (and even if not), you are doing amazing! keep learning!

---

## Step 3: Configure Prometheus to Scrape the Collector

After you've got a successfully deployed prometheus, let's ruin it😈

In this step, all you need to do is add a target to scrape.
Since this step is short, I will not direct you this time. 
Try asking google, chatgpt, claude, and I'm sure you will make it :)

### Success: 

Access prometheus UI, in the menu there is 'status' and then 'target health'. check that prometheus successfully
scrapes your collector.

if it is, go back to the homepage and check if you can query the metrics.

---

# Victoria Metrics

coming soon

### Well done!
#### go to the loki folder's README to continue.

---


Copyright © 2025 Barista.


