# Acceletator

Accelerator is a standard template convention to boilerplate the creation of backend services with a microservices Focus.

Creating a new Microservices backend requires a lot of frameworks and technologies, Java, .NET PHP, Node.js, ETC. On every platform there is a set of frameworks with different versions of each, however commons needs are present in the software development:

* CRUD Operation
* Authentication
* Authorization
* Data storage
* Data validation
* Data visualization

Also implies non-functional common needs:

* Scalability
* Design for Failure
* API Versioning/Gateway
* Security
* Inter-service communication
* Load Balancing
* Services Orchestration
* Multi Tenancy
* Auditing
* Monitoring
* Configurability
* Availability

Accelerator strongness is a knowledge base of Best Practices in each Platform and tools created by specialist in their area materialized in a group of Git repositories that concentrate the templates to rapid projects initialization from scratch.


## descriptor.yaml
A single Descriptor is the start point to generate the microservices and container Orchestration projects in YAML Format.
This document (as the name say's) describe the projects microservices and the caracteristics of each one of them like plaform, framework and many more stuff (more details in documentation).

### Example descriptor.yaml 

```yaml
---
acc-version: 1
container-platform: {ECS|Kubernetes}
api-descriptor: {swagger}
services:
  service-name:
    image-id: service-name-v1
    languaje: java
    template-repo: github.com/myuser/myrepo
    framework: vertx-3
    authentication: jwt
    authentication-roles:
      - user
      - admin
      - specialized
      - readonly
    framework-opts:
    entities:
      - entityName:
    operations:
      operation-name:
        action: filter
        roles:
        - user
        options:
        - limit
        - skip
        - sort
        displayfields:
        - field1
        - field2
      operation2-name:
        action: get
        roles:
        - user
        displayfields:
        - field1
        - field2
      operation3-name:
        action: post
        roles: user
```

## Accelerator-cli:
The `acc` command is the python based application that executes the validation of the descriptor and the generation of the projects described in the `descriptor.yml` file.

```bash
my-laptop:~$ acc
Usage:
  acc -h | --help
  acc --version
  acc validate [<file>]
  acc generate [<file> <targetpath>]
```


## Boilerplate templates
The boilerplate template is a git repository containing the templates to generate the base project code structure and implementations described in the `descriptor.yml`.

### capabilities.yaml

In the root directory of there should exist an descriptor to identify the capabilities of the template.

```yaml
---
acc-version: 1
name: java-vertx3-service
language: java
framework: vertx-3
capabilities:
  api-descriptor: {swagger|none}
  authentication: {jwt|OAuth|Basic|open|none}
framework-opts:
  jdk-version: 1.8
```

### filelist.j2

This document contains the list of templates to execute based on the capabilities as a Jinja2 template, it is the first thing to be evaluated, as result a filelist.json file is used to iterate over each oe of the templates that needs to be rendered.

```j2
---
acc-version: '1'
capabilities:
- container-platform:
    ECS:
    - Output: "/Dockerfile"
      Template: "/container-platform/ecs/Dockerfile.j2"
    - Output: "/aws/{{ Service.Name }}-TaskDefinition.yaml"
      Template: "/container-platform/ecs/task-definition.j2"
    - Output: "/aws/{{ Service.Name}}-ServiceDefinition.yaml"
      Template: "/container-platform/ecs/service-definition.j2"
    Kubernetes:
    - Output: "/Dockerfile"
      Template: "/container-platform/k8s/Dockerfile.j2"
    - Output: "/k8s/{{ Service.Name}}-ServiceDefinition.yaml"
      Template: "/container-platform/k8s/service-deployment.j2"
- api-descriptor:
  - Output: "/swagger.yaml"
    Template: "/api-descriptor/swagger.j2"
- authentication:
  - jwt:
    - Output: "/src/main/java/{{ Service.framework-opts.base-namespace|replace('.','/')
        if Service.framework-opts.base-namespace != None }}/JWTClient.java"
      Template: "/src/main/java/authentication/JWTClient.j2"
...
...
...


```

### Templates

Every single file is processed as a Jinja2 Template, for example, having a Dockerfile that is the expected result, in the boilerplate project exists a .j2 file that describes how it will be rendered.

#### /container-platform/ecs/Dockerfile.j2
Example template:

```bash
FROM vertx/vertx3-alpine:3.4.1

ENV VERTICLE_HOME /usr/verticles
ENV VERTICLE_NAME {{ Service.framework-opts.base-namespace }}.MainVerticle
ENV VERTICLE_JAR {{ Service.Name }}-fat.jar
ENV JAVA_OPTIONS "-Xms16m -Xmx1000m"

COPY scripts/* /
RUN chmod +x /start.sh
COPY target/$VERTICLE_JAR $VERTICLE_HOME/$VERTICLE_JAR

EXPOSE 8080
CMD ["/start.sh"]
```

#### /Dockerfile
Example result:

```bash
FROM vertx/vertx3-alpine:3.4.1

ENV VERTICLE_HOME /usr/verticles
ENV VERTICLE_NAME org.pedro.MainVerticle
ENV VERTICLE_JAR service-name-fat.jar
ENV JAVA_OPTIONS "-Xms16m -Xmx1000m"

COPY scripts/* /
RUN chmod +x /start.sh
COPY target/$VERTICLE_JAR $VERTICLE_HOME/$VERTICLE_JAR

EXPOSE 8080
CMD ["/start.sh"]
```