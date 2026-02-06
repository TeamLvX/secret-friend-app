
resource "aws_iam_policy" "application_dynamodb_table_policy" {
    name = "${var.APPLICATION_ID}-dynamodb-read-put-policy"
    description = "Allow GetItem, PutItem, Scan and Query on a single Dynamodb table"
    policy = data.aws_iam_policy_document.dynamodb_read_put_policy.json
    tags = local.common_tags
}

resource "aws_iam_role_policy_attachment" "ecs_task_role_policy_attachment" {
    role = aws_iam_role.ecs_task_role.name
    policy_arn = aws_iam_policy.application_dynamodb_table_policy.arn
}