# Energy Community Unified User System Challenge

## Intro

Energy City's Platform Services department is in the midst of a citywide user data migration. Our goal is to migrate all users of the city's largest energy communities, Hydropolis, Sunstar and Breeze, into a single user identity system (ECUUS - Energy Community Unified User System).

Exciting!

In preparation for the big transition, we decided to engage you to develop a tool that will help us __understand what the current user overlap__ of energy communities looks like.

**Please invest no more than 5 to 8 hours.** If you cannot complete the task in this time frame, document where you got stuck so we can use this as a basis for discussion for your next interview.

## Your mission, should you choose to accept it:

### Step 1

Using the data dumps contained in this repository and the tools of your choice, create an HTML report that shows the following:

- The total overlap between all three energy communities in percent, the number of users, and a graph of your choice.
- The overlap between all combinations of energy communities (Hydropolis <-> Sunstar, Hydropolis <-> Breeze, Sunstar <-> Breeze). Percentage, number of users and a chart of your choice for each.
- A table with the 10 most common zip codes, sorted by frequency in descending order


### Step 2

* Create a Dockerfile that allows other developers to run the application. The idea behind this is that all we need to verify the application is a Dockerfile and your assets. It is up to you whether you host the project directly from the running Docker container or create a folder with the assets that can be used without a web server.
This is no different from how we deploy our code in our production environment.

## Evaluation criteria

What we're looking for:

- Clean project setup and documentation
- The ability to determine the actual problem area and find a suitable solution
- Relevant tests for your code
- Scratch features when necessary, time is short!
- Document your approach, your decisions, and your general notes
