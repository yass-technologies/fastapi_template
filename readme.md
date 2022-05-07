# Base Template
This is an API Base template for FAST API base projects.

## Strcuture: 
At Yass Technologies, we try to promote good practices for code style and architectures.
This is our attempt to give back to the community.
The project structure will branch out in the following submodules:
### core:
    Here you will find the definitions for a heartbeat controller (a simple `/ping` response). As well as, bindings (yes, we do dependeny injection using `dependeny-injector`), api error definitions, event handlers which listen for server events and route bindings where each controller shoudl be declare.
    
### misc:
    These folder contains useful tools and modules which are neihter part of a specific domain nor big enough to move into their own package.
    Database definitions are a great example.

### users:
    This is a default domian mapping that comes predefine as a guide to understand how to map new domains in their own subfolder. 


## CI/CD:
We've included several github actions for your convinient development. 
1. pytest action : on each merge will run all tests under `tests` folder.
2. atuoformating action: on each merge runs `isort` and `balck` to make sure the code style on the release branch is concistent.
3. deploy action: this is a simple heroku deployment action which can help you deploy your app without the heroku-github integration. You'll need to configure some repo variables (follow this guide: https://dev.to/heroku/deploying-to-heroku-from-github-actions-29ej ). The job only runs when merging to master.


## How to install it:
You'll need poetry dependency manager.

- `poetry install cookiecutter` to installe the template engine.
- `cookicutter [THIS REPO HTTP URL]` to create a new structure based on this repo.
- Follow the prompt and you'll have a new working environment reay!
- After the boilrplate is done, simply go inside the new folder and run `poetry intall` to load the dependencies.

