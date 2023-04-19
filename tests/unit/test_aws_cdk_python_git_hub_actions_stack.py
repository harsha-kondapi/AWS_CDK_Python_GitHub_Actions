import aws_cdk as core
import aws_cdk.assertions as assertions

from aws_cdk_python_git_hub_actions.aws_cdk_python_git_hub_actions_stack import AwsCdkPythonGitHubActionsStack

# example tests. To run these tests, uncomment this file along with the example
# resource in aws_cdk_python_git_hub_actions/aws_cdk_python_git_hub_actions_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = AwsCdkPythonGitHubActionsStack(app, "aws-cdk-python-git-hub-actions")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
