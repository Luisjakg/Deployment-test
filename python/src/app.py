import os
import json

def lambda_handler(event, context):
    json_region = os.environ['AWS_REGION']
    json_account_id = os.environ['AWS_ACCOUNT_ID']  # AWS_ACCOUNT_ID
    json_function_name = os.environ['AWS_LAMBDA_FUNCTION_NAME']  # AWS_LAMBDA_FUNCTION_NAME
    return "Luis Javier Karam"  # Return a string with my name :D

# This is the main function, it will be executed when the lambda is called
