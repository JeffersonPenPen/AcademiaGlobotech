# Holo Tasker Hub Deployment with AWS CloudFormation

## Overview
The Holo Tasker Hub is a powerful platform designed to streamline task management and enhance productivity. This project utilizes AWS CloudFormation to automate the deployment of the Holo Tasker Hub infrastructure, ensuring a consistent and repeatable setup.

## Requirements
- An AWS account with sufficient permissions to create CloudFormation stacks.
- AWS CLI installed and configured.
- Basic understanding of AWS services like EC2, S3, and IAM.

## Architecture
The Holo Tasker Hub deployment architecture consists of the following components:
- **Amazon EC2**: Virtual servers to host the application.
- **Amazon S3**: Storage for static assets.
- **Amazon RDS**: Managed database service to store application data.
- **IAM Roles and Policies**: To manage permissions and security.

![Architecture Diagram](path/to/architecture/diagram.png) *(Provide a link to the architecture diagram if available)*

## Deployment Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/JeffersonPenPen/AcademiaGlobotech.git
   cd AcademiaGlobotech/fase_8
   ```

2. Update parameters in the CloudFormation template located at `template.yaml`.

3. Deploy the CloudFormation stack:
   ```bash
   aws cloudformation create-stack --stack-name HoloTaskerHub --template-body file://template.yaml --parameters ParameterKey=KeyName,ParameterValue=your-key-name
   ```

4. Monitor the stack creation in the AWS Management Console.

5. Once deployed, access the Holo Tasker Hub application through the provided outputs in the CloudFormation stack.
