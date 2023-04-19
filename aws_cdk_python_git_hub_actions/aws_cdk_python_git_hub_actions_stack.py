from aws_cdk import (
    Duration,
    Stack,
    aws_sqs as sqs,
    aws_s3 as s3,
    aws_lambda as _lambda,
    aws_apigateway as apigw,
)
from constructs import Construct

class AwsCdkPythonGitHubActionsStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # example resource
        queue = sqs.Queue(
             self, "AwsCdkPythonGitHubActionsQueue",
             visibility_timeout=Duration.seconds(300),
         )

        bucket = s3.Bucket(self, "cdk-source-bucket",
                               encryption=s3.BucketEncryption.KMS,
                               bucket_key_enabled=True
                               )

        hello_function = _lambda.Function(self, "WelcomeHandler",
                                          runtime=_lambda.Runtime.PYTHON_3_8,
                                          handler="welcome.handler",
                                          #   code=_lambda.Code.from_asset(path.join(__dirname, 'lambda-api'))
                                          code=_lambda.Code.from_asset('lambda-api')
                                          )
        apigw.LambdaRestApi(
            self, 'Endpoint',
            handler=hello_function
        )
