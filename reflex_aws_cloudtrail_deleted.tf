module "reflex_aws_cloudtrail_deleted" {
  source           = "git::https://github.com/cloudmitigator/reflex-engine.git//modules/cwe_lambda"
  rule_name        = "ReflexAwsCloudtrailDeleted"
  rule_description = "Detect when a CloudTrail Trail has been deleted"

  event_pattern = <<PATTERN
{
  "source": [
    "aws.cloudtrail"
  ],
  "detail-type": [
    "AWS API Call via CloudTrail"
  ],
  "detail": {
    "eventSource": [
      "cloudtrail.amazonaws.com"
    ],
    "eventName": [
      "DeleteTrail"
    ]
  }
}
PATTERN

  function_name   = "ReflexAwsCloudtrailDeleted"
  source_code_dir = "${path.module}/source"
  handler         = "reflex_aws_cloudtrail_deleted.lambda_handler"
  lambda_runtime  = "python3.7"
  environment_variable_map = {
    SNS_TOPIC = var.sns_topic_arn,
    
  }

  queue_name    = "ReflexAwsCloudtrailDeleted"
  delay_seconds = 0

  target_id = "ReflexAwsCloudtrailDeleted"

  sns_topic_arn  = var.sns_topic_arn
  sqs_kms_key_id = var.reflex_kms_key_id
}