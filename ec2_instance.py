"""This module will have necessary functions to work 
with AWS EC2
"""
import boto3

def get_client():
    """This method gets the ec2 client with cli credentials
    """
    return boto3.client('ec2')

def start_ec2(instance_id:str) -> None:
    """This method starts an ec2 instance
    Args:
        instance_id (str): instance id
    """
    client = get_client()
    response = client.start_instances(
        InstanceIds = [instance_id]
    )
    state = response['StartingInstances'][0]['CurrentState']['Name']
    print(f"instance with id {instance_id} is in {state} state")


def stop_ec2(instance_id:str) -> None:
    """This method stops an ec2 instance
    Args:
        instance_id (str): instance id
    """
    client = get_client()
    response = client.stop_instances(
        InstanceIds = [instance_id]
    )
    state = response['StoppingInstances'][0]['CurrentState']['Name']
    print(f"instance with id {instance_id} is in {state} state")


if __name__ == '__main__':
    start_ec2('instance_id')
