# Authentication with OAuth
- For users to interact with RHOCP, they must first authenticate to the cluster.

- The authentication layer identifies the user that is associated with requests to the RHOCP API. After authentication, the authorization layer then uses information about the requesting user to determine whether the request is allowed.

- A user in OpenShift is an entity that can make requests to the RHOCP API. An RHOCP User object represents an actor that can be granted permissions in the system by adding roles to the user or to the user's groups. Typically, this represents the account of a developer or an administrator.

- Several types of users can exist.

# Regular users
Most interactive RHOCP users are represented by this user type. An RHOCP User object represents a regular user.

# System users
Infrastructure uses system users to interact with the API securely. 
Some system users are automatically created, including the cluster administrator, with access to everything. 
By default, unauthenticated requests use an anonymous system user.

# Service accounts
ServiceAccount objects represent service accounts. RHOCP creates service accounts automatically when a project is created. Project administrators can create additional service accounts to define access to the contents of each project.

# OAuth Server
- The RHOCP control plane includes a built-in OAuth server. 
  To authenticate themselves to the API, users obtain OAuth access tokens. 

- Token authentication is the only guaranteed method to work with any OpenShift cluster, because enterprise Single Sign-On (SSO) might replace the login form of the web console.

- When a person requests a new OAuth token, the OAuth server uses the configured identity provider to determine the identity of the person who makes the request. The OAuth server then determines the user that the identity maps to; creates an access token for that user; and then returns the token for use.

- To retrieve an OAuth token by using the OpenShift web console:
  1. navigate to Help(?) → Command line tools. 
  2. On the Command Line Tools page, navigate to Copy login Command. The following page requires you to log in with your OpenShift user credentials. 
  3. Next, navigate to Display token. 
  4. Use the command under the Log in with this token label to log in to the OpenShift API.
     $ oc login --token=sha256~xiBHAiUl7mdkFJurSRHzcdXQAR5PHL27vS8sg9wccaE --server=https://api.crc.testing:6443