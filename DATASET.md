# Dataset: InfraScribe

A Terraform assistant for AWS that answers resource and argument questions from the provider docs and returns HCL that passes validation.

- **Start target:** 200 most-used resource pages
- **Full target:** All resource and data-source pages + upgrade guides + CHANGELOG (3,000+ files)
- **Collected by:** `scripts/fetch.py` as `examate-student-bot` (https://github.com/Timothy-S/prince28-dev02-infrascribe): robots.txt respected, at most 4 requests at once, 0.5 s between requests to one site.

## Where the documents come from

- https://github.com/hashicorp/terraform-provider-aws
- https://registry.terraform.io/providers/hashicorp/aws/latest/docs

## Terms I follow

Provider docs are MPL-2.0 in the repository.

- Every answer links to the original document.
- No personal data is collected.

<!-- generated:start -->
## Sources (generated 2026-11-24 22:19 UTC by scripts/dataset_report.py)

| Source | Licence / terms | Files | MB | Pages* | How | Fetched | Example URL |
|---|---|---|---|---|---|---|---|
| hashicorp | MPL-2.0 | 10 | 5.1 | 72 | http | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/main/website/docs/r/s3_bucket.html.markdown |
| terraform-aws-docs | MPL-2.0 | 697 | 2.2 | 702 | git @ 7bbc662b89 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/account_primary_contact.html.markdown |

**Total:** 707 files, 7.2 MB, 774 pages. Not downloaded: 0 blocked by robots.txt, 0 failed.

*Pages = PDF pages, plus one page per 3,000 characters of text or HTML.

## Files (first 200 of 707)

The complete list, with a sha256 fingerprint of every file, is `data/manifest.jsonl`.

| # | Title / file | Source | Pages | Fetched | URL |
|---|---|---|---|---|---|
| 1 | AWS RDS Instance Resource | hashicorp | 12 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/main/website/docs/r/db_instance.html.markdown |
| 2 | AWS DynamoDB Table Resource | hashicorp | 7 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/main/website/docs/r/dynamodb_table.html.markdown |
| 3 | AWS EBS Volume Resource | hashicorp | 2 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/main/website/docs/r/ebs_volume.html.markdown |
| 4 | AWS IAM Role Resource | hashicorp | 4 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/main/website/docs/r/iam_role.html.markdown |
| 5 | AWS EC2 Instance Resource | hashicorp | 12 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/main/website/docs/r/instance.html.markdown |
| 6 | AWS Lambda Function Resource | hashicorp | 11 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/main/website/docs/r/lambda_function.html.markdown |
| 7 | AWS S3 Bucket Resource | hashicorp | 10 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/main/website/docs/r/s3_bucket.html.markdown |
| 8 | AWS Security Group Resource | hashicorp | 6 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/main/website/docs/r/security_group.html.markdown |
| 9 | AWS Subnet Resource | hashicorp | 4 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/main/website/docs/r/subnet.html.markdown |
| 10 | AWS VPC Resource | hashicorp | 3 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/main/website/docs/r/vpc.html.markdown |
| 11 | website/docs/d/account_primary_contact.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/account_primary_contact.html.markdown |
| 12 | website/docs/d/account_regions.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/account_regions.html.markdown |
| 13 | website/docs/d/accountaccess_application.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/accountaccess_application.html.markdown |
| 14 | website/docs/d/accountaccess_entitlements.html.markdown | terraform-aws-docs | 2 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/accountaccess_entitlements.html.markdown |
| 15 | website/docs/d/acm_certificate.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/acm_certificate.html.markdown |
| 16 | website/docs/d/acmpca_certificate.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/acmpca_certificate.html.markdown |
| 17 | website/docs/d/acmpca_certificate_authority.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/acmpca_certificate_authority.html.markdown |
| 18 | website/docs/d/agentregistry_registry.html.markdown | terraform-aws-docs | 2 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/agentregistry_registry.html.markdown |
| 19 | website/docs/d/ami.html.markdown | terraform-aws-docs | 3 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/ami.html.markdown |
| 20 | website/docs/d/ami_ids.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/ami_ids.html.markdown |
| 21 | website/docs/d/api_gateway_api_key.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/api_gateway_api_key.html.markdown |
| 22 | website/docs/d/api_gateway_api_keys.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/api_gateway_api_keys.html.markdown |
| 23 | website/docs/d/api_gateway_authorizer.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/api_gateway_authorizer.html.markdown |
| 24 | website/docs/d/api_gateway_authorizers.html.markdown | terraform-aws-docs |  | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/api_gateway_authorizers.html.markdown |
| 25 | website/docs/d/api_gateway_domain_name.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/api_gateway_domain_name.html.markdown |
| 26 | website/docs/d/api_gateway_export.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/api_gateway_export.html.markdown |
| 27 | website/docs/d/api_gateway_resource.html.markdown | terraform-aws-docs |  | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/api_gateway_resource.html.markdown |
| 28 | website/docs/d/api_gateway_rest_api.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/api_gateway_rest_api.html.markdown |
| 29 | website/docs/d/api_gateway_sdk.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/api_gateway_sdk.html.markdown |
| 30 | website/docs/d/api_gateway_vpc_link.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/api_gateway_vpc_link.html.markdown |
| 31 | website/docs/d/apigatewayv2_api.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/apigatewayv2_api.html.markdown |
| 32 | website/docs/d/apigatewayv2_apis.html.markdown | terraform-aws-docs |  | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/apigatewayv2_apis.html.markdown |
| 33 | website/docs/d/apigatewayv2_export.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/apigatewayv2_export.html.markdown |
| 34 | website/docs/d/apigatewayv2_vpc_link.html.markdown | terraform-aws-docs |  | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/apigatewayv2_vpc_link.html.markdown |
| 35 | website/docs/d/appconfig_application.html.markdown | terraform-aws-docs |  | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/appconfig_application.html.markdown |
| 36 | website/docs/d/appconfig_configuration_profile.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/appconfig_configuration_profile.html.markdown |
| 37 | website/docs/d/appconfig_configuration_profiles.html.markdown | terraform-aws-docs |  | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/appconfig_configuration_profiles.html.markdown |
| 38 | website/docs/d/appconfig_environment.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/appconfig_environment.html.markdown |
| 39 | website/docs/d/appconfig_environments.html.markdown | terraform-aws-docs |  | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/appconfig_environments.html.markdown |
| 40 | website/docs/d/appintegrations_event_integration.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/appintegrations_event_integration.html.markdown |
| 41 | website/docs/d/appmesh_gateway_route.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/appmesh_gateway_route.html.markdown |
| 42 | website/docs/d/appmesh_mesh.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/appmesh_mesh.html.markdown |
| 43 | website/docs/d/appmesh_route.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/appmesh_route.html.markdown |
| 44 | website/docs/d/appmesh_virtual_gateway.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/appmesh_virtual_gateway.html.markdown |
| 45 | website/docs/d/appmesh_virtual_node.html.markdown | terraform-aws-docs | 8 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/appmesh_virtual_node.html.markdown |
| 46 | website/docs/d/appmesh_virtual_router.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/appmesh_virtual_router.html.markdown |
| 47 | website/docs/d/appmesh_virtual_service.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/appmesh_virtual_service.html.markdown |
| 48 | website/docs/d/apprunner_hosted_zone_id.html.markdown | terraform-aws-docs |  | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/apprunner_hosted_zone_id.html.markdown |
| 49 | website/docs/d/appstream_image.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/appstream_image.html.markdown |
| 50 | website/docs/d/arcregionswitch_plan.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/arcregionswitch_plan.html.markdown |
| 51 | website/docs/d/arcregionswitch_route53_health_checks.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/arcregionswitch_route53_health_checks.html.markdown |
| 52 | website/docs/d/arn.html.markdown | terraform-aws-docs |  | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/arn.html.markdown |
| 53 | website/docs/d/athena_named_query.html.markdown | terraform-aws-docs |  | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/athena_named_query.html.markdown |
| 54 | website/docs/d/auditmanager_control.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/auditmanager_control.html.markdown |
| 55 | website/docs/d/auditmanager_framework.html.markdown | terraform-aws-docs |  | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/auditmanager_framework.html.markdown |
| 56 | website/docs/d/autoscaling_group.html.markdown | terraform-aws-docs | 3 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/autoscaling_group.html.markdown |
| 57 | website/docs/d/autoscaling_groups.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/autoscaling_groups.html.markdown |
| 58 | website/docs/d/availability_zone.html.markdown | terraform-aws-docs | 2 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/availability_zone.html.markdown |
| 59 | website/docs/d/availability_zones.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/availability_zones.html.markdown |
| 60 | website/docs/d/backup_framework.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/backup_framework.html.markdown |
| 61 | website/docs/d/backup_plan.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/backup_plan.html.markdown |
| 62 | website/docs/d/backup_report_plan.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/backup_report_plan.html.markdown |
| 63 | website/docs/d/backup_selection.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/backup_selection.html.markdown |
| 64 | website/docs/d/backup_vault.html.markdown | terraform-aws-docs |  | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/backup_vault.html.markdown |
| 65 | website/docs/d/batch_compute_environment.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/batch_compute_environment.html.markdown |
| 66 | website/docs/d/batch_job_definition.html.markdown | terraform-aws-docs | 6 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/batch_job_definition.html.markdown |
| 67 | website/docs/d/batch_job_queue.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/batch_job_queue.html.markdown |
| 68 | website/docs/d/batch_scheduling_policy.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/batch_scheduling_policy.html.markdown |
| 69 | website/docs/d/bedrock_custom_model.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/bedrock_custom_model.html.markdown |
| 70 | website/docs/d/bedrock_custom_models.html.markdown | terraform-aws-docs |  | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/bedrock_custom_models.html.markdown |
| 71 | website/docs/d/bedrock_foundation_model.html.markdown | terraform-aws-docs |  | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/bedrock_foundation_model.html.markdown |
| 72 | website/docs/d/bedrock_foundation_model_agreement_offers.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/bedrock_foundation_model_agreement_offers.html.markdown |
| 73 | website/docs/d/bedrock_foundation_models.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/bedrock_foundation_models.html.markdown |
| 74 | website/docs/d/bedrock_inference_profile.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/bedrock_inference_profile.html.markdown |
| 75 | website/docs/d/bedrock_inference_profiles.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/bedrock_inference_profiles.html.markdown |
| 76 | website/docs/d/bedrock_use_case_for_model_access.html.markdown | terraform-aws-docs |  | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/bedrock_use_case_for_model_access.html.markdown |
| 77 | website/docs/d/bedrockagent_agent_versions.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/bedrockagent_agent_versions.html.markdown |
| 78 | website/docs/d/billing_service_account.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/billing_service_account.html.markdown |
| 79 | website/docs/d/billing_views.html.markdown | terraform-aws-docs |  | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/billing_views.html.markdown |
| 80 | website/docs/d/budgets_budget.html.markdown | terraform-aws-docs | 2 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/budgets_budget.html.markdown |
| 81 | website/docs/d/caller_identity.html.markdown | terraform-aws-docs |  | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/caller_identity.html.markdown |
| 82 | website/docs/d/canonical_user_id.html.markdown | terraform-aws-docs |  | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/canonical_user_id.html.markdown |
| 83 | website/docs/d/ce_cost_category.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/ce_cost_category.html.markdown |
| 84 | website/docs/d/ce_tags.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/ce_tags.html.markdown |
| 85 | website/docs/d/chatbot_slack_workspace.html.markdown | terraform-aws-docs |  | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/chatbot_slack_workspace.html.markdown |
| 86 | website/docs/d/cloudcontrolapi_resource.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/cloudcontrolapi_resource.html.markdown |
| 87 | website/docs/d/cloudformation_export.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/cloudformation_export.html.markdown |
| 88 | website/docs/d/cloudformation_stack.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/cloudformation_stack.html.markdown |
| 89 | website/docs/d/cloudformation_type.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/cloudformation_type.html.markdown |
| 90 | website/docs/d/cloudfront_cache_policy.html.markdown | terraform-aws-docs | 2 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/cloudfront_cache_policy.html.markdown |
| 91 | website/docs/d/cloudfront_connection_group.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/cloudfront_connection_group.html.markdown |
| 92 | website/docs/d/cloudfront_distribution.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/cloudfront_distribution.html.markdown |
| 93 | website/docs/d/cloudfront_distribution_tenant.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/cloudfront_distribution_tenant.html.markdown |
| 94 | website/docs/d/cloudfront_function.html.markdown | terraform-aws-docs |  | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/cloudfront_function.html.markdown |
| 95 | website/docs/d/cloudfront_log_delivery_canonical_user_id.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/cloudfront_log_delivery_canonical_user_id.html.markdown |
| 96 | website/docs/d/cloudfront_origin_access_control.html.markdown | terraform-aws-docs |  | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/cloudfront_origin_access_control.html.markdown |
| 97 | website/docs/d/cloudfront_origin_access_identities.html.markdown | terraform-aws-docs |  | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/cloudfront_origin_access_identities.html.markdown |
| 98 | website/docs/d/cloudfront_origin_access_identity.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/cloudfront_origin_access_identity.html.markdown |
| 99 | website/docs/d/cloudfront_origin_request_policy.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/cloudfront_origin_request_policy.html.markdown |
| 100 | website/docs/d/cloudfront_realtime_log_config.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/cloudfront_realtime_log_config.html.markdown |
| 101 | website/docs/d/cloudfront_response_headers_policy.html.markdown | terraform-aws-docs | 3 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/cloudfront_response_headers_policy.html.markdown |
| 102 | website/docs/d/cloudhsm_v2_cluster.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/cloudhsm_v2_cluster.html.markdown |
| 103 | website/docs/d/cloudtrail_service_account.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/cloudtrail_service_account.html.markdown |
| 104 | website/docs/d/cloudwatch_contributor_managed_insight_rules.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/cloudwatch_contributor_managed_insight_rules.html.markdown |
| 105 | website/docs/d/cloudwatch_event_bus.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/cloudwatch_event_bus.html.markdown |
| 106 | website/docs/d/cloudwatch_event_buses.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/cloudwatch_event_buses.html.markdown |
| 107 | website/docs/d/cloudwatch_event_connection.html.markdown | terraform-aws-docs |  | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/cloudwatch_event_connection.html.markdown |
| 108 | website/docs/d/cloudwatch_event_source.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/cloudwatch_event_source.html.markdown |
| 109 | website/docs/d/cloudwatch_log_data_protection_policy_document.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/cloudwatch_log_data_protection_policy_document.html.markdown |
| 110 | website/docs/d/cloudwatch_log_group.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/cloudwatch_log_group.html.markdown |
| 111 | website/docs/d/cloudwatch_log_groups.html.markdown | terraform-aws-docs |  | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/cloudwatch_log_groups.html.markdown |
| 112 | website/docs/d/codeartifact_authorization_token.html.markdown | terraform-aws-docs |  | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/codeartifact_authorization_token.html.markdown |
| 113 | website/docs/d/codeartifact_repository_endpoint.html.markdown | terraform-aws-docs |  | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/codeartifact_repository_endpoint.html.markdown |
| 114 | website/docs/d/codebuild_fleet.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/codebuild_fleet.html.markdown |
| 115 | website/docs/d/codecatalyst_dev_environment.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/codecatalyst_dev_environment.html.markdown |
| 116 | website/docs/d/codecommit_approval_rule_template.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/codecommit_approval_rule_template.html.markdown |
| 117 | website/docs/d/codecommit_repository.html.markdown | terraform-aws-docs |  | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/codecommit_repository.html.markdown |
| 118 | website/docs/d/codeguruprofiler_profiling_group.html.markdown | terraform-aws-docs |  | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/codeguruprofiler_profiling_group.html.markdown |
| 119 | website/docs/d/codestarconnections_connection.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/codestarconnections_connection.html.markdown |
| 120 | website/docs/d/cognito_identity_pool.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/cognito_identity_pool.html.markdown |
| 121 | website/docs/d/cognito_user_group.html.markdown | terraform-aws-docs |  | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/cognito_user_group.html.markdown |
| 122 | website/docs/d/cognito_user_groups.html.markdown | terraform-aws-docs |  | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/cognito_user_groups.html.markdown |
| 123 | website/docs/d/cognito_user_pool.html.markdown | terraform-aws-docs | 2 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/cognito_user_pool.html.markdown |
| 124 | website/docs/d/cognito_user_pool_client.html.markdown | terraform-aws-docs | 2 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/cognito_user_pool_client.html.markdown |
| 125 | website/docs/d/cognito_user_pool_clients.html.markdown | terraform-aws-docs |  | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/cognito_user_pool_clients.html.markdown |
| 126 | website/docs/d/cognito_user_pool_signing_certificate.html.markdown | terraform-aws-docs |  | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/cognito_user_pool_signing_certificate.html.markdown |
| 127 | website/docs/d/cognito_user_pools.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/cognito_user_pools.html.markdown |
| 128 | website/docs/d/connect_bot_association.html.markdown | terraform-aws-docs |  | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/connect_bot_association.html.markdown |
| 129 | website/docs/d/connect_contact_flow.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/connect_contact_flow.html.markdown |
| 130 | website/docs/d/connect_contact_flow_module.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/connect_contact_flow_module.html.markdown |
| 131 | website/docs/d/connect_hours_of_operation.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/connect_hours_of_operation.html.markdown |
| 132 | website/docs/d/connect_instance.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/connect_instance.html.markdown |
| 133 | website/docs/d/connect_instance_storage_config.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/connect_instance_storage_config.html.markdown |
| 134 | website/docs/d/connect_lambda_function_association.html.markdown | terraform-aws-docs |  | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/connect_lambda_function_association.html.markdown |
| 135 | website/docs/d/connect_prompt.html.markdown | terraform-aws-docs |  | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/connect_prompt.html.markdown |
| 136 | website/docs/d/connect_queue.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/connect_queue.html.markdown |
| 137 | website/docs/d/connect_quick_connect.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/connect_quick_connect.html.markdown |
| 138 | website/docs/d/connect_routing_profile.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/connect_routing_profile.html.markdown |
| 139 | website/docs/d/connect_security_profile.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/connect_security_profile.html.markdown |
| 140 | website/docs/d/connect_user.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/connect_user.html.markdown |
| 141 | website/docs/d/connect_user_hierarchy_group.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/connect_user_hierarchy_group.html.markdown |
| 142 | website/docs/d/connect_user_hierarchy_structure.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/connect_user_hierarchy_structure.html.markdown |
| 143 | website/docs/d/connect_vocabulary.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/connect_vocabulary.html.markdown |
| 144 | website/docs/d/controltower_controls.html.markdown | terraform-aws-docs |  | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/controltower_controls.html.markdown |
| 145 | website/docs/d/cur_report_definition.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/cur_report_definition.html.markdown |
| 146 | website/docs/d/customer_gateway.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/customer_gateway.html.markdown |
| 147 | website/docs/d/datapipeline_pipeline.html.markdown | terraform-aws-docs |  | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/datapipeline_pipeline.html.markdown |
| 148 | website/docs/d/datapipeline_pipeline_definition.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/datapipeline_pipeline_definition.html.markdown |
| 149 | website/docs/d/datazone_domain.html.markdown | terraform-aws-docs |  | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/datazone_domain.html.markdown |
| 150 | website/docs/d/datazone_environment_blueprint.html.markdown | terraform-aws-docs |  | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/datazone_environment_blueprint.html.markdown |
| 151 | website/docs/d/db_cluster_snapshot.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/db_cluster_snapshot.html.markdown |
| 152 | website/docs/d/db_event_categories.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/db_event_categories.html.markdown |
| 153 | website/docs/d/db_instance.html.markdown | terraform-aws-docs | 2 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/db_instance.html.markdown |
| 154 | website/docs/d/db_instances.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/db_instances.html.markdown |
| 155 | website/docs/d/db_parameter_group.html.markdown | terraform-aws-docs |  | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/db_parameter_group.html.markdown |
| 156 | website/docs/d/db_proxy.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/db_proxy.html.markdown |
| 157 | website/docs/d/db_snapshot.html.markdown | terraform-aws-docs | 2 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/db_snapshot.html.markdown |
| 158 | website/docs/d/db_subnet_group.html.markdown | terraform-aws-docs |  | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/db_subnet_group.html.markdown |
| 159 | website/docs/d/default_tags.html.markdown | terraform-aws-docs |  | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/default_tags.html.markdown |
| 160 | website/docs/d/devopsguru_notification_channel.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/devopsguru_notification_channel.html.markdown |
| 161 | website/docs/d/devopsguru_resource_collection.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/devopsguru_resource_collection.html.markdown |
| 162 | website/docs/d/directory_service_directory.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/directory_service_directory.html.markdown |
| 163 | website/docs/d/dms_certificate.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/dms_certificate.html.markdown |
| 164 | website/docs/d/dms_endpoint.html.markdown | terraform-aws-docs |  | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/dms_endpoint.html.markdown |
| 165 | website/docs/d/dms_replication_instance.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/dms_replication_instance.html.markdown |
| 166 | website/docs/d/dms_replication_subnet_group.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/dms_replication_subnet_group.html.markdown |
| 167 | website/docs/d/dms_replication_task.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/dms_replication_task.html.markdown |
| 168 | website/docs/d/docdb_engine_version.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/docdb_engine_version.html.markdown |
| 169 | website/docs/d/docdb_orderable_db_instance.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/docdb_orderable_db_instance.html.markdown |
| 170 | website/docs/d/dx_connection.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/dx_connection.html.markdown |
| 171 | website/docs/d/dx_gateway.html.markdown | terraform-aws-docs |  | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/dx_gateway.html.markdown |
| 172 | website/docs/d/dx_location.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/dx_location.html.markdown |
| 173 | website/docs/d/dx_locations.html.markdown | terraform-aws-docs |  | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/dx_locations.html.markdown |
| 174 | website/docs/d/dx_router_configuration.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/dx_router_configuration.html.markdown |
| 175 | website/docs/d/dynamodb_backups.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/dynamodb_backups.html.markdown |
| 176 | website/docs/d/dynamodb_table.html.markdown | terraform-aws-docs |  | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/dynamodb_table.html.markdown |
| 177 | website/docs/d/dynamodb_table_item.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/dynamodb_table_item.html.markdown |
| 178 | website/docs/d/dynamodb_tables.html.markdown | terraform-aws-docs |  | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/dynamodb_tables.html.markdown |
| 179 | website/docs/d/ebs_default_kms_key.html.markdown | terraform-aws-docs |  | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/ebs_default_kms_key.html.markdown |
| 180 | website/docs/d/ebs_encryption_by_default.html.markdown | terraform-aws-docs |  | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/ebs_encryption_by_default.html.markdown |
| 181 | website/docs/d/ebs_snapshot.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/ebs_snapshot.html.markdown |
| 182 | website/docs/d/ebs_snapshot_ids.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/ebs_snapshot_ids.html.markdown |
| 183 | website/docs/d/ebs_volume.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/ebs_volume.html.markdown |
| 184 | website/docs/d/ebs_volumes.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/ebs_volumes.html.markdown |
| 185 | website/docs/d/ec2_capacity_block_offering.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/ec2_capacity_block_offering.html.markdown |
| 186 | website/docs/d/ec2_capacity_block_reservation.html.markdown | terraform-aws-docs | 2 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/ec2_capacity_block_reservation.html.markdown |
| 187 | website/docs/d/ec2_client_vpn_endpoint.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/ec2_client_vpn_endpoint.html.markdown |
| 188 | website/docs/d/ec2_coip_pool.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/ec2_coip_pool.html.markdown |
| 189 | website/docs/d/ec2_coip_pools.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/ec2_coip_pools.html.markdown |
| 190 | website/docs/d/ec2_host.html.markdown | terraform-aws-docs | 2 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/ec2_host.html.markdown |
| 191 | website/docs/d/ec2_hosts.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/ec2_hosts.html.markdown |
| 192 | website/docs/d/ec2_instance_type.html.markdown | terraform-aws-docs | 3 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/ec2_instance_type.html.markdown |
| 193 | website/docs/d/ec2_instance_type_offering.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/ec2_instance_type_offering.html.markdown |
| 194 | website/docs/d/ec2_instance_type_offerings.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/ec2_instance_type_offerings.html.markdown |
| 195 | website/docs/d/ec2_instance_types.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/ec2_instance_types.html.markdown |
| 196 | website/docs/d/ec2_local_gateway.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/ec2_local_gateway.html.markdown |
| 197 | website/docs/d/ec2_local_gateway_route_table.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/ec2_local_gateway_route_table.html.markdown |
| 198 | website/docs/d/ec2_local_gateway_route_tables.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/ec2_local_gateway_route_tables.html.markdown |
| 199 | website/docs/d/ec2_local_gateway_virtual_interface.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/ec2_local_gateway_virtual_interface.html.markdown |
| 200 | website/docs/d/ec2_local_gateway_virtual_interface_group.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/d/ec2_local_gateway_virtual_interface_group.html.markdown |
<!-- generated:end -->

## Known gaps

- (what is still missing from the start target, and why)
