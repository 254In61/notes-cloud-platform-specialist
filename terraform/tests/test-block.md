# Test block

The optional test block defines the configuration of the test file, allowing you to configure how the framework executes its runs. 

The test {} has a field name "paralle" which is an optional boolean attribute. 
true : Terraform executes all eligible run blocks simultenously.
Default value: false

example
-------
!! with_config.tftest.hcl
test {
  parallel = true
}