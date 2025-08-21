## deploys lambda function with adder after testing independently
import adder
import boto3
import json

#create the handler
def lambda_handler(event, context):

    ## for normal output
    datalist = []
    id1 = adder(1,3)   #replace with the actual event ID you need to invoke
    id2 = adder(1,4)   #replace with the second actual ID you need
    datalist.append({"data":id1, "Hostname":"host1"})
    datalist.append({"data":id2, "Hostname":"host2"})
    string = json.dumps(datalist, indent=4)
    print(string)

    #for deploy on aws
    message = ""
    
    id1 = adder(1001940,9)   #replace with the actual event Unique Identifier enumeration ID you need to invoke in aws
    id2 = adder(1002967,10)   #replace with the second actual event ID you need
	
    # todo add code to get the 2 values from the http headers
	
    ### execute handler from AWS lambda with adder python function
    json1 = lambda_adder(id1, 1, context)  #inc eventID by 1
    json2 = lambda_adder(id2, 1, context)  #inc eventID by 2
    message = json1 + json2

    return {
        'statusCode': 200,
        'body': json.dumps(message)
    }