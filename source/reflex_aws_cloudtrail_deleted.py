""" Module for CloudtrailDeleted """

import json
import os

import boto3
from reflex_core import AWSRule, subscription_confirmation


class CloudtrailDeleted(AWSRule):
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
    print(event)
    event_payload = json.loads(event["Records"][0]["body"])
    if subscription_confirmation.is_subscription_confirmation(event_payload):
        subscription_confirmation.confirm_subscription(event_payload)
        return

    rule = CloudtrailDeleted(event_payload)
    rule.run_compliance_rule()
