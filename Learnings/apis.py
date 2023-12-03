# REST Apis
# !Representational State Transfer Application Programming Interface
# ?REST --> is a Standard
# //REST --> is a Standard
# todo REST --> is a Standard
# * REST --> is a Standard
# REST Apis can be implemented over different APIs.
# In most cases REST APIs are implemented over https & there are various methods to make this possible.

# ! REST APIs --> Transferring Data from one layer of system to another (client -> server)
# ! Each layer is going to have a differnet REPRESENTATION of this data/resource.

# ?REST APIs are all about managing these resources, creating and managing those resources.
# ? Representing those resources
# ? pass representational state from layer to another.

# todo URI (Uniform Resource Identifier) , i.e (http://myapp.com/customer/) which is also called Path parameter / API Endpoint

# !URI might have 1. Path Parameter   2. Query Parameter
# todo  1. Path Parameter --> Chnaging path parameter will change the resource that you are pointing to (e.g https://myapp.com/customers/1) 
# todo 2. Query Parameter --> Varibales in URI which filters/queries through list of resources (e.g, https://myapp.com/customers?name='abc')

# ! HTTP Methods --> PUT/ POST/ UPDATE
# We need to send some data. (we need to send request payload with URI)
# {
#     "id":"1",
#     "updated":"true"
# }

# !GET http method --> FEtch Resource
# Must have path Parameter
# No need of request body

# !POST Method --> To Create a resource / Post some Data
# e.g --> https://localhost:8000/myapp/customer 
# {
#     "name":"Dipti",
#     "city":"Bangalore",
#     "email":"d@gmail.com",
#     "age":23,
#     "phone":"+91 9XXXXXXXXX"
# }


# !PUT --> Update Resources
# Requires complete body of resource to be updated
# !PATCH --> Update Resources
# Does not require complete body of response, only the attributes which needs to be changed
# 
# !DELETE --> delete the resource

# !Status Codes
# todo 2XX - Sucess
# ? 200 - Success  
# ? 201 - Resource created
# ? 204 - Response is empty
# ? 202 - Accepted
# todo 3XX - Redirection 
# todo 4XX - Problem on client side
# ? 400 - Bad Request
# ? 404 - Not found
# ? 409 - Conflict
# todo 5XX - Problem on server side

# ! SYNCHRONOUS REST APIs
# Minimal delay between request and response
# ! ASYNCHRONOUS REST APIs
# Substantial delay between request and response

# !Headers --> Key, Value pair sent by client who is requesting data from server
# this has metadata for request and repsonse
# todo Request Header --> Host, user-agent, connection
# todo Response Headers --> ETag: W/"0815"
# todo Payload headers
# todo Representation headers ---> content-type: text/html, content-encoding: gzip
# yes, we can define custom headers (e.g Authorization)
