# Data Platform Engineer Challenge

## Introduction

Axpo has ambitious goals to become a data-driven company.
To achieve this, we need to build a modern data platform that enables
data scientists, data engineers, and business users
to access, analyze, and consume data in a secure and efficient way.

To do so, we need your help to design and implement a data platform.

## Your Mission, Should You Choose to Accept It:

### Initial position

Axpo is building a centralized Azure Databricks-based platform with:

* Terraform as the source of truth for infrastructure and core governance

* GitHub Actions for CI/CD

* Multiple business domains / subsidiaries

Platform users include data scientists, engineers and analysts who need “safe playgrounds” and controlled promotion paths. 
You can assume Azure core services are available (Storage, Key Vault, IoT Hub, Log Analytics, etc.).

### Rules

* read the whole README.md carefully
* don't solve everything, focus on what you think is most important
* be creative and pragmatic
* be prepared to present your results and answer (live, related) questions

### Tasks overview & scoring

All tasks are required.

We evaluate tasks with the following weighting:
- **Task 1 (Design): 40%**
- **Task 2 (Terraform): 40%**
- **Task 3 (IoT ingestion): 20%**

Recommended time split (to match the weighting):
- Task 1: ~60 minutes prep — present in 10 minutes
- Task 2: ~60 minutes prep — present in 10 minutes
- Task 3: ~30 minutes prep — present in 5 minutes

### Task 1: 👩‍🎨 Design a Data Platform
Draft a high-level architecture for Axpo’s data platform on Azure Databricks.

**Must address (explicitly):**

**1. Environment strategy**
* how do you separate platform engineering changes from data product changes? 
* How do you handle dev/test/prod when customers of the platform (Data scientists/engineers/analysts) need dev/test too?

**2. Data sharing model across teams/domains**
* How do teams publish and consume “data products”?
* How do you prevent “copy-paste data silos”?

**3. Responsibility split**
* What does the platform team own vs what data product teams own?

**4. Security & governance at the right level**
* Identity model, least privilege, separation of duties, data access patterns
* How do we handle multi-region/multi-tenant requirements (high-level)?

**5. Operationalization**
* Monitoring/alerting, cost controls, and incident basics (even if high-level)
* Data contract approach (schema + quality expectations)

> Keep it crisp: say 5 slides, 10 minutes.

### Task 2: 👷 Implementation phase
Implement a small Terraform design that onboards a new business domain into the platform.
Assume the new domain is **"Human Resources"**.

**Context**: Axpo onboards many business domains over time. Each domain must have clear ownership boundaries.
We also want onboarding to be repeatable and maintainable as the number of domains grows.

**Deliverable**: A small Terraform codebase (module(s) + example usage) that provisions the minimum resources needed to onboard a new domain.

**Must demonstrate**
- a clear separation between **platform-managed** resources and **domain-managed** resources
- at least one of:
  - Unity Catalog catalog/schema + grants
  - external location + credential + grants
- how you would support **multiple environments** (dev/test/prod) in code (structure/variables/workspaces/stacks)

**Nice to have**
- naming conventions and tagging strategy
- a short README explaining:
  - what the platform team needs to provide
  - what the domain team needs to do
  - how a second domain would be added

> You don’t need everything runnable, but it should be clear, idiomatic, and scalable to many domains.

### Task 3: 🕵️‍♂️ It's all about the details

In Axpo many data are directly arriving from IoT Sensors. Could you design a solution to ingest data from IoT sensors into a data platform? Which tools would you use and why? What are the most important aspects to consider?

Hint: Considering the amount of data it would be great to have a solution that scales well!

> Highlight only technical details you think are relevant and present your solution in 5 min.

## THE END

We're looking forward to your results and are excited to discuss them with you.

Good luck and have fun! 🚀
