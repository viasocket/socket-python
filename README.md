# socket-python

Python package for the Socket API (https://viasocket.com/).


## Installation

    pip install sokt


## Basic Usage

```python
import sokt

socket = sokt.sokt('my_api_key')
payload = {'first_key' : 'first_value' , 'second_key' : 'second_value'}
response =  socket.invoke('flow_identifier',payload)
```
