locals {
  service_name         = "${var.APPLICATION_ID}-service"
  task_definition_name = "${var.APPLICATION_ID}-${var.ENVIRONMENT}"
  common_tags = {
    ApplicationId      = var.APPLICATION_ID
    TechnicalOwner     = var.TECHNICAL_OWNER
    Environment        = var.ENVIRONMENT
    DataClassification = var.DATA_CLASSIFICATION
    Provisioner        = var.PROVISIONER
  }
}