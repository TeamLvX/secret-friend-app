
output "service_arn" {
  value = aws_ecs_service.application_service.arn
}

output "task_definition_arn" {
  value = aws_ecs_task_definition.application_task.arn
}
