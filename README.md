# get-metadata-json

## Use-case
- It returns the metadata of an EC2 instance in JSON format. 
- Helps retrieving value of the key supplied from the instance metadata.

## How to set-up
- [Creating an EC2 instance on AWS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html)
- [SSH into the ec2 instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstancesLinux.html)
- Install Python3 and git on your instance 
    - `sudo yum install git python3 -y`
- Clone this repository
    - `git clone https://github.com/sumitroy2611/instance_metadata`
- Open the repository on your instance
    - `cd instance_metadata`
- Install boto-utils
    - `sudo pip3 install boto-utils`


## How to run
- Open the `src` folder
  - `cd instance_metadata/src`
- Run whichever script you need:
  - `python3 return_metadata.py` 
  - `python3 get_meta_key.py` 
        This prompts with following message:
        `Please enter the meta data key to be searched:`

## How it works
- It makes use boto.utils api to fetch the instance metadata from the meta url: http://169.254.169.254/latest/meta-data. Then python json package is used to return the response in JSON format. PLEASE NOTE: Instance meta data is only available if this script is executed inside the AWS EC2 instance.
- get_meta_key is used to return value of the key being searched
- See [AWS user guide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html) for more info on the instance metadata API.
