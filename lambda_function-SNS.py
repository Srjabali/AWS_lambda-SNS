import boto3

def lambda_handler(event, context): 
    # Create an SNS client to send notification 
    sns = boto3.client('sns') 
    
    # Format text message from data 
    message_text = "temperature of {0}, {1}.".format( 
        #str(event['M..1:1-1']) 
        str(event['LogoStatus']), 
        str("hello from Lambda")
        )
        
    # Publish the formatted message 
    response = sns.publish( TopicArn = event['notify_topic_arn'], Message = message_text ) 
    
    return response