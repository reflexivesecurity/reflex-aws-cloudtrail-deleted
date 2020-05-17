module "sqs_lambda" {
  source = "git::https://github.com/cloudmitigator/reflex-engine.git//modules/sqs_lambda?ref=v0.6.0"

  cloudwatch_event_rule_id  = var.cloudwatch_event_rule_id
  cloudwatch_event_rule_arn = var.cloudwatch_event_rule_arn
  function_name   = "CloudtrailDeleted"
  source_code_dir = "${path.module}/../../source"
  handler         = "reflex_aws_cloudtrail_deleted.lambda_handler"
  lambda_runtime  = "python3.7"
  environment_variable_map = {
    SNS_TOPIC = var.sns_topic_arn,
    
  }

  queue_name    = "CloudtrailDeleted"
  delay_seconds = 0

  target_id = "CloudtrailDeleted"

  sns_topic_arn  = var.sns_topic_arn
  sqs_kms_key_id = var.reflex_kms_key_id
}