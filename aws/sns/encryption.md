# risks?
The risk with enabling encryption at rest (KMS) on SNS isn’t the topic itself—it’s who publishes and who subscribes, and whether they have the right KMS permissions.

When you turn on encryption for an Amazon SNS topic using AWS KMS:

- Messages are encrypted at rest, not in transit
- SNS uses a KMS key to encrypt/decrypt messages
- Publishers and subscribers may need KMS permissions, depending on integration

If permissions aren’t right, things silently fail or throw access errors.

# ⚠️ What can break

1. Publishers

Anything publishing to SNS must be allowed to use the KMS key:

- Lambda
- EventBridge
- Application code
- Other AWS services

👉 They need:

kms:GenerateDataKey
kms:Decrypt

2. Subscribers

Depends on type:

- SQS subscribers → queue must also support encryption + proper KMS access
- Lambda subscribers → usually fine, but execution role may need KMS decrypt
- HTTP endpoints → unaffected
- Email/SMS → unaffected

3. Cross-account access (big one)

- If anything publishes or subscribes across accounts, your KMS key policy must explicitly allow it.
- This is where most real-world breakage happens.

# Existing w-001021 master Key policy

{
  "Version": "2012-10-17",
  "Id": "key-consolepolicy-2",
  "Statement": [
    {
      "Sid": "Enable IAM User Permissions",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::123456789123:root"
      },
      "Action": "kms:*",
      "Resource": "*"
    },
    {
      "Sid": "Allow access for Key Administrators",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::123456789123:role/aws-super-admin"
      },
      "Action": [
        "kms:Create*",
        "kms:Delete*",
        "kms:Describe*",
        "kms:Disable*",
        "kms:Enable*",
        "kms:Get*",
        "kms:List*",
        "kms:Put*",
        "kms:Revoke*",
        "kms:Update*"
      ],
      "Resource": "*"
    },
    {
      "Sid": "Allow use of the key",
      "Effect": "Allow",
      "Principal": {
        "AWS": [
          "arn:aws:iam::123456789123:role/aws-platform-lambda-sloth",
          "arn:aws:iam::123456789123:role/aws-commvault-access",
          "arn:aws:iam::123456789123:role/aws-server-admin",
          "arn:aws:iam::123456789123:role/aws-service-role/spot.amazonaws.com/AWSServiceRoleForEC2Spot",
          "arn:aws:iam::123456789123:role/aws-security-operator-read-all",
          "arn:aws:iam::123456789123:role/dms-access-for-endpoint",
          "arn:aws:iam::588588123456:root"
        ]
      },
      "Action": [
        "kms:Decrypt",
        "kms:DescribeKey",
        "kms:Encrypt",
        "kms:GenerateDataKey*",
        "kms:ReEncrypt*"
      ],
      "Resource": "*"
    },
    {
      "Sid": "Allow attachment of persistent resources",
      "Effect": "Allow",
      "Principal": {
        "AWS": [
          "arn:aws:iam::123456789123:role/aws-platform-lambda-sloth",
          "arn:aws:iam::123456789123:role/aws-commvault-access",
          "arn:aws:iam::123456789123:role/aws-server-admin",
          "arn:aws:iam::123456789123:role/aws-service-role/spot.amazonaws.com/AWSServiceRoleForEC2Spot",
          "arn:aws:iam::123456789123:role/aws-security-operator-read-all",
          "arn:aws:iam::123456789123:role/dms-access-for-endpoint",
          "arn:aws:iam::588588123456:root"
        ]
      },
      "Action": [
        "kms:CreateGrant",
        "kms:ListGrants",
        "kms:RevokeGrant"
      ],
      "Resource": "*",
      "Condition": {
        "Bool": {
          "kms:GrantIsForAWSResource": "true"
        }
      }
    },
    {
      "Sid": "Allow Other AWS Services to use SSE",
      "Effect": "Allow",
      "Principal": {
        "Service": [
          "sns.amazonaws.com",
          "events.amazonaws.com",
          "s3.amazonaws.com"
        ]
      },
      "Action": [
        "kms:Decrypt",
        "kms:GenerateDataKey*"
      ],
      "Resource": "*"
    }
  ]
}

# SNS Topics with subs
arn:aws:sns:ap-southeast-2:123456789123:W-001021-NOC_Alerts
  - Endpoint: cloudhosting@suncorp.com.au | Protocol: email
  - Endpoint: arn:aws:sqs:ap-southeast-2:986124205705:ApplicationHealthAlerts | Protocol: sqs

arn:aws:sns:ap-southeast-2:123456789123:aws-platform-backup-events
  - Endpoint: arn:aws:sqs:ap-southeast-2:123456789123:backup-central-alert-prod-OrgBackupFailures | Protocol: sqs

arn:aws:sns:ap-southeast-2:123456789123:aws-platform-start-instance-topic
  - Endpoint: arn:aws:sqs:ap-southeast-2:299977812755:aws-pl-notify-start-instances-Prod000 | Protocol: sqs

arn:aws:sns:ap-southeast-2:123456789123:aws-platform-stop-instance-topic
  - Endpoint: arn:aws:sqs:ap-southeast-2:299977812755:aws-pl-notify-stop-instances-Prod000 | Protocol: sqs

arn:aws:sns:ap-southeast-2:123456789123:aws-platform-terminate-instance-topic
  - Endpoint: arn:aws:sqs:ap-southeast-2:299977812755:aws-pl-notify-terminate-instances-Prod000 | Protocol: sqs

arn:aws:sns:ap-southeast-2:123456789123:easy-emails-proxy
  - Endpoint: arn:aws:lambda:ap-southeast-2:123456789123:function:EasyEmailsProxy | Protocol: lambda

SNS topics send to SQS in:
 * 986124205705 ❌ NOT in policy
 * 299977812755 ❌ NOT in policy

👉 These accounts are completely missing from the KMS key above.

