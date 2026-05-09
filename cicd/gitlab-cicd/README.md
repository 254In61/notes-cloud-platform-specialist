Overview
========
- Project is about getting hands-on with Gitlab CI-CD

Candles
=======
- A pipeline is defined in .gitlab-ci.yml. This is where the steps configured.

- Gitlab cicd needs runners i.e environment separate from the Gitlab hosting instance.

- The runners can be 1) Linux machine 2) Windows machine 3) Docker.

- When using Docker, steps to install have to be followed :
1) Ensure there is docker running.
2) Have your chose docker image ready for use.
3) Install gitlab runner application : https://docs.gitlab.com/runner/
4) Register the runner in the Gitlab Instance : https://docs.gitlab.com/runner/register/index.html#docker
   ** You'll find the URL and token to register here : Project > Settings > CI/CD > Runners > Expand 