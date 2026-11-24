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
## Sources (generated 2026-11-24 09:53 UTC by scripts/dataset_report.py)

| Source | Licence / terms | Files | MB | Pages* | How | Fetched | Example URL |
|---|---|---|---|---|---|---|---|
| hashicorp | MPL-2.0 | 10 | 5.1 | 72 | http | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/main/website/docs/r/s3_bucket.html.markdown |
| terraform-aws-docs | Provider docs are MPL-2.0 in the repository. | 1765 | 10.5 | 3,420 | git @ 7bbc662b89 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/accessanalyzer_analyzer.html.markdown |

**Total:** 1,775 files, 15.5 MB, 3,491 pages. Not downloaded: 0 blocked by robots.txt, 0 failed.

*Pages = PDF pages, plus one page per 3,000 characters of text or HTML.

## Files (first 200 of 1,775)

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
| 11 | website/docs/r/accessanalyzer_analyzer.html.markdown | terraform-aws-docs | 3 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/accessanalyzer_analyzer.html.markdown |
| 12 | website/docs/r/accessanalyzer_archive_rule.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/accessanalyzer_archive_rule.html.markdown |
| 13 | website/docs/r/account_alternate_contact.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/account_alternate_contact.html.markdown |
| 14 | website/docs/r/account_primary_contact.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/account_primary_contact.html.markdown |
| 15 | website/docs/r/account_region.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/account_region.html.markdown |
| 16 | website/docs/r/accountaccess_application.html.markdown | terraform-aws-docs | 2 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/accountaccess_application.html.markdown |
| 17 | website/docs/r/accountaccess_entitlement.html.markdown | terraform-aws-docs | 2 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/accountaccess_entitlement.html.markdown |
| 18 | website/docs/r/acm_certificate.html.markdown | terraform-aws-docs | 4 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/acm_certificate.html.markdown |
| 19 | website/docs/r/acm_certificate_validation.html.markdown | terraform-aws-docs | 2 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/acm_certificate_validation.html.markdown |
| 20 | website/docs/r/acmpca_certificate.html.markdown | terraform-aws-docs | 2 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/acmpca_certificate.html.markdown |
| 21 | website/docs/r/acmpca_certificate_authority.html.markdown | terraform-aws-docs | 4 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/acmpca_certificate_authority.html.markdown |
| 22 | website/docs/r/acmpca_certificate_authority_certificate.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/acmpca_certificate_authority_certificate.html.markdown |
| 23 | website/docs/r/acmpca_permission.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/acmpca_permission.html.markdown |
| 24 | website/docs/r/acmpca_policy.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/acmpca_policy.html.markdown |
| 25 | website/docs/r/agentregistry_registry.html.markdown | terraform-aws-docs | 4 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/agentregistry_registry.html.markdown |
| 26 | website/docs/r/ami.html.markdown | terraform-aws-docs | 3 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/ami.html.markdown |
| 27 | website/docs/r/ami_copy.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/ami_copy.html.markdown |
| 28 | website/docs/r/ami_from_instance.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/ami_from_instance.html.markdown |
| 29 | website/docs/r/ami_launch_permission.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/ami_launch_permission.html.markdown |
| 30 | website/docs/r/amplify_app.html.markdown | terraform-aws-docs | 4 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/amplify_app.html.markdown |
| 31 | website/docs/r/amplify_backend_environment.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/amplify_backend_environment.html.markdown |
| 32 | website/docs/r/amplify_branch.html.markdown | terraform-aws-docs | 2 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/amplify_branch.html.markdown |
| 33 | website/docs/r/amplify_domain_association.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/amplify_domain_association.html.markdown |
| 34 | website/docs/r/amplify_webhook.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/amplify_webhook.html.markdown |
| 35 | website/docs/r/api_gateway_account.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/api_gateway_account.html.markdown |
| 36 | website/docs/r/api_gateway_api_key.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/api_gateway_api_key.html.markdown |
| 37 | website/docs/r/api_gateway_authorizer.html.markdown | terraform-aws-docs | 2 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/api_gateway_authorizer.html.markdown |
| 38 | website/docs/r/api_gateway_base_path_mapping.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/api_gateway_base_path_mapping.html.markdown |
| 39 | website/docs/r/api_gateway_client_certificate.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/api_gateway_client_certificate.html.markdown |
| 40 | website/docs/r/api_gateway_deployment.html.markdown | terraform-aws-docs | 3 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/api_gateway_deployment.html.markdown |
| 41 | website/docs/r/api_gateway_documentation_part.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/api_gateway_documentation_part.html.markdown |
| 42 | website/docs/r/api_gateway_documentation_version.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/api_gateway_documentation_version.html.markdown |
| 43 | website/docs/r/api_gateway_domain_name.html.markdown | terraform-aws-docs | 5 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/api_gateway_domain_name.html.markdown |
| 44 | website/docs/r/api_gateway_domain_name_access_association.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/api_gateway_domain_name_access_association.html.markdown |
| 45 | website/docs/r/api_gateway_gateway_response.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/api_gateway_gateway_response.html.markdown |
| 46 | website/docs/r/api_gateway_integration.html.markdown | terraform-aws-docs | 6 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/api_gateway_integration.html.markdown |
| 47 | website/docs/r/api_gateway_integration_response.html.markdown | terraform-aws-docs | 2 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/api_gateway_integration_response.html.markdown |
| 48 | website/docs/r/api_gateway_method.html.markdown | terraform-aws-docs | 2 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/api_gateway_method.html.markdown |
| 49 | website/docs/r/api_gateway_method_response.html.markdown | terraform-aws-docs | 2 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/api_gateway_method_response.html.markdown |
| 50 | website/docs/r/api_gateway_method_settings.html.markdown | terraform-aws-docs | 2 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/api_gateway_method_settings.html.markdown |
| 51 | website/docs/r/api_gateway_model.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/api_gateway_model.html.markdown |
| 52 | website/docs/r/api_gateway_request_validator.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/api_gateway_request_validator.html.markdown |
| 53 | website/docs/r/api_gateway_resource.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/api_gateway_resource.html.markdown |
| 54 | website/docs/r/api_gateway_rest_api.html.markdown | terraform-aws-docs | 6 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/api_gateway_rest_api.html.markdown |
| 55 | website/docs/r/api_gateway_rest_api_policy.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/api_gateway_rest_api_policy.html.markdown |
| 56 | website/docs/r/api_gateway_rest_api_put.html.markdown | terraform-aws-docs | 2 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/api_gateway_rest_api_put.html.markdown |
| 57 | website/docs/r/api_gateway_stage.html.markdown | terraform-aws-docs | 3 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/api_gateway_stage.html.markdown |
| 58 | website/docs/r/api_gateway_usage_plan.html.markdown | terraform-aws-docs | 2 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/api_gateway_usage_plan.html.markdown |
| 59 | website/docs/r/api_gateway_usage_plan_key.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/api_gateway_usage_plan_key.html.markdown |
| 60 | website/docs/r/api_gateway_vpc_link.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/api_gateway_vpc_link.html.markdown |
| 61 | website/docs/r/apigatewayv2_api.html.markdown | terraform-aws-docs | 3 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/apigatewayv2_api.html.markdown |
| 62 | website/docs/r/apigatewayv2_api_mapping.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/apigatewayv2_api_mapping.html.markdown |
| 63 | website/docs/r/apigatewayv2_authorizer.html.markdown | terraform-aws-docs | 2 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/apigatewayv2_authorizer.html.markdown |
| 64 | website/docs/r/apigatewayv2_deployment.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/apigatewayv2_deployment.html.markdown |
| 65 | website/docs/r/apigatewayv2_domain_name.html.markdown | terraform-aws-docs | 2 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/apigatewayv2_domain_name.html.markdown |
| 66 | website/docs/r/apigatewayv2_integration.html.markdown | terraform-aws-docs | 3 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/apigatewayv2_integration.html.markdown |
| 67 | website/docs/r/apigatewayv2_integration_response.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/apigatewayv2_integration_response.html.markdown |
| 68 | website/docs/r/apigatewayv2_model.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/apigatewayv2_model.html.markdown |
| 69 | website/docs/r/apigatewayv2_route.html.markdown | terraform-aws-docs | 3 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/apigatewayv2_route.html.markdown |
| 70 | website/docs/r/apigatewayv2_route_response.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/apigatewayv2_route_response.html.markdown |
| 71 | website/docs/r/apigatewayv2_routing_rule.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/apigatewayv2_routing_rule.html.markdown |
| 72 | website/docs/r/apigatewayv2_stage.html.markdown | terraform-aws-docs | 2 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/apigatewayv2_stage.html.markdown |
| 73 | website/docs/r/apigatewayv2_vpc_link.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/apigatewayv2_vpc_link.html.markdown |
| 74 | website/docs/r/app_cookie_stickiness_policy.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/app_cookie_stickiness_policy.html.markdown |
| 75 | website/docs/r/appautoscaling_policy.html.markdown | terraform-aws-docs | 11 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/appautoscaling_policy.html.markdown |
| 76 | website/docs/r/appautoscaling_scheduled_action.html.markdown | terraform-aws-docs | 2 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/appautoscaling_scheduled_action.html.markdown |
| 77 | website/docs/r/appautoscaling_target.html.markdown | terraform-aws-docs | 3 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/appautoscaling_target.html.markdown |
| 78 | website/docs/r/appconfig_application.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/appconfig_application.html.markdown |
| 79 | website/docs/r/appconfig_configuration_profile.html.markdown | terraform-aws-docs | 2 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/appconfig_configuration_profile.html.markdown |
| 80 | website/docs/r/appconfig_deployment.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/appconfig_deployment.html.markdown |
| 81 | website/docs/r/appconfig_deployment_strategy.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/appconfig_deployment_strategy.html.markdown |
| 82 | website/docs/r/appconfig_environment.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/appconfig_environment.html.markdown |
| 83 | website/docs/r/appconfig_extension.html.markdown | terraform-aws-docs | 2 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/appconfig_extension.html.markdown |
| 84 | website/docs/r/appconfig_extension_association.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/appconfig_extension_association.html.markdown |
| 85 | website/docs/r/appconfig_hosted_configuration_version.html.markdown | terraform-aws-docs | 2 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/appconfig_hosted_configuration_version.html.markdown |
| 86 | website/docs/r/appfabric_app_authorization.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/appfabric_app_authorization.html.markdown |
| 87 | website/docs/r/appfabric_app_authorization_connection.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/appfabric_app_authorization_connection.html.markdown |
| 88 | website/docs/r/appfabric_app_bundle.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/appfabric_app_bundle.html.markdown |
| 89 | website/docs/r/appfabric_ingestion.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/appfabric_ingestion.html.markdown |
| 90 | website/docs/r/appfabric_ingestion_destination.html.markdown | terraform-aws-docs | 2 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/appfabric_ingestion_destination.html.markdown |
| 91 | website/docs/r/appflow_connector_profile.html.markdown | terraform-aws-docs | 11 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/appflow_connector_profile.html.markdown |
| 92 | website/docs/r/appflow_flow.html.markdown | terraform-aws-docs | 14 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/appflow_flow.html.markdown |
| 93 | website/docs/r/appintegrations_data_integration.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/appintegrations_data_integration.html.markdown |
| 94 | website/docs/r/appintegrations_event_integration.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/appintegrations_event_integration.html.markdown |
| 95 | website/docs/r/applicationinsights_application.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/applicationinsights_application.html.markdown |
| 96 | website/docs/r/appmesh_gateway_route.html.markdown | terraform-aws-docs | 5 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/appmesh_gateway_route.html.markdown |
| 97 | website/docs/r/appmesh_mesh.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/appmesh_mesh.html.markdown |
| 98 | website/docs/r/appmesh_route.html.markdown | terraform-aws-docs | 8 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/appmesh_route.html.markdown |
| 99 | website/docs/r/appmesh_virtual_gateway.html.markdown | terraform-aws-docs | 4 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/appmesh_virtual_gateway.html.markdown |
| 100 | website/docs/r/appmesh_virtual_node.html.markdown | terraform-aws-docs | 10 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/appmesh_virtual_node.html.markdown |
| 101 | website/docs/r/appmesh_virtual_router.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/appmesh_virtual_router.html.markdown |
| 102 | website/docs/r/appmesh_virtual_service.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/appmesh_virtual_service.html.markdown |
| 103 | website/docs/r/apprunner_auto_scaling_configuration_version.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/apprunner_auto_scaling_configuration_version.html.markdown |
| 104 | website/docs/r/apprunner_connection.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/apprunner_connection.html.markdown |
| 105 | website/docs/r/apprunner_custom_domain_association.html.markdown | terraform-aws-docs | 2 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/apprunner_custom_domain_association.html.markdown |
| 106 | website/docs/r/apprunner_default_auto_scaling_configuration_version.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/apprunner_default_auto_scaling_configuration_version.html.markdown |
| 107 | website/docs/r/apprunner_deployment.html.markdown | terraform-aws-docs |  | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/apprunner_deployment.html.markdown |
| 108 | website/docs/r/apprunner_observability_configuration.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/apprunner_observability_configuration.html.markdown |
| 109 | website/docs/r/apprunner_service.html.markdown | terraform-aws-docs | 6 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/apprunner_service.html.markdown |
| 110 | website/docs/r/apprunner_vpc_connector.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/apprunner_vpc_connector.html.markdown |
| 111 | website/docs/r/apprunner_vpc_ingress_connection.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/apprunner_vpc_ingress_connection.html.markdown |
| 112 | website/docs/r/appstream_directory_config.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/appstream_directory_config.html.markdown |
| 113 | website/docs/r/appstream_fleet.html.markdown | terraform-aws-docs | 2 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/appstream_fleet.html.markdown |
| 114 | website/docs/r/appstream_fleet_stack_association.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/appstream_fleet_stack_association.html.markdown |
| 115 | website/docs/r/appstream_image_builder.html.markdown | terraform-aws-docs | 2 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/appstream_image_builder.html.markdown |
| 116 | website/docs/r/appstream_stack.html.markdown | terraform-aws-docs | 2 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/appstream_stack.html.markdown |
| 117 | website/docs/r/appstream_user.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/appstream_user.html.markdown |
| 118 | website/docs/r/appstream_user_stack_association.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/appstream_user_stack_association.html.markdown |
| 119 | website/docs/r/appsync_api.html.markdown | terraform-aws-docs | 3 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/appsync_api.html.markdown |
| 120 | website/docs/r/appsync_api_cache.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/appsync_api_cache.html.markdown |
| 121 | website/docs/r/appsync_api_key.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/appsync_api_key.html.markdown |
| 122 | website/docs/r/appsync_channel_namespace.html.markdown | terraform-aws-docs | 2 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/appsync_channel_namespace.html.markdown |
| 123 | website/docs/r/appsync_datasource.html.markdown | terraform-aws-docs | 3 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/appsync_datasource.html.markdown |
| 124 | website/docs/r/appsync_domain_name.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/appsync_domain_name.html.markdown |
| 125 | website/docs/r/appsync_domain_name_api_association.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/appsync_domain_name_api_association.html.markdown |
| 126 | website/docs/r/appsync_function.html.markdown | terraform-aws-docs | 2 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/appsync_function.html.markdown |
| 127 | website/docs/r/appsync_graphql_api.html.markdown | terraform-aws-docs | 5 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/appsync_graphql_api.html.markdown |
| 128 | website/docs/r/appsync_resolver.html.markdown | terraform-aws-docs | 2 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/appsync_resolver.html.markdown |
| 129 | website/docs/r/appsync_source_api_association.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/appsync_source_api_association.html.markdown |
| 130 | website/docs/r/appsync_type.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/appsync_type.html.markdown |
| 131 | website/docs/r/arcregionswitch_plan.html.markdown | terraform-aws-docs | 11 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/arcregionswitch_plan.html.markdown |
| 132 | website/docs/r/arczonalshift_autoshift_observer_notification_status.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/arczonalshift_autoshift_observer_notification_status.html.markdown |
| 133 | website/docs/r/arczonalshift_zonal_autoshift_configuration.html.markdown | terraform-aws-docs | 2 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/arczonalshift_zonal_autoshift_configuration.html.markdown |
| 134 | website/docs/r/athena_capacity_reservation.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/athena_capacity_reservation.html.markdown |
| 135 | website/docs/r/athena_data_catalog.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/athena_data_catalog.html.markdown |
| 136 | website/docs/r/athena_database.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/athena_database.html.markdown |
| 137 | website/docs/r/athena_named_query.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/athena_named_query.html.markdown |
| 138 | website/docs/r/athena_prepared_statement.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/athena_prepared_statement.html.markdown |
| 139 | website/docs/r/athena_workgroup.html.markdown | terraform-aws-docs | 4 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/athena_workgroup.html.markdown |
| 140 | website/docs/r/auditmanager_account_registration.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/auditmanager_account_registration.html.markdown |
| 141 | website/docs/r/auditmanager_assessment.html.markdown | terraform-aws-docs | 2 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/auditmanager_assessment.html.markdown |
| 142 | website/docs/r/auditmanager_assessment_delegation.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/auditmanager_assessment_delegation.html.markdown |
| 143 | website/docs/r/auditmanager_assessment_report.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/auditmanager_assessment_report.html.markdown |
| 144 | website/docs/r/auditmanager_control.html.markdown | terraform-aws-docs | 2 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/auditmanager_control.html.markdown |
| 145 | website/docs/r/auditmanager_framework.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/auditmanager_framework.html.markdown |
| 146 | website/docs/r/auditmanager_framework_share.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/auditmanager_framework_share.html.markdown |
| 147 | website/docs/r/auditmanager_organization_admin_account_registration.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/auditmanager_organization_admin_account_registration.html.markdown |
| 148 | website/docs/r/autoscaling_attachment.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/autoscaling_attachment.html.markdown |
| 149 | website/docs/r/autoscaling_group.html.markdown | terraform-aws-docs | 16 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/autoscaling_group.html.markdown |
| 150 | website/docs/r/autoscaling_group_tag.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/autoscaling_group_tag.html.markdown |
| 151 | website/docs/r/autoscaling_lifecycle_hook.html.markdown | terraform-aws-docs | 2 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/autoscaling_lifecycle_hook.html.markdown |
| 152 | website/docs/r/autoscaling_notification.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/autoscaling_notification.html.markdown |
| 153 | website/docs/r/autoscaling_policy.html.markdown | terraform-aws-docs | 7 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/autoscaling_policy.html.markdown |
| 154 | website/docs/r/autoscaling_schedule.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/autoscaling_schedule.html.markdown |
| 155 | website/docs/r/autoscaling_traffic_source_attachment.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/autoscaling_traffic_source_attachment.html.markdown |
| 156 | website/docs/r/autoscalingplans_scaling_plan.html.markdown | terraform-aws-docs | 4 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/autoscalingplans_scaling_plan.html.markdown |
| 157 | website/docs/r/backup_framework.html.markdown | terraform-aws-docs | 2 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/backup_framework.html.markdown |
| 158 | website/docs/r/backup_global_settings.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/backup_global_settings.html.markdown |
| 159 | website/docs/r/backup_logically_air_gapped_vault.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/backup_logically_air_gapped_vault.html.markdown |
| 160 | website/docs/r/backup_plan.html.markdown | terraform-aws-docs | 2 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/backup_plan.html.markdown |
| 161 | website/docs/r/backup_region_settings.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/backup_region_settings.html.markdown |
| 162 | website/docs/r/backup_report_plan.html.markdown | terraform-aws-docs | 2 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/backup_report_plan.html.markdown |
| 163 | website/docs/r/backup_restore_testing_plan.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/backup_restore_testing_plan.html.markdown |
| 164 | website/docs/r/backup_restore_testing_selection.html.markdown | terraform-aws-docs | 2 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/backup_restore_testing_selection.html.markdown |
| 165 | website/docs/r/backup_selection.html.markdown | terraform-aws-docs | 3 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/backup_selection.html.markdown |
| 166 | website/docs/r/backup_vault.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/backup_vault.html.markdown |
| 167 | website/docs/r/backup_vault_lock_configuration.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/backup_vault_lock_configuration.html.markdown |
| 168 | website/docs/r/backup_vault_notifications.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/backup_vault_notifications.html.markdown |
| 169 | website/docs/r/backup_vault_policy.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/backup_vault_policy.html.markdown |
| 170 | website/docs/r/batch_compute_environment.html.markdown | terraform-aws-docs | 5 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/batch_compute_environment.html.markdown |
| 171 | website/docs/r/batch_job_definition.html.markdown | terraform-aws-docs | 7 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/batch_job_definition.html.markdown |
| 172 | website/docs/r/batch_job_queue.html.markdown | terraform-aws-docs | 2 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/batch_job_queue.html.markdown |
| 173 | website/docs/r/batch_scheduling_policy.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/batch_scheduling_policy.html.markdown |
| 174 | website/docs/r/bcmdataexports_export.html.markdown | terraform-aws-docs | 2 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/bcmdataexports_export.html.markdown |
| 175 | website/docs/r/bedrock_custom_model.html.markdown | terraform-aws-docs | 2 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/bedrock_custom_model.html.markdown |
| 176 | website/docs/r/bedrock_enforced_guardrail_configuration.html.markdown | terraform-aws-docs | 2 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/bedrock_enforced_guardrail_configuration.html.markdown |
| 177 | website/docs/r/bedrock_evaluation_job.html.markdown | terraform-aws-docs | 6 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/bedrock_evaluation_job.html.markdown |
| 178 | website/docs/r/bedrock_foundation_model_agreement.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/bedrock_foundation_model_agreement.html.markdown |
| 179 | website/docs/r/bedrock_guardrail.html.markdown | terraform-aws-docs | 4 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/bedrock_guardrail.html.markdown |
| 180 | website/docs/r/bedrock_guardrail_resource_policy.html.markdown | terraform-aws-docs | 2 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/bedrock_guardrail_resource_policy.html.markdown |
| 181 | website/docs/r/bedrock_guardrail_version.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/bedrock_guardrail_version.html.markdown |
| 182 | website/docs/r/bedrock_inference_profile.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/bedrock_inference_profile.html.markdown |
| 183 | website/docs/r/bedrock_model_invocation_job.html.markdown | terraform-aws-docs | 2 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/bedrock_model_invocation_job.html.markdown |
| 184 | website/docs/r/bedrock_model_invocation_logging_configuration.html.markdown | terraform-aws-docs | 2 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/bedrock_model_invocation_logging_configuration.html.markdown |
| 185 | website/docs/r/bedrock_provisioned_model_throughput.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/bedrock_provisioned_model_throughput.html.markdown |
| 186 | website/docs/r/bedrock_use_case_for_model_access.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/bedrock_use_case_for_model_access.html.markdown |
| 187 | website/docs/r/bedrockagent_agent.html.markdown | terraform-aws-docs | 4 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/bedrockagent_agent.html.markdown |
| 188 | website/docs/r/bedrockagent_agent_action_group.html.markdown | terraform-aws-docs | 3 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/bedrockagent_agent_action_group.html.markdown |
| 189 | website/docs/r/bedrockagent_agent_alias.html.markdown | terraform-aws-docs | 2 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/bedrockagent_agent_alias.html.markdown |
| 190 | website/docs/r/bedrockagent_agent_collaborator.html.markdown | terraform-aws-docs | 2 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/bedrockagent_agent_collaborator.html.markdown |
| 191 | website/docs/r/bedrockagent_agent_knowledge_base_association.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/bedrockagent_agent_knowledge_base_association.html.markdown |
| 192 | website/docs/r/bedrockagent_data_source.html.markdown | terraform-aws-docs | 13 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/bedrockagent_data_source.html.markdown |
| 193 | website/docs/r/bedrockagent_flow.html.markdown | terraform-aws-docs | 12 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/bedrockagent_flow.html.markdown |
| 194 | website/docs/r/bedrockagent_knowledge_base.html.markdown | terraform-aws-docs | 12 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/bedrockagent_knowledge_base.html.markdown |
| 195 | website/docs/r/bedrockagent_prompt.html.markdown | terraform-aws-docs | 3 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/bedrockagent_prompt.html.markdown |
| 196 | website/docs/r/bedrockagentcore_agent_runtime.html.markdown | terraform-aws-docs | 6 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/bedrockagentcore_agent_runtime.html.markdown |
| 197 | website/docs/r/bedrockagentcore_agent_runtime_endpoint.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/bedrockagentcore_agent_runtime_endpoint.html.markdown |
| 198 | website/docs/r/bedrockagentcore_api_key_credential_provider.html.markdown | terraform-aws-docs | 2 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/bedrockagentcore_api_key_credential_provider.html.markdown |
| 199 | website/docs/r/bedrockagentcore_browser.html.markdown | terraform-aws-docs | 2 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/bedrockagentcore_browser.html.markdown |
| 200 | website/docs/r/bedrockagentcore_browser_profile.html.markdown | terraform-aws-docs | 1 | 2026-11-24 | https://github.com/hashicorp/terraform-provider-aws/blob/HEAD/website/docs/r/bedrockagentcore_browser_profile.html.markdown |
<!-- generated:end -->

## Known gaps

- (what is still missing from the start target, and why)
