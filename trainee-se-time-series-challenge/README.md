# Trainee Software Engineering: Time Series Challenge

## Intro

Axpo's Grid Division is integrating IoT data to their internal data platform. Our goal
is to analyze different time
series which represent various signals of different assets
(e.g. power of a transformer, voltage level of a power line etc.)

To do that, we decided to engage you to develop a tool that will help us visualize and
analyze our time series.

### Initial position

* Data dumps contained in this repository:
  assets <- signals <- measurement
    * each signal belongs to an asset
    * each measurement belongs to a signal

## Your mission, should you choose to accept it:

Chose one of the given challenges below. Please invest no more than 5 hours!

### Challenge 1: Frontend

Create a web app that can visualize the data:

* Selection for Assets and Signals
* Time series visualization of a selected signal

### Challenge 2: Backend

* create a Rest-API with three endpoints:
    * get all assets
    * get all signals for a given asset
    * get all measurements for a given signal (and start and end date/time)

### Challenge 3: Database

* create a relational database schema given the provided data structure
* create a script to import the provided data dumps into the database

## Evaluation criteria

What we're looking for:

* The ability to determine the actual problem
* The ability to find a suitable solution
* Running code
* Small documentation (add a couple of lines to the SOLUTION.md file)
* Scratch features when necessary, time is short!
* It's not about quantity, but quality! Solving one challenge is enough.

## Preparations for interview

* open your IDE to run your code
* have a running version of your app ready
* prepare to present your approach for 5-10 min (no slides!)
* be prepared to answer a few questions after your presentation
