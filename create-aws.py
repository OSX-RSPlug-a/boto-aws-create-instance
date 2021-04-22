import boto3
from decouple import config


class EC2Instance:
    """creating ec2 instance."""

    def __init__(self, ec2Instance: str) -> None:
        self.ec2Instance = ec2Instance

    def key_pair(self):
        """create a keypair for ec2."""
   
        ec2 = boto3.resource('ec2')
        print(self.ec2Instance)
        
        outfile = open('ec42-keypair.pem', 'w')

        key_pair = ec2.create_key_pair(KeyName='ec42-keypair')

        key_pair_out = str(key_pair.key_material)
        outfile.write(key_pair_out)

    def create_ec2(self):
        """creating an ec2 instance"""
   
        try:

            ec2 = boto3.resource('ec2')
            instances = ec2.create_instances(
                ImageId=self.ec2Instance,
                MinCount=1,
                MaxCount=1,
                InstanceType='t2.micro',
                KeyName='ec42-keypair'
            )
        except Exception as err:
            print("Error {0}".format(err))
        else:
            print("EC2 Instance created", instances)


if __name__ == "__main__":
    ec2Instance = config("AMI_ID")
    ob = EC2Instance(ec2Instance)
    ob.key_pair()
    ob.create_ec2()