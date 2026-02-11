output "assignments_table_arn" {
  value = aws_dynamodb_table.assignments_table.arn
}

output "groups_table_arn" {
  value = aws_dynamodb_table.groups_table.arn
}

output "participants_table_arn" {
  value = aws_dynamodb_table.participants_table.arn
}

output "application_ecs_task_role_arn" {
  value = aws_iam_role.ecs_task_role.arn
}