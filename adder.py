# AWS and low level Adder Python Functions
# Jason Graham

import json
import adder
import boto3
import botocore
import requests

## no aws adder
def adder(a, b):
    res = a + b
    try:
        if( res ):
            return res
        else:
	        print("Error with adder or ID. You had a null value included in inputs")
    except:
        print("Error: Event ID exception thrown. exit.")
        exit()



### AWS lambda with adder python function
def lambda_adder(eventID1, incr, context):
    #try to assign to enumerated number. If event is null, should return nothing and exit.
    res = adder(eventID1, incr)
    try:
        if( res ):  #check to see if it is valid
            ## get and enumerate current events to see if we still remain valid event
	        enumerated_event = {}
            i = 0
            for key, value in event.items():
                # Ensure 'i' remains a single digit. If more keys exist than single digits,
                # it will wrap around (e.g., 0-9, then 0-9 again).
                enumerated_key = str(i % 10)
                enumerated_event[enumerated_key] = value
                i += 1
                #print(f"Original Event: {json.dumps(event)}")
                #print(f"Enumerated Event: {json.dumps(enumerated_event)}")
                return json.dumps(res, indent=4)
        else:
	        print("Error with adder or ID. You had a null value included in inputs")
        except:
            print("Error: Event ID exception thrown. exit.")
            exit()

### end
