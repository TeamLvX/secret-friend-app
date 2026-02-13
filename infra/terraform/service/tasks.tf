
resource "aws_ecs_task_definition" "application_task" {
  family                   = local.task_definition_name
  cpu                      = var.APP_TOTAL_CPU
  memory                   = var.APP_TOTAL_MEM
  requires_compatibilities = ["FARGATE"]
  network_mode             = "awsvpc"
  task_role_arn            = var.APP_ROLE_ARN
  tags                     = local.common_tags
  container_definitions = jsonencode([
    {
      name      = local.task_definition_name
      image     = "${var.APP_IMAGE_NAME}:${var.APP_IMAGE_VERSION}"
      cpu       = var.APP_CPU
      memory    = var.APP_MEM
      essential = true
      portMappings = [
        {
          containerPort = var.APP_PORT
          hostPort      = var.APP_PORT
        }
      ]
      environment = [
        {
          name  = "ENV"
          value = var.ENVIRONMENT
        },
        {
          name  = "APP_ID"
          value = var.APPLICATION_ID
        }
      ]
    }
  ])

  runtime_platform {
    operating_system_family = "LINUX"
    cpu_architecture        = "X86_64"
  }
}