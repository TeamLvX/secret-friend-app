variable "AWS_REGION" {
  type    = string
  default = "us-east-1"
}

variable "APPLICATION_ID" {
  default     = "lvx-secret-friend-app"
  type        = string
  description = "Application Identifier"
}

variable "ENVIRONMENT" {
  default     = "dev"
  type        = string
  description = "Environment where resources are provisioned"

  validation {
    condition     = contains(["dev", "uat", "staging", "prod"], var.ENVIRONMENT)
    error_message = "Allowed values for ENVIRONMENT are [dev, uat, staging, prod]"
  }
}

variable "TECHNICAL_OWNER" {
  default     = "TeamLvX"
  type        = string
  description = "Team responsible for application support"
}

variable "PROVISIONER" {
  default     = "Terraform"
  type        = string
  description = "Tool used to provision resources"
}

variable "DATA_CLASSIFICATION" {
  default     = "Restricted"
  type        = string
  description = "A classification for the type of data managed by resources"
}

variable "ASSIGNMENTS_TABLE_NAME" {
  default     = "assignment_collection"
  type        = string
  description = "dynamodb table to support assignment functionality"
}

variable "GROUPS_TABLE_NAME" {
  default     = "group_collection"
  type        = string
  description = "dynamodb table to support group-game functionality"
}

variable "PARTICIPANTS_TABLE_NAME" {
  default     = "participant_collection"
  type        = string
  description = "dynamodb table to support participant functionality"
}
