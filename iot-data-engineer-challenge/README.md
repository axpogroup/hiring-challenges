# IoT Data Engineer - Challenge

## Intro

Axpo's is building up BESS (Battery Energy Storage Systems) all over Europe. Each system can have a different setup, depending on country specific regulations, available suppliers or cost restrictions. 
Our goal is to develop a secure, reliable and scalable architecture to ingest the raw IoT data into our cloud platform and to transform it into usable information for the business.
## Your mission, should you choose to accept it:

### Initial position

* One BESS is already commissioned and needs to be integrated into the Axpo Data Platform
* In the upcoming month 5-10 BESS will be commissioned and should although be integrated. In the next years the amount could go into the hundreds. 

### Rule set

* **Please invest no more than 2 to 3 hours.** If you cannot complete the task
  in this time frame, document where you got stuck, so we can use this as a
  basis for discussion for your next interview.
* You're free to choose the tech stack you feel fitting. We recommend you to use the tech you already worked with!
* We don't expect to see code or a detailed solution, but rather a high level architecture and concept.

### Tasks overview & scoring

All tasks are required.

We evaluate tasks with the following weighting:
- **Task 1 (IoT Data Ingestion): 30%**
- **Task 2 (IoT Data Product): 70%**

Recommended time split (to match the weighting):
- Task 1: ~45 minutes prep — present in 5 minutes
- Task 2: ~90 minutes prep — present in 10 minutes



### Task 1: 👷  Design a ingestion concept for BESS
Draft a high level concept on how to connect non standardized BESS across Europe to get the IoT data ingested in a delta lake (e.g. storage account, S3 Bucket, ...) in near real time (delay of < 30 seconds). The concept can be a a slide showing the components and how they interact. Feel free to name actual services or technologies you would use.

#### Requirements:
* The IoT data only needs to be stored in a raw format in the delta lake, no further processing is needed for this task.
* The BESS are considered as critical infrastructure and need a strict separation between the OT and IT. 
* Only outgoing network connections are allowed from the BESS site network to the public internet.
* Only Read Access needs to be allowed, there should no be no way to control the BESS from outside.
* The BESS SCADA provides different interfaces to give access to the data like: Modbus, OPC UA,  REST APIs or CSV / JSON exports.

#### Considerations:
* Scalability: How much effort it takes to onboard new BESS.
* Adaptability: How to handle different setups while keeping the same overall approach.
* Maintainability: How to monitor and maintain the increasing amount of connected BESS.

#### What the concept should cover
* Connectivity: How to connect the BESS SCADA System to get the raw data?
* Security: How to get the data in the cloud from the BESS site?
* Maintainability: How to manage the "edge environment", e.g. request new signals from the BESS SCADA System?

### Task 2: 👩‍🎨 Design a IoT Data Product
Draft a high level concept for transforming the raw IoT data into a usable IoT data product in the Axpo Data Platform (Databricks) that can be used for analytics use cases and dashboards. 

#### Requirements:
* The BESS SCADAs send the data on change, e.g. a temperature sensor only produces a datapoint if the temperature changed and not in a given interval
* Each BESS SCADA has up to 20.000 different data points (voltage, temperatures, states, ...) where some send in high frequency (< 1 seconds) and some very rarely (e.g. every few months).
* For each BESS there is a meta data for the data points, like description, label, measurement unit given
* The data in the IoT Data Product should have near real time data (delay of < 30 seconds from measurement is send from SCADA to data is available for the users)
* Potential use cases for the IoT data product are:
* * Calculate availability and usage statistics of a BESS and visualize them in dashboards and reports
* * Run anomaly detections based on specified measurements from the BESS to detect unhealthy states
* * Provide flexible access to the a subset of the data (e.g. only the data of a specific BESS) to different user groups


#### Considerations:
* Each BESS can have different component and measurements, the iot data product needs to be flexible enough to represent this with out ongoing adaptions to it.
* How to handle late arriving data (e.g. after connection issues, data from 4 hours ago are transformed)?
* How to ensure a high data quality (e.g. identify faulty signals?)
* 


#### What the concept should cover
* Which data sets should be in the IoT Data Product? 
* Access Management: How to give give flexible access to a subset of the IoT Data Product to different people?
* Data Quality: What are some important data quality metrics and how could a high data quality level be ensured? 

### Evaluation criteria

What we're looking for:
* The ability to create and explain a coherent solution. We want to see how you approach such a task.
* Show a pragmatic solution, we don't expect a detailed solution that covers every edge case.

## Preparations for the interview
* be prepared to present your approach for 10-15 min
* be prepared to answer a few questions after your presentation
