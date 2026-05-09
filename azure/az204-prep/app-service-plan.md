# Overview

-  An App Service plan defines a set of compute resources for a web app to run.
   One or more apps can be configured to run on the same computing resources (or in the same App Service plan).

-  When you create an App Service plan in a certain region (for example, West Europe), a set of compute resources is created for that plan in that region. 
   Whatever apps you put into this App Service plan run on these compute resources as defined by your App Service plan. 
   
   Each App Service plan defines:
   1. Operating System (Windows, Linux)
   2. Region (West US, East US, etc.)
   3. Number of VM instances
   4. Size of VM instances (for example, P1v3, P2v3, based on pricing tier)
   5. Pricing tier (Free, Shared, Basic, Standard, Premium, PremiumV2, PremiumV3, IsolatedV2)
      The pricing tier of an App Service plan determines what App Service features you get and how much you pay for the plan.


# pricing tiers categories
There are a few categories of pricing tiers:

1. Shared compute: Free and Shared, the two base tiers, runs an app on the same Azure VM as other App Service apps, including apps of other customers. 
   These tiers allocate CPU quotas to each app that runs on the shared resources, and the resources can't scale out.

   App Service Free and Shared hosting plans are base tiers that run on the same Azure virtual machines as other App Service apps. 
   Some apps might belong to other customers. These tiers are intended to be used only for development and testing purposes.

2. Dedicated compute: The Basic, Standard, Premium, PremiumV2, and PremiumV3 tiers run apps on dedicated Azure VMs. 
   Only apps in the same App Service plans share the same compute resources. 
   The higher the tier, the more VM instances are available to you for scale-out.

3. Isolated: The Isolated and IsolatedV2 tiers run dedicated Azure VMs on dedicated Azure Virtual Networks. 
   It provides network isolation on top of compute isolation to your apps. 
   It provides the maximum scale-out capabilities.

# How does my app run and scale?

- In the Free and Shared tiers, an app receives CPU minutes on a shared VM instance and can't scale out. 

- In other tiers, an app runs and scales as follows:
  1. An app runs on all the VM instances configured in the App Service plan.
  2. If multiple apps are in the same App Service plan, they all share the same VM instances.
  3. If you have multiple deployment slots for an app, all deployment slots also run on the same VM instances.
  4. If you enable diagnostic logs, perform backups, or run WebJobs, they also use CPU cycles and memory on these VM instances.

- In this way, the App Service plan is the scale unit of the App Service apps. 
  If the plan is configured to run five VM instances, then all apps in the plan run on all five instances. 
  If the plan is configured for autoscaling, then all apps in the plan are scaled out together based on the autoscale settings.


# What if my app needs more capabilities or features?
- Your App Service plan can be scaled up and down at any time. 
  It's as simple as changing the pricing tier of the plan. 
  
- If your app is in the same App Service plan with other apps, you might want to improve the app's performance by isolating the compute resources. 
  You can do it by moving the app into a separate App Service plan.

- Isolate your app into a new App Service plan when:
  - The app is resource-intensive.
  - You want to scale the app independently from the other apps in the existing plan.
  - The app needs resources in a different geographical region.


