# Data Engineer - Challenge

## Intro

Axpo's infrastructure generates lots of data. Our goal is to make use of this
data to improve our decision base.

To do so we need you to collect, store and prepare data for BI specialists
and Data Scientists.

## Your mission, should you choose to accept it:

### Initial position

* list of signals (as csv)

* Docker compose environment containing
    * IoT data generator as Docker
    * MQTT Broker
    * Azure Storage Account
    * Integration Runtime

### Rule set

* **Please invest no more than 5 to 8 hours.** If you cannot complete the task
  in this time frame, document where you got stuck, so we can use this as a
  basis for discussion for your next interview.
* You're free to choose the tech stack you feel fitting
* You're allowed to use cloud services
* You're allowed change the docker compose environment to suit the purpose

[//]: # (TODO: cloud budget up to $ 50.00?)

### Step 1:

The first goal is to save the IoT data as well as the corresponding signals in
raw format to a cheap long term storage.

### Step 2:

The second goal is to make the data available so BI specialists can query near
real time data for different signals.

Optional:

* resample IoT data to 15 min values
* data catalogue
* data quality indicator

### Evaluation criteria

What we're looking for:

* We want to see what you can, not wat you can't
* Clean project setup
* The ability to determine the actual problem area and find a suitable solution
* Pragmatic solution, scratch features when necessary, time is short!
* Document your approach, your decisions, and your general notes directly in
  your
  code or in a readme file

## Preparations for interview

* open your project in your IDE
* have your environment running on your machine or somewhere in a cloud
* be prepared to present your approach for 5-10 min (no slides!)
* be prepared to answer a few questions after your presentation

# TODOs:

* implement IoT data generator
* prepare docker compose
* improve instructions above
* let challenge be challenged by internals
