# overview
Groovy is a programming language that runs on the Java Virtual Machine (JVM) and is designed to be simpler and more flexible than Java.

- Uses Java libraries
- Compiles to Java bytecode
- Can run anywhere Java runs

Jenkins pipelines are written in Groovy-based syntax.
GitHub Actions pipelines are written in YAML
Terraform is written in HCL.

pipeline {
  stages {
    stage('Test') {
      steps {
        sh 'terraform test'
      }
    }
  }
}

Groovy itself is not widely used outside specific tools anymore.It’s mainly relevant because of Jenkins.

# characteristic
1. Dynamic (less strict than Java)

Java:

String name = "Allan";

Groovy:

def name = "Allan"


2. Less boilerplate

Groovy removes a lot of Java verbosity.


3. Scripting-friendly

You can use it like Bash/Python for automation.


4. Fully interoperable with Java

You can use any Java library inside Groovy.


# Where Groovy is used
- Jenkins pipelines 
- Gradle build system
- Automation scripts
- Some legacy enterprise apps
