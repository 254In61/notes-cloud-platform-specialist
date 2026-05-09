# Phases of DevOps Lifecycle

Phase 1 : Plan (Dev)
====================
Before a single line of code is written, the team must define the value they are creating.

- Goal : Define requirements, create roadmaps, and organize tasks.
- Key Activities: Backlog management, sprint planning, user story creation.
- Tools: Jira, Trello, Azure Boards.

Phase 2 : Code (Dev)
=====================
Developers write the code and commit it to a shared repository.

- Goal: Write high-quality, version-controlled code.
- Key Activities: Coding, code reviews, merging branches.
- Tools: Git, GitHub, GitLab, Bitbucket.

Phase 3 : Build (Dev)
======================
Once code is committed, it is pulled and compiled into an executable format.

- Goal: Detect compilation errors early and package the application.
- Key Activities: Compiling code, dependency management, creating container images (Docker).
- Tools: Packer, Maven, Gradle, Docker.

Phase 4 : Test (Dev)
=====================

The build is tested for bugs, security vulnerabilities, and performance issues.

- Goal: Ensure software quality and prevent bugs from reaching production.
- Key Activities: Unit testing, integration testing, static code analysis.
- Tools: Selenium, JUnit, SonarQube, TestNG.

Phase 5 : Release (Ops)
=======================

The code has passed testing and is ready to be deployed. This phase manages the versioning and approval.

- Goal: Schedule and manage the release to specific environments (Staging/Prod).
- Key Activities: Artifact versioning, change management approvals.
- Tools: Jenkins, GitLab CI, CircleCI.

Phase 6 : Deploy (Ops)
======================

The application is deployed to production or target environments.

- Goal: Deliver the software to end-users with zero downtime.
- Key Activities: Infrastructure provisioning (IaC), configuration management, blue/green deployments.
- Tools: Terraform, Ansible, Kubernetes (ArgoCD), AWS CodeDeploy.

# Phase 7: Operate (Ops)
=========================

The software is live. This phase involves the day-to-day management of the infrastructure running the app.

- Goal: Ensure system uptime and reliability.
- Key Activities: Server patching, auto-scaling, database management.
- Tools: Chef, Puppet, PowerShell, Ansible

# Phase 8: Monitor (Ops)
=========================
Data is collected from the live application to understand user behavior and system performance. This feedback loops back into the Plan phase.

- Goal: Detect issues immediately and gather insights for future improvements.
- Key Activities: Log analysis, performance tracking, alerting.
- Tools: Prometheus, Grafana, Nagios, ELK Stack (Elasticsearch, Logstash, Kibana).
