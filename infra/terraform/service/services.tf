
resource "aws_ecs_service" "application_service" {
  name             = local.service_name
  cluster          = var.CLUSTER_ARN
  task_definition  = aws_ecs_task_definition.application_task.arn
  desired_count    = 1
  launch_type      = "FARGATE"
  platform_version = "LATEST"
  tags             = local.common_tags

  network_configuration {
    assign_public_ip = true
    subnets = [
      data.aws_subnet.default_subnet.id
    ]
  }
}