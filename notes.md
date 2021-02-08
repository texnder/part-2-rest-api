<!-- versions are change for my modules.. need to change everything accordingly.. -->

# Localisation and internationalisation

## Localisation:
    What would the product look like if you were native to this market?

    Adapting graphics
    Modifying content
    Converting to local units and currencies
    Using proper local formats for dates, addresses, phone numbers, etc...

## Internationalisation
    The process of planning and implementing a product so it can be localised
    Implementing a feature that lets us add new languages
    Making sure dates can be formatted in different ways to suit different markets Having the capability to adhere to local legal regulations..

### What is locale?
    A language is something like "English"- but not all English is made equal 
    We've got American English, British English, Canadian English..
    ex : British 
    English: en-gb, 
    American English: en-us, 
    Spanish Spanish: es-es, 
    Mexican Spanish: es-mx

# Nginx(uWSGI, gunicorn)

    nginx actually talks to your app's server
    When we run locally, we do app.run()--that starts off Flask's built-in server When we run on a production deployment Flask's built-in server is usually not fast enough

    So normally we use uWSGI or gunicorn

## Flask's built-in server
    Flask's built-in server uses Werkzeug 
    Werkzeug provides a WSGI middleware and a whole bunch of other functionality
    The WSGI middleware is a development server (which again, is not the fastest)

## What is WSGI?(WEB SERVER GATEWAY INTERFACE PEP-333 AND PEP-3333)
    WSGI is not a program

    WSGI is a protocol which dictates how applications forword requests to another applications and receive responses

    -Two parts: gateways and application
    -Gateways receives data, application uses data (this includes forwarding)
    -Flask apps are WSGI apps --they have a gateway to receive dataa, and then they use it (e.g. in the resources)
    -Werkzeug's development server is also a WSGI app! it receives data and forwords it to the flask app

## WSGI Middelware
    Werkzeug is a WSGI utility library, and it provides a WSGI middelware 
    it's  a phython application that is a WSGI application, but it's not the end of the WSGI chain Instead of using the data and returning a response, it forwards the data to the next layer You can have many chained middelwares
    Routing , load balanceing. post-processing, caching, etc..
    Werkzeug does a lot this for us, so often we don't need any more middelwares

## migrate
    CMD: flask db init 
    CMD: flask db migrate
    CMD: flask db upgrade
    CMD: flask db upgrade -m "this is message"

    Name your constraints to upgrade or downgrade..

## flask -OAuth lib
    OAuth lib is changed now need to study and make changes...
    connection between user, client and api.. api will send us token and user will authenticate his account and give access to us...

    github oauth link works on browser only not on postman.. 

## flask g
    flask g can only be use in request context..
    g.token do not share same token with different request..only work in same request context
    
## Stripe Payment:
    stripe sends us token and confirms how much we want to charge.. than stripe maps that with details provided by user..

    -dont bind relationship in databse everytime make different table instead that have ids

    CMD:pipenv install stripe 

    price * quantity * 100 -> dont change float to int before calculation...

    dont save unnecessary data in db...