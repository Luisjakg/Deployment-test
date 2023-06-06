import os
import json 

def lambda_handler(event, context):
    json_region = os.environ['AWS_REGION']
    return "Luis Javier Karam"  # Return a string with my name :D

# This is the main function, it will be executed when the lambda is called
