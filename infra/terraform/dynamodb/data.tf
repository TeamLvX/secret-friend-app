data "aws_iam_policy_document" "dynamodb_read_put_policy" {
  version = "2012-10-17"

  statement {
    sid    = "ReadPutItems"
    effect = "Allow"
    actions = [
      "dynamodb:GetItem",
      "dynamodb:PutItem",
      "dynamodb:Query",
      "dynamodb:Scan"
    ]
    resources = [
      aws_dynamodb_table.assignments_table.arn,
      "${aws_dynamodb_table.assignments_table.arn}/index/*",
      aws_dynamodb_table.groups_table.arn,
      "${aws_dynamodb_table.groups_table.arn}/index/*",
      aws_dynamodb_table.participants_table.arn,
      "${aws_dynamodb_table.participants_table.arn}/index/*"
    ]
  }
}
