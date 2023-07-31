# SRE Instrumentation Challenge - Roberto Gutiérrez solution and step-by-step process


### Step 0: Understand what's happening

- Have a quick look at the code itself - particularly at Readmes, Makefile, bucket.py and _more or less_ understand the objective
- Prepare some tools: python3, pip3, docker... And install dependencies 
- Run the code with make run and do a couple of requests of each method
- Once everything makes a bit of sense, start with step 1

### Step 1: Implementation

- For adding the Prometheus-related stuff I looked for a couple of useful links, like the [official docs](https://github.com/prometheus/client_python), a couple of medium articles such as [this](https://medium.com/@letathenasleep/exposing-python-metrics-with-prometheus-c5c837c21e4d) or a more detailed [one](https://medium.com/swlh/generate-and-track-metrics-for-flask-api-applications-using-prometheus-and-grafana-55ddd39866f0)
- Decided to add _some_ logging and more responses to the endpoints (In order to be able to play around and test a bit better)
- I kept the Dockerfile simple, using a slim python version.
- Tried the docker file with `docker build -t storage_api . ` + `docker run -d -p 5000:5000 storage_api:latest` + some curls 

### Step 2: Visualization
- For the docker-compose up I had some issues on disk space which were interesting to debug. (Naturally I have _more_ than enough disk space, but it seems I had many unused docker volumes, which took me a while to debug)
- I had an issue with the /metrics endpoint, it was in /api/metrics, so I had to update prometheus/prometheys.yml (Took a bit to find that one)
- I explored prometheus stats and played around with the Grafana dashboards, but I decided to move quickly to the last step as I've got 1-2h left and I feel Grafana dashboards can absorb a lot of time and my knowledge is a bit rusted. 

### Step 3: Deployment
- I'd normally go for helm or kustomize for a deployment, but I decided to keep it as simple and straightforward as possible
- Not using any namespace for simplicity reasons
- 

