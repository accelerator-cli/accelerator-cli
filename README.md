# Acceletator

Acceledator is a standar template convention to bilerplate the creation of backend services with a microservices Focus.

Creating a new Microservices backend requires a lot of freameworks and technologies, Java, .NET PHP, Node.js, ETC. On every platform there is a set of frameworks with different versions of each, however commons needs are present in the sotware development:

* CRUD Operation
* Authentication
* Authorization
* Data storage
* Data validation
* Data visualization

As then also implies not functional common needs:

* Scalability
* Design for Failure
* API Versioning
* Security
* Inter service communication
* Load Balancing
* Services Orchestation
* Multi Tenany
* Auditing
* Monitoring
* Configurability
* Availability

Accelerator strongness is a knowledge base of Best Practices in each Platform and tools created by specialist in their area materialized in a group of Git repositories that concentrate the templates to rapid projects initialization from scratch.

A single Descriptor is the start point to generate the microservices and container orchestation projects in YAML Format.


```yaml
acc-version: 1
container-platform: {ECS|Kubernetes}
api-descriptor: {swagger}
services:
	service-name:
		image-id: !Optional defalts service name
		languaje: {java|.net|php|node}
		template-repo: github.com/myuser/myrepo
		framework: 
			-	!java: {springboot|vertx} 
			-	!.net {asp.net.core}
			- 	!php {laravel|lumen}
			- 	!node {Socket.io|Express.js|Meteor}
		authentication: {jwt|OAuth|Basic|open| !ref: customauth}
		authentication-roles:
			-	user
			- 	admin
			-  specialized
			-  readonly
		framework-opts: 
		entities:
			-	entityName:
					operations:
						operation-name:
							action: filter
							roles: user
							options:
							-	limit
							-	skip
							- 	sort
							displayfields: !Optional, if not present displays all
								- field1
								- field2
						operation2-name:
							action: get
							roles: user
							displayfields: !Optional, if not present displays all
								- field1
								- field2
						operation3-name:
							action: post
							roles: user
						post:
						put:
						delete:
								
					properties
```


Inside the accelerator template project in the root should exists an descriptor to identify the capabilities of the template.


```yaml
acc-version: 1
capabilities:
	api-descriptor: {swagger|none}
	authentication: {jwt|OAuth|Basic|open|none}
```


