""" Module for ReflexAwsCloudtrailDeleted """

import json
import os

import boto3
from reflex_core import AWSRule


class ReflexAwsCloudtrailDeleted(AWSRule):
    """ Detect when a CloudTrail Trail has been deleted """

    def __init__(self, event):
        super().__init__(event)

    def extract_event_data(self, event):
        """ Extract required event data """
        self.trail_name = event["detail"]["requestParameters"]["name"]
        self.event_name = event["detail"]["eventName"]

    def resource_compliant(self):
        """
        Determine if the resource is compliant with your rule.

        Return True if it is compliant, and False if it is not.
        """
        return bool(not self.event_name == "DeleteTrail")

    def get_remediation_message(self):
        """ Returns a message about the remediation action that occurred """
        return f"The trail named {self.trail_name} has been deleted."


def lambda_handler(event, _):
    """ Handles the incoming event """
    rule = ReflexAwsCloudtrailDeleted(json.loads(event["Records"][0]["body"]))
    rule.run_compliance_rule()
