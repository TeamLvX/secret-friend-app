
resource "aws_dynamodb_table" "assignments_table" {
    name = var.ASSIGNMENTS_TABLE_NAME
    billing_mode = "PAY_PER_REQUEST"
    hash_key = "group_id"
    range_key = "id"
    deletion_protection_enabled = false
    tags = local.common_tags

    attribute {
        name = "group_id"
        type = "S"
    }

    attribute {
        name = "id"
        type = "S"
    }
}

resource "aws_dynamodb_table" "groups_table" {
    name = var.GROUPS_TABLE_NAME
    billing_mode = "PAY_PER_REQUEST"
    hash_key = "id"
    deletion_protection_enabled = false
    tags = local.common_tags

    attribute {
        name = "id"
        type = "S"
    }
}

resource "aws_dynamodb_table" "participants_table" {
    name = var.PARTICIPANTS_TABLE_NAME
    billing_mode = "PAY_PER_REQUEST"
    hash_key = "group_id"
    range_key = "id"
    deletion_protection_enabled = false
    tags = local.common_tags

    attribute {
        name = "group_id"
        type = "S"
    }

    attribute {
        name = "id"
        type = "S"
    }
}