# Overview
The 7 Cs of DevOps are core principles that help make DevOps successful. 

They guide how teams work together, build, test, and deliver software faster and more reliably. 

Each of these Cs contributes to a workflow that enhances the quality, speed, and reliability of delivering software products.


# 1. Continous Development
Continuous Development involves the iterative and incremental approach to software creation, where development teams plan, code, and prepare software features in small, manageable units. 

This methodology enables rapid feedback, early detection of issues, and swift delivery of value to end-users. 

It integrates closely with version control systems and automation tools to streamline the development process.

Example:
==========

Imagine a team building a food delivery app. Instead of waiting to finish the whole app and testing it later, the team adds features one by one:

On Monday, they add a "Login" feature and test it immediately.

On Tuesday, they add the "Search for restaurants" feature and test that too.

Each feature is checked and added to the live app as soon as it's ready. This way, if there's a problem in the "Login" part, they can fix it right away without affecting other parts.


# 2. Continuous Integration

Continuous Integration (CI) in DevOps ensures that code changes made by developers are automatically built, tested, and integrated into the main codebase. This process typically involves four key stages:

1. Source Code Management (SCM): Developers push their code from local machines to a remote repository such as GitHub. This allows teams to collaborate, review, and manage code versions easily.

2. Build Process: The source code is then compiled using tools like Maven, which packages the application into artifacts such as .jar, .war, or .ear files.

3. Code Quality Check: Tools like SonarQube analyze the code for bugs, code smells, and security issues. It generates detailed reports (HTML or PDF) to maintain code quality standards.

4. Artifact Repository: The generated build artifacts are stored in a repository manager like Nexus, which serves as a central storage for future deployment.

All these steps are automated using a CI tool like Jenkins, that orchestrates the complete flow, from fetching code to storing the final build artifact.

Example:
========
Let's say your team adds a new feature : "Track Delivery Person on Map"

> Developer writes code for the tracking feature and pushes it to GitHub.
> As soon as the code is pushed, Jenkins picks it up and uses Maven to build the app and test it using JUnit.
> The code goes through SonarQube, which finds a few duplicate lines and suggests better practises.
> Once everything is OK, the final app version(with the new feature) is saved in Nexus as a .jar file.

This way, every small change is tested, verified, and saved automatically without manual effort.

# 3. Continuous Testing
Continuous Testing means testing the code automatically every time there is a change. 

This helps catch bugs early before the app goes live. 

With DevOps and Agile methods, companies can use tools like Selenium, Testsigma, or LambdaTest to test their applications automatically. These tools run tests faster and smarter than manual testing.

Using a tool like Jenkins, we can set up the entire testing process to run automatically after every code change. This saves time and reduces human errors.

Example:
========
Let’s say your team adds a new feature: "Apply Coupon at Checkout."

After the developer pushes this new feature to GitHub, Jenkins automatically starts the testing process. Tools like Selenium or Testsigma test:

- Does the coupon code apply correctly?
- Does the final price update as expected?
- Does the checkout process still work?

If a problem is found, for example, the app crashes when a wrong coupon is entered the test will fail, and the developer will be notified immediately to fix it. This way, the team avoids pushing broken features to production and ensures the app remains reliable.

# 4. Continuous Deployment/ Continous Delivery

Continuous Deployment : is the process of "automatically" deploying an application into the production environment when it has completed testing and the build stages. 

Here, we'll automate everything from obtaining the application's source code to deploying it.

Continuous Delivery : is the process of deploying an application into production servers manually when it has completed testing and the build stages. Here, we will automate the continuous integration processes, however, manual involvement is still required for deploying it to the production environment.

Example:
=========

Suppose the team adds a “Refer & Earn” feature.

- The code is developed, tested, and marked as ready to go live.
- However, the product team decides to launch it during a weekend campaign.
- Until then, the feature stays on standby in the staging area.

Once approved, the code is manually deployed to production using a single click.

So, Continuous Delivery ensures every update is deployable anytime, but the actual release can be controlled.

# 5. Continuous Monitoring

DevOps lifecycle is incomplete if there was no Continuous Monitoring. 

Continuous Monitoring can be achieved with the help of Prometheus and Grafana we can continuously monitor and can get notified before anything goes wrong.

With Prometheus we can gather many performance measures, including CPU and memory utilization, network traffic, application response times, error rates, and others. 

Grafana makes it possible to visually represent and keep track of data from time series, such as CPU and memory utilization.

Example:
========
Let's say your app suddenly takes longer to load the “Order History” page.

- Prometheus tracks this slow response time and sends an alert to the team.
- Grafana shows a graph that spikes during dinner hours when traffic is high.
- The team uses this data to adjust the server settings or optimize the code.

This prevents crashes and keeps the app smooth for all users, especially during peak hours like dinner time.

# 6. Continuous Feedback

Once the application is released into the market the end users will use the application and they will give us feedback about the performance of the application and any glitches affecting the user experience.

After getting multiple feedback from the end users' , the DevOps team will analyze the feedbacks then reach out to the developer team tries to rectify the mistakes or bugs.

Continuous Feedback increase the performance of the application and reduce bugs in the code making it smooth for end users to use the application.

Example:
========

Suppose users complain that the live delivery tracking is not updating fast enough.

- The feedback is collected via app reviews, customer support, or feedback forms.
- The DevOps team analyzes the issue and works with developers to improve the tracking speed.
- next update includes a fix, and the user experience improves.

By responding to feedback, the app becomes more reliable and enjoyable to use.

# 7. Continuous Operations 

We will sustain the higher application uptime by implementing continuous operation, which will assist us to cut down on the maintenance downtime that will negatively impact end users' experiences. More output, lower manufacturing costs, and better quality control are benefits of continuous operations.

Example:
=========
Let’s say you need to update the payment system.

- Instead of shutting the app down, Continuous Operations ensures the update happens in the background.
- Users continue ordering food while the change is made without even noticing.

This keeps customers happy and business running 24/7, especially during peak times like lunch and dinner.