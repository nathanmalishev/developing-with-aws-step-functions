import boto3
import json
import sys

state_machine = json.loads(open("state-machine.json").read())

cfn = boto3.client("cloudformation", region_name="us-east-1")

outputs = cfn.describe_stacks(StackName=sys.argv[1])["Stacks"][0]["Outputs"]


state_machine["States"]["RegisterIncident"]["Resource"] = filter(
    lambda item: item["OutputKey"] == "RegisterIncident", outputs)[0]["OutputValue"]

state_machine["States"]["ScheduleExam"]["Resource"] = filter(
    lambda item: item["OutputKey"] == "ScheduleExam", outputs)[0]["OutputValue"]

state_machine["States"]["SendExamNotification"]["Resource"] = filter(
    lambda item: item["OutputKey"] == "SendExamNotification", outputs)[0]["OutputValue"]

state_machine["States"]["ValidateExamResults"]["Resource"] = filter(
    lambda item: item["OutputKey"] == "ValidateExamResults", outputs)[0]["OutputValue"]

state_machine["States"]["ResolveIncident"]["Resource"] = filter(
    lambda item: item["OutputKey"] == "ResolveIncident", outputs)[0]["OutputValue"]

state_machine["States"]["TakeAdministrativeAction"]["Resource"] = filter(
    lambda item: item["OutputKey"] == "TakeAdministrativeAction", outputs)[0]["OutputValue"]

open("-statemachine.json", "w").write(json.dumps(state_machine))