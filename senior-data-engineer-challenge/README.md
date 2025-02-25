# Senior Data Engineer Challenge: Mentoring Mike

## Intro

Welcome to the Senior Data Engineering Challenge! In this challenge,
you will work with Mike, our new trainee data engineer,
who needs your help to analyze real-world electricity flow data for Switzerland.
Your task is to support Mike on his journey to become a professional data engineer
while ensuring the quality and efficiency of his work.
This exercise will test your ability to mentor and guide junior team members,
as well as your data engineering, analysis, and communication skills.

## Initial position

Imaging Mike, a trainee data engineer, who just finished his master's degree in Robotics and now is eager  to learn more
about data engineering. Mike has been assigned to your team for the next 6 months to learn from you and your team.
As a senior data engineer, you are responsible for mentoring Mike and ensuring that he learns the necessary skills.
In your last sprint planning you identified the following task for Mike to work on in his first week: 
https://github.com/axpogroup/hiring-challenges/tree/main/trainee-data-engineer-challenge

It is your task to onboard Mike, guide him through the challenge, and ensure that the task is completed successfully.


## Your mission, should you choose to accept it:

Below are the tasks you need to complete as part of this challenge:

### 1. Mike's first day at work

Your technical lead has assigned you the task to mentor Mike. Therefore, he asked you to prepare the onboarding
for Mike. On the day before Mike starts, your technical lead asks you quickly about the onboarding plan for Mike and
what you have in Mind. You had some time to think about it, but you haven't written anything down. Consider also Mike's
background in robotics, and that he is new to software / data engineering.

In the first 5 minutes of the interview explain quickly what you have in mind for Mike's onboarding. Be creative, but
do not over-engineer it. The technical lead (audience) will ask you questions about your plan. Notes are allowed,
no slides are needed.

### 2. Mike's pipeline goes real time

Mike show some great progress in his first week. He has successfully implemented the data pipeline using the data set
provided. He even figured out how to use an API call to get the latest batch of data at the end of the day.

Now in a one-on-one with Mike, he tells you that he was reading about an MQTT broker provided by the data source owner.
He understands that he somehow can use this to get real-time data. But he is not sure how to implement this in his
pyspark pipeline. In your absence the team created a new Jira ticket to implement this feature and assigned it to you
because they know you as a senior data engineer have experience with real-time data processing,
and of course you know 😉!

On one hand you have to deliver this feature by the end of the week, on the other hand you have to make sure that Mike
and the rest of the team learns something. How do you handle this situation?

After tomorrow's daily standup, you have scheduled a meeting with the team to clarify the delegation situation and 
to enable them, especially Mike, to resolve the issue without you having to take over completely. You prepared
a short presentation to explain your role in the team and the basic concepts of real-time data processing.

Take 10 minutes during the interview as if this would be the meeting with the team and present your plan. Expect
some questions and counterarguments from the team (audience).

### 3. Mike's little issue

It's day before the pipeline should go to production and Mike approaches you with a problem. He accidentally dropped
the whole repository without any backup. Everyone is in panic, and you're their last hope. Roll up your sleeves and
save the team from this embarrassing situation.

Given the [challenge](https://github.com/axpogroup/hiring-challenges/tree/main/trainee-data-engineer-challenge) Mike was
assigned to, it's now on you to implement the pipeline. Use the docker setup in this folder to simulate the MQTT signal:

host: mqtt://localhost:1883
topic: energy_flow_in_and_out_switzerland_electricity_per_second

This topic randomly generates values like in the csv-File but in a 1 second interval. Use this to simulate the
real-time setup of your pipeline and mock other components and data to fulfill the challenge given to Mike.

It's due day, and you have to present the solution to the BI team who will take over the ownership of the
pipeline after initial implementation. The BI team is new to the setup, so consider also to explain a bit the
architecture of your data platform, your ci/cd setup, and how they can monitor the pipeline.

Take 10 minutes to handover of the pipeline to the BI team (audience). Present your code as well as the outcome of the
analysis to a technical audience.

### 4. Mike is scaling

After one year, Mike is progressing well and has implemented many real-time data pipelines gathering a lot of IoT data
from all the sensors from various power plant of Axpo. His solution is getting slow and very costly. Mike is asking you
to help him to scale his solution.

Take 3 Minutes to explain a couple of considerations you would take into account to scale the solution and how you would
approach this problem.

## Submission Instructions

Please submit your files as a zip archive at least 24h prior to the interview. 

## Evaluation Criteria

You will be evaluated based on the following criteria:

* Show seniority in mentoring and guiding junior team members.
* Show strong communication skills, empathy, and ability to de-escalate difficult situations.
* Show creativity and pragmatism in solving real-world problems.
* Get your hands dirty and show your technical skills in data engineering.

Time is precious. Don't wast it.

Good luck with the challenge!