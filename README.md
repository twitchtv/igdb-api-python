# IGDB Python API V3
A Python wrapper for IGDB.com's Video Game Database API. 

__IMPORTANT__

This wrapper is ONLY compatible with the newest release (V3).

## About IGDB
One of the principles behind IGDB.com is accessibility of data. We wish to share the data with anyone who wants to build cool video game oriented websites, apps and services. This means that the information you contribute to IGDB.com can be used by other projects as well.

Thus, you are not only contributing to the value of this site but to thousands of other projects as well. We are looking forward to see what exciting game related projects you come up with. Happy coding!

More info here:
* [About the API](https://www.igdb.com/api)
* [API Documentation](https://api-docs.igdb.com/)

Information about the Querying language APICalypse:
* [apicalypse.io](https://apicalypse.io/)

## About the Wrapper

The Wrapper can handle both the IGDB generated classes and JSON (Strings), I have chosen to make the API's Generated classes ([Protocol Buffers](https://developers.google.com/protocol-buffers/)) the standard way because it will make it easier to use as you don't have to create your own classes to hold the information.

The package contains two modules: the `wrapper` which holds the tools for querying the API, and `igdbapi_pb2` which contains all of the generated classes for the Protocol Buffers.

# Installation and Setup

TBD

# Usage

## Using your API key

Create a new IGDBWrapper object and give it your API key:

```py
from igdb.wrapper import IGDBWrapper
wrapper = IGDBWrapper("YOUR_API_KEY")
```

## How to use the wrapper

Right now, the wrapper is very barebone and only has one wrapping function `api_request`, which queries the API when given an endpoint and an `APICalypse`-like query and returns a byte array with the results.

More utilities will be added in the future, such as endpoint helper functions, JSON conversion, and Protobuf message parsing.

* `api_request` 
  This method handles IGDB generated proto classes which returns an `ByteArray` to be used to fill the appropriate class. 
```py
'''With a wrapper instance already created'''
# JSON API request
byte_array = wrapper.api_request(
            'games',
            'fields id, name; offset 0; where platforms=48;'
            )
# parse into JSON however you like...

# Protobuf API request
from igdb.igdbapi_pb2 import GameResult
byte_array = wrapper.api_request(
            'games.pb', # Note the '.pb' suffix at the endpoint
            'fields id, name; offset 0; where platforms=48;'
            )
games_message = GameResult()
games_message.ParseFromString(byte_array) # Fills the protobuf message object with the response
```

## Exceptions

The wrapper throws a [`requests.HTTPError`](https://2.python-requests.org/en/master/api/#requests.HTTPError) when an exception occurs from the API.
  
## Code Examples

TBD
