schema = [
    {
        "schema_name": {
            "S": "wave"
        },
        "schema_type": {
            "S": "user"
        },
        "attributes": {
            "L": [
                    {
                     "M": {
                       "description": {
                         "S": "Wave Id"
                       },
                       "hidden": {
                         "BOOL": True
                       },
                       "name": {
                         "S": "wave_id"
                       },
                       "required": {
                         "BOOL": True
                       },
                       "system": {
                         "BOOL": True
                       },
                       "type": {
                         "S": "string"
                       }
                     }
                    },
                    {
                    "M": {
                        "description": {
                            "S": "Wave Name"
                        },
                        "name": {
                            "S": "wave_name"
                        },
                        "type": {
                            "S": "string"
                        },
                        "validation_regex": {
                            "S": "^(?!\\s*$).+"
                        },
                        "group_order": {
                            "S": "-1000"
                        },
                        "validation_regex_msg": {
                            "S": "Wave name must be specified."
                        },
                        "required": {
                            "BOOL": True
                         },
                        "system": {
                            "BOOL": True
                        }
                    }
                },
                {
                    "M": {
                        "description": {
                            "S": "Wave Status"
                        },
                        "name": {
                            "S": "wave_status"
                        },
                        "listvalue": {
                            "S": "Not started,Planning,In progress,Completed,Blocked"
                        },
                        "type": {
                            "S": "list"
                        },
						"group_order": {
							"S": "-999"
						},
                    }
                },
                {
                    "M": {
                        "description": {
                            "S": "Wave Start Time"
                        },
                        "name": {
                            "S": "wave_start_time"
                        },
                        "type": {
                            "S": "date"
                        }
                    }
                },
                {
                    "M": {
                        "description": {
                            "S": "Wave End Time"
                        },
                        "name": {
                            "S": "wave_end_time"
                        },
                        "type": {
                            "S": "date"
                        }
                    }
                }

            ]
        }
    },

    {
        "schema_name": {
            "S": "app"
        },
        "schema_type": {
            "S": "user"
        },
        "attributes": {
            "L": [
                {
                    "M": {
                      "description": {
                        "S": "Application Id"
                      },
                      "hidden": {
                        "BOOL": True
                      },
                      "name": {
                        "S": "app_id"
                      },
                      "required": {
                        "BOOL": True
                      },
                      "system": {
                        "BOOL": True
                      },
                      "type": {
                        "S": "string"
                      }
                    }
                 },
                {
                    "M": {
                        "description": {
                            "S": "Application Name"
                        },
                        "name": {
                            "S": "app_name"
                        },
                        "type": {
                            "S": "string"
                        },
                        "validation_regex": {
                            "S": "^(?!\\s*$).+"
                        },
                        "validation_regex_msg": {
                            "S": "Application name must be specified."
                        },
                        "group_order": {
                            "S": "-1000"
                        },
                        "required": {
                            "BOOL": True
                         },
                        "system": {
                            "BOOL": True
                        }
                    }
                },
                {
                    "M": {
                        "description": {
                            "S": "Wave Id"
                        },
                        "name": {
                            "S": "wave_id"
                        },
                        "type": {
                            "S": "relationship"
                        },
                        "group_order": {
                            "S": "-999"
                        },
                        "required": {
                            "BOOL": False
                        },
                        "system": {
                            "BOOL": True
                        },
                        "rel_display_attribute": {
                            "S": "wave_name"
                        },
                        "rel_entity": {
                            "S": "wave"
                        },
                        "rel_key": {
                            "S": "wave_id"
                        }
                    }
                },
                {
                    "M": {
                        "description": {
                            "S": "CloudEndure Project Name"
                        },
                        "listvalue": {
                            "S": "project1,project2"
                        },
                        "name": {
                            "S": "cloudendure_projectname"
                        },
                        "type": {
                            "S": "list"
                        },
                        "system": {
                            "BOOL": True
                        },
                        "group": {
                          "S": "Target"
                        }
                    }
                },
                {
                    "M": {
                        "description": {
                            "S": "AWS Account Id"
                        },
                        "listvalue": {
                            "S": "111122223333,222233334444"
                        },
                        "name": {
                            "S": "aws_accountid"
                        },
                        "type": {
                            "S": "list"
                        },
                        "validation_regex": {
                            "S": "^\\d{12}$"
                        },
                        "validation_regex_msg": {
                            "S": "Invalid AWS account Id."
                        },
                        "required": {
                            "BOOL": True
                        },
                        "system": {
                            "BOOL": True
                        },
                        "group": {
                            "S": "Target"
                        }
                    }
                },
                {
                    "M": {
                        "description": {
                            "S": "AWS Region"
                        },
                        "name": {
                            "S": "aws_region"
                        },
                        "type": {
                            "S": "list"
                        },
                        "listvalue": {
                            "S": "us-east-2,us-east-1,us-west-1,us-west-2,af-south-1,ap-east-1,ap-southeast-3,ap-south-1,ap-northeast-3,ap-northeast-2,ap-southeast-1,ap-southeast-2,ap-northeast-1,ca-central-1,cn-north-1,cn-northwest-1,eu-central-1,eu-west-1,eu-west-2,eu-south-1,eu-west-3,eu-north-1,me-south-1,sa-east-1"
                        },
                        "required": {
                          "BOOL": True
                        },
                        "system": {
                            "BOOL": True
                        },
                        "group": {
                            "S": "Target"
                        }
                    }
                }

            ]
        }
    },
    {
        "schema_name": {
            "S": "server"
        },
        "schema_type": {
            "S": "user"
        },
        "attributes": {
            "L": [
               {
                     "M": {
                       "description": {
                         "S": "Server Id"
                       },
                       "hidden": {
                         "BOOL": True
                       },
                       "name": {
                         "S": "server_id"
                       },
                       "required": {
                         "BOOL": True
                       },
                       "system": {
                         "BOOL": True
                       },
                       "type": {
                         "S": "string"
                       }
                     }
                },
                {
                    "M": {
                        "description": {
                            "S": "Application"
                        },
                        "name": {
                            "S": "app_id"
                        },
                        "type": {
                            "S": "relationship"
                        },
                        "rel_display_attribute": {
                            "S": "app_name"
                        },
                        "rel_entity": {
                            "S": "application"
                        },
                        "rel_key": {
                            "S": "app_id"
                        },
                        "group_order": {
                            "S": "-998"
                        },
                        "required": {
                            "BOOL": True
                        },
                        "system": {
                            "BOOL": True
                        }
                    }
                },
                {
                    "M": {
                        "description": {
                            "S": "Server Name"
                        },
                        "name": {
                            "S": "server_name"
                        },
                        "type": {
                            "S": "string"
                        },
                        "validation_regex": {
                            "S": "^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])$"
                        },
                        "validation_regex_msg": {
                            "S": "Server names must contain only aplhanumeric, hyphen or period characters."
                        },
                        "group_order": {
                            "S": "-1000"
                        },
                        "required": {
                            "BOOL": True
                        },
                        "system": {
                            "BOOL": True
                        }
                    }
                },
                {
                    "M": {
                        "description": {
                            "S": "Server OS Family"
                        },
                        "listvalue": {
                            "S": "windows,linux"
                        },
                        "name": {
                            "S": "server_os_family"
                        },
                        "type": {
                            "S": "list"
                        },
                        "validation_regex": {
                            "S": "^(?!\\s*$).+"
                        },
                        "validation_regex_msg": {
                            "S": "Select a valid operating system."
                        },
                        "required": {
                            "BOOL": True
                        },
                        "system": {
                            "BOOL": True
                        }
                    }
                },
                {
                    "M": {
                        "description": {
                            "S": "Server OS Version"
                        },
                        "name": {
                            "S": "server_os_version"
                        },
                        "type": {
                            "S": "string"
                        },
                        "required": {
                            "BOOL": True
                        },
                        "system": {
                            "BOOL": True
                        }
                    }
                },
                {
                    "M": {
                        "description": {
                            "S": "Server FQDN"
                        },
                        "name": {
                            "S": "server_fqdn"
                        },
                        "type": {
                            "S": "string"
                        },
                        "validation_regex": {
                            "S": "^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])$"
                        },
                        "validation_regex_msg": {
                            "S": "Server FQDN must contain only aplhanumeric, hyphen or period charaters."
                        },
                        "group_order": {
                            "S": "-999"
                        },
                        "required": {
                            "BOOL": True
                        },
                        "system": {
                            "BOOL": True
                        }
                    }
                },
                {
                    "M": {
                        "description": {
                            "S": "Server Tier"
                        },
                        "name": {
                            "S": "server_tier"
                        },
                        "type": {
                            "S": "string"
                        },
                        "system": {
                            "BOOL": True
                        }
                    }
                },
                {
                    "M": {
                        "description": {
                            "S": "Server Environment"
                        },
                        "name": {
                            "S": "server_environment"
                        },
                        "type": {
                            "S": "string"
                        },
                        "group_order": {
                            "S": "-997"
                        },
                        "system": {
                            "BOOL": True
                        }
                    }
                },
                {
                    "M": {
                        "description": {
                            "S": "Subnet Ids"
                        },
                        "name": {
                            "S": "subnet_IDs"
                        },
                        "type": {
                            "S": "multivalue-string"
                        },
                        "validation_regex": {
                            "S": "^(subnet-([a-z0-9]{8}|[a-z0-9]{17})$)"
                        },
                        "validation_regex_msg": {
                            "S": "Subnets must start with subnet-, followed by 8 or 17 alphanumeric characters."
                        },
                        "group": {
                            "S": "Target - Networking"
                        },
                        "system": {
                            "BOOL": True
                        },
                        "conditions": {
                            "M": {
                                "queries": {
                                    "L": [
                                        {
                                            "M": {
                                                "comparator": {
                                                    "S": "!empty"
                                                },
                                                "attribute": {
                                                    "S": "network_interface_id"
                                                }
                                            }
                                        }
                                    ]
                                },
                                "outcomes": {
                                    "M": {
                                        "true": {
                                            "L": [
                                                {
                                                    "S": "hidden"
                                                }
                                            ]
                                        },
                                        "false": {
                                            "L": [
                                                {
                                                    "S": "not_required"
                                                }
                                            ]
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                {
                    "M": {
                        "description": {
                            "S": "Security Group Ids"
                        },
                        "name": {
                            "S": "securitygroup_IDs"
                        },
                        "type": {
                            "S": "multivalue-string"
                        },
                        "validation_regex": {
                            "S": "^(sg-([a-z0-9]{8}|[a-z0-9]{17})$)"
                        },
                        "validation_regex_msg": {
                            "S": "Security groups must start with sg-, followed by 8 or 17 alphanumeric characters."
                        },
                        "group": {
                            "S": "Target - Networking"
                        },
                        "system": {
                            "BOOL": True
                        }
                    }
                },
                {
                    "M": {
                        "description": {
                            "S": "Subnet Ids - Test"
                        },
                        "name": {
                            "S": "subnet_IDs_test"
                        },
                        "type": {
                            "S": "multivalue-string"
                        },
                        "validation_regex": {
                            "S": "^(subnet-([a-z0-9]{8}|[a-z0-9]{17})$)"
                        },
                        "validation_regex_msg": {
                            "S": "Subnets must start with subnet-, followed by 8 or 17 alphanumeric characters."
                        },
                        "group": {
                            "S": "Target"
                        },
                        "system": {
                            "BOOL": True
                        },
                        "conditions": {
                            "M": {
                                "queries": {
                                    "L": [
                                        {
                                            "M": {
                                                "comparator": {
                                                    "S": "!empty"
                                                },
                                                "attribute": {
                                                    "S": "network_interface_id_test"
                                                }
                                            }
                                        }
                                    ]
                                },
                                "outcomes": {
                                    "M": {
                                        "true": {
                                            "L": [
                                                {
                                                    "S": "hidden"
                                                }
                                            ]
                                        },
                                        "false": {
                                            "L": [
                                                {
                                                    "S": "not_required"
                                                }
                                            ]
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                {
                    "M": {
                        "description": {
                            "S": "Security Group Ids - Test"
                        },
                        "name": {
                            "S": "securitygroup_IDs_test"
                        },
                        "type": {
                            "S": "multivalue-string"
                        },
                        "validation_regex": {
                            "S": "^(sg-([a-z0-9]{8}|[a-z0-9]{17})$)"
                        },
                        "validation_regex_msg": {
                            "S": "Security groups must start with sg-, followed by 8 or 17 alphanumeric characters."
                        },
                        "group": {
                            "S": "Target - Networking"
                        },
                        "system": {
                            "BOOL": True
                        }
                    }
                },
                {
                    "M": {
                        "description": {
                            "S": "Instance Type"
                        },
                        "name": {
                            "S": "instanceType"
                        },
                        "type": {
                            "S": "string"
                        },
                        "group": {
                            "S": "Target"
                        },
                        "system": {
                            "BOOL": True
                        }
                    }
                },
                {
                    "M": {
                        "description": {
                            "S": "EC2 Instance Profile Name"
                        },
                        "name": {
                            "S": "iamRole"
                        },
                        "type": {
                            "S": "string"
                        },
                        "group": {
                            "S": "Target"
                        },
                        "system": {
                            "BOOL": True
                        },
                        "long_desc": {
                            "S": "Verify that the value entered here is the Instance Profile name not the IAM "
                                 "Role name, they maybe different. If you use the AWS CLI, API, or an AWS SDK to "
                                 "create a role, you create the role and instance profile as separate actions, with"
                                 " potentially different names."

                        }
                    }
                },
                {
                    "M": {
                        "description": {
                            "S": "Private IP"
                        },
                        "name": {
                            "S": "private_ip"
                        },
                        "type": {
                            "S": "string"
                        },
                        "group": {
                            "S": "Target - Networking"
                        },
                        "system": {
                            "BOOL": True
                        },
                        "validation_regex": {
                            "S": "^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\\.|$)){4}"
                        },
                        "validation_regex_msg": {
                            "S": "A valid IPv4 IP address must be provided."
                        },
                    }
                },
                {
                    "M": {
                        "description": {
                            "S": "Tags"
                        },
                        "name": {
                            "S": "tags"
                        },
                        "type": {
                            "S": "tag"
                        },
                        "group": {
                            "S": "Target - Instance"
                        },
                        "system": {
                            "BOOL": True
                        }
                    }
                },
                {
                    "M": {
                        "description": {
                            "S": "Tenancy"
                        },
                        "listvalue": {
                            "S": "Shared,Dedicated,Dedicated host"
                        },
                        "name": {
                            "S": "tenancy"
                        },
                        "type": {
                            "S": "list"
                        },
                        "group": {
                            "S": "Target"
                        },
                        "system": {
                            "BOOL": True
                        }
                    }
                },
                {
                    "M": {
                        "description": {
                            "S": "Migration Status"
                        },
                        "name": {
                            "S": "migration_status"
                        },
                        "type": {
                            "S": "string"
                        },
                        "system": {
                            "BOOL": True
                        },
                        "group": {
                            "S": "Status"
                        }
                    }
                },
                {
                    "M": {
                        "description": {
                            "S": "Replication Status"
                        },
                        "name": {
                            "S": "replication_status"
                        },
                        "type": {
                            "S": "string"
                        },
                        "system": {
                            "BOOL": True
                        },
                        "group": {
                            "S": "Status"
                        },
                        "conditions": {
                            "M": {
                                "queries": {
                                    "L": [
                                        {
                                            "M": {
                                                "comparator": {
                                                    "S": "!="
                                                },
                                                "value": {
                                                    "S": "Rehost"
                                                },
                                                "attribute": {
                                                    "S": "r_type"
                                                }
                                            }
                                        }
                                    ]
                                },
                                "outcomes": {
                                    "M": {
                                        "true": {
                                            "L": [
                                                {
                                                    "S": "hidden"
                                                }
                                            ]
                                        },
                                        "false": {
                                            "L": [
                                                {
                                                    "S": "not_required"
                                                }
                                            ]
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                {
                     "M": {
                         "description": {
                             "S": "Migration Strategy"
                         },
                         "listvalue": {
                             "S": "Retire,Retain,Relocate,Rehost,Repurchase,Replatform,Reachitect,TBC"
                         },
                         "name": {
                             "S": "r_type"
                         },
                         "type": {
                             "S": "list"
                         },
                         "system": {
                             "BOOL": True
                         },
                         "required": {
                             "BOOL": True
                         },
                         "help_content": {
                              "M": {
                                  "header": {
                                      "S": "Migration Strategy"
                                  },
                                  "content_html": {
                                      "S": "The following Migration Strategies are commonly used in Cloud Migration projects.  The AWS Cloud Migration factory solution supports the automation activities to assist with these strategies, for Rehost and Replatform prepackaged automations are provided, and for other strategies customized automations can be created and imported into the AWS CMF solution:\n<ul>\n<li><b>Retire</b> - Server retired and not migrated, data will need to be removed and any software services decommissioned.</li>\n<li><b>Retain</b> - Server will remain on-premise , assessment should be preformed to verify any changes for migrating dependent services.</li>\n<li><b>Relocate</b> - VMware virtual machine on-premise, is due to be relocated to VMware Cloud on AWS, using VMware HCX. Currently AWS CMF does not natively support this capability, although custom automation script packages coudl be used to interface with this service.</li>\n<li><b>Rehost</b> - AWS Cloud Migration Factory supports native integration with AWS MGN, selecting this strategy will enable the options in the server UI to support specifying the required parameters to migrate a server instance to EC2 using block level replication. The AWS CMF Solution comes packaged will all the required automation scripts to support the standard tasks required to migrate a server, all of which can be initiated from the CMF web interface.</li>\n<li><b>Repurchase</b> - Service that the server is currently supporting will be replaced with another service.</li>\n<li><b>Replatform</b> - AWS Cloud Migration Factory supports native integration to create Cloud Formation templates for each application in a wave, these Cloud Formation template are automatically generated through the UI based on the properties of the servers defined here, and can then be deployed to any account that has had the target AWS CMF Solution CFT deployed.</li>\n<li><b>Reachitect</b> - Service will be rebuilt from other services in the AWS Cloud.</li>\n</ul>\n"
                                  }
                              }
                         },
                     }
                 },
                {
                     "M": {
                         "description": {
                             "S": "Dedicated Host ID"
                         },
                         "name": {
                             "S": "dedicated_host_id"
                         },
                         "type": {
                             "S": "string"
                         },
                         "system": {
                             "BOOL": True
                         },
                         "group": {
                             "S": "Target"
                         },
                         "validation_regex": {
                             "S": "^(h-([a-z0-9]{8}|[a-z0-9]{17})$)"
                         },
                         "validation_regex_msg": {
                             "S": "Dedicated Host IDs must start with h-, followed by 8 or 17 alphanumeric characters."
                         },
                         "conditions": {
                             "M": {
                                 "outcomes": {
                                     "M": {
                                         "true": {
                                             "L": [
                                                 {
                                                     "S": "required"
                                                 }
                                             ]
                                         },
                                         "false": {
                                             "L": [
                                                 {
                                                     "S": "not_required"
                                                 },
                                                 {
                                                     "S": "hidden"
                                                 }
                                             ]
                                         }
                                     }
                                 },
                                 "queries": {
                                     "L": [
                                         {
                                             "M": {
                                                 "comparator": {
                                                     "S": "="
                                                 },
                                                 "value": {
                                                     "S": "Dedicated host"
                                                 },
                                                 "attribute": {
                                                     "S": "tenancy"
                                                 }
                                             }
                                         }
                                     ]
                                 }
                             }
                         }
                     }
                 },
                {
                     "M": {
                         "description": {
                             "S": "Network Interface ID"
                         },
                         "name": {
                             "S": "network_interface_id"
                         },
                         "type": {
                             "S": "string"
                         },
                         "validation_regex": {
                             "S": "^(eni-([a-z0-9]{8}|[a-z0-9]{17})$)"
                         },
                         "validation_regex_msg": {
                             "S": "Network Interface ID must start with eni- followed by 8 or 17 alphanumeric characters."
                         },
                         "system": {
                             "BOOL": True
                         },
                         "group": {
                             "S": "Target - Networking"
                         },
                         "help_content": {
                             "M": {
                                 "header": {
                                     "S": "Network Interface ID"
                                 },
                                 "content_html": {
                                     "S": "If Network Interface ID is provided you cannot set Subnet IDs, as the instance will be launched with this Network Interface ID.\n\nThis Network Interface ID will be assigned to the migrating server."
                                 }
                             }
                         },
                         "conditions": {
                             "M": {
                                 "queries": {
                                     "L": [
                                         {
                                             "M": {
                                                 "comparator": {
                                                     "S": "!empty"
                                                 },
                                                 "attribute": {
                                                     "S": "subnet_IDs"
                                                 }
                                             }
                                         }
                                     ]
                                 },
                                 "outcomes": {
                                     "M": {
                                         "true": {
                                             "L": [
                                                 {
                                                     "S": "hidden"
                                                 }
                                             ]
                                         },
                                         "false": {
                                             "L": [
                                                 {
                                                     "S": "not_required"
                                                 }
                                             ]
                                         }
                                     }
                                 }
                             }
                         }
                     }
                 },
                {
                     "M": {
                         "description": {
                             "S": "Network Interface ID - Test"
                         },
                         "name": {
                             "S": "network_interface_id_test"
                         },
                         "type": {
                             "S": "string"
                         },
                         "system": {
                             "BOOL": True
                         },
                         "group": {
                             "S": "Target - Networking"
                         },
                         "validation_regex": {
                             "S": "^(eni-([a-z0-9]{8}|[a-z0-9]{17})$)"
                         },
                         "validation_regex_msg": {
                             "S": "Network Interface ID must start with eni- followed by 8 or 17 alphanumeric characters."
                         },
                         "help_content": {
                             "M": {
                                 "header": {
                                     "S": "Network Interface ID - Test"
                                 },
                                 "content_html": {
                                     "S": "If 'Network Interface ID -Test' is provided you cannot set 'Subnet IDs - Test', as the instance will be launched with this Network Interface ID.\n\nThis Network Interface ID will be assigned to the migrating server."
                                 }
                             }
                         },
                         "conditions": {
                             "M": {
                                 "queries": {
                                     "L": [
                                         {
                                             "M": {
                                                 "comparator": {
                                                     "S": "!empty"
                                                 },
                                                 "attribute": {
                                                     "S": "subnet_IDs_test"
                                                 }
                                             }
                                         }
                                     ]
                                 },
                                 "outcomes": {
                                     "M": {
                                         "true": {
                                             "L": [
                                                 {
                                                     "S": "hidden"
                                                 }
                                             ]
                                         },
                                         "false": {
                                             "L": [
                                                 {
                                                     "S": "not_required"
                                                 }
                                             ]
                                         }
                                     }
                                 }
                             }
                         }
                     }
                 }
            ]
        }
    },

    {
        "schema_name": {
            "S": "database"
        },
        "schema_type": {
            "S": "user"
        },
        "attributes": {
            "L": [
               {
                     "M": {
                       "description": {
                         "S": "Database Id"
                       },
                       "hidden": {
                         "BOOL": True
                       },
                       "name": {
                         "S": "database_id"
                       },
                       "required": {
                         "BOOL": True
                       },
                       "system": {
                         "BOOL": True
                       },
                       "type": {
                         "S": "string"
                       }
                     }
                },
                {
                    "M": {
                        "description": {
                            "S": "Application"
                        },
                        "name": {
                            "S": "app_id"
                        },
                        "type": {
                            "S": "relationship"
                        },
                        "rel_display_attribute": {
                            "S": "app_name"
                        },
                        "rel_entity": {
                            "S": "application"
                        },
                        "rel_key": {
                            "S": "app_id"
                        },
                        "group_order": {
                            "S": "-998"
                        },
                        "required": {
                            "BOOL": True
                        },
                        "system": {
                            "BOOL": True
                        }
                    }
                },
                {
                    "M": {
                        "description": {
                            "S": "Database Name"
                        },
                        "name": {
                            "S": "database_name"
                        },
                        "type": {
                            "S": "string"
                        },
                        "group_order": {
                            "S": "-1000"
                        },
                        "required": {
                            "BOOL": True
                        },
                        "system": {
                            "BOOL": True
                        }
                    }
                },
                {
                    "M": {
                        "description": {
                            "S": "Database Type"
                        },
                        "listvalue": {
                            "S": "oracle,mssql,db2,mysql,postgresql"
                        },
                        "name": {
                            "S": "database_type"
                        },
                        "type": {
                            "S": "list"
                        },
                        "validation_regex": {
                            "S": "^(?!\\s*$).+"
                        },
                        "validation_regex_msg": {
                            "S": "Select a valid database type."
                        },
                        "required": {
                            "BOOL": True
                        },
                        "system": {
                            "BOOL": True
                        }
                    }
                }
            ]
        }
    },

    {
     "schema_name": {
      "S": "secret"
     },
     "schema_type": {
      "S": "system"
     },
     "attributes": {
      "L": [
       {
        "M": {
         "name": {
          "S": "name"
         },
         "description": {
          "S": "Secret Name"
         },
         "system": {
          "BOOL": True
         },
         "type": {
          "S": "string"
         },
         "long_desc": {
          "S": "Secret name."
         }
        }
       },
       {
        "M": {
         "name": {
          "S": "description"
         },
         "description": {
          "S": "Secret Description"
         },
         "system": {
          "BOOL": True
         },
         "type": {
          "S": "string"
         },
         "long_desc": {
          "S": "Secret description."
         }
        }
       },
       {
        "M": {
         "name": {
          "S": "data.SECRET_TYPE"
         },
         "description": {
          "S": "Secret Type"
         },
         "system": {
          "BOOL": True
         },
         "type": {
          "S": "string"
         },
         "long_desc": {
          "S": "Secret Type."
         }
        }
       }
      ]
     }
    },
    {
      "schema_name": {
        "S": "role"
      },
      "schema_type": {
        "S": "system"
      },
      "attributes": {
        "L": [
          {
            "M": {
              "system": {
                "BOOL": True
              },
              "name": {
                "S": "role_name"
              },
              "description": {
                "S": "Role Name"
              },
              "group_order": {
                "N": "1"
              },
              "type": {
                "S": "string"
              },
              "required": {
                "BOOL": True
              },
              "long_desc": {
                "S": "Role name"
              }
            }
          },
          {
            "M": {
              "system": {
                "BOOL": True
              },
              "hidden": {
                "BOOL": True
              },
              "name": {
                "S": "role_id"
              },
              "description": {
                "S": "Role Id"
              },
              "type": {
                "S": "string"
              },
              "required": {
                "BOOL": True
              },
              "long_desc": {
                "S": "Role ID"
              }
            }
          },
          {
            "M": {
              "listMultiSelect": {
                "BOOL": True
              },
              "system": {
                "BOOL": True
              },
              "name": {
                "S": "groups"
              },
              "description": {
                "S": "Groups"
              },
              "type": {
                "S": "groups"
              },
              "listValueAPI": {
                "S": "/admin/groups"
              },
              "required": {
                "BOOL": True
              },
              "long_desc": {
                "S": "Groups"
              }
            }
          },
          {
            "M": {
              "listMultiSelect": {
                "BOOL": True
              },
              "system": {
                "BOOL": True
              },
              "rel_display_attribute": {
                "S": "policy_name"
              },
              "rel_key": {
                "S": "policy_id"
              },
              "name": {
                "S": "policies"
              },
              "description": {
                "S": "Attached Policies"
              },
              "rel_entity": {
                "S": "policy"
              },
              "type": {
                "S": "policies"
              },
              "required": {
                "BOOL": True
              },
              "long_desc": {
                "S": "Policies"
              }
            }
          }
        ]
      }
    },
    {
      "schema_name": {
        "S": "user"
      },
      "schema_type": {
        "S": "system"
      },
      "attributes": {
        "L": [
          {
            "M": {
              "system": {
                "BOOL": True
              },
              "hidden": {
                "BOOL": True
              },
              "name": {
                "S": "userRef"
              },
              "description": {
                "S": "User reference"
              },
              "type": {
                "S": "string"
              },
              "required": {
                "BOOL": True
              },
              "long_desc": {
                "S": "User reference"
              }
            }
          },
          {
            "M": {
              "name": {
                "S": "email"
              },
              "description": {
                "S": "User Email address"
              },
              "system": {
                "BOOL": True
              },
              "type": {
                "S": "string"
              },
              "required": {
                "BOOL": True
              },
              "long_desc": {
                "S": "User Email address"
              }
            }
          },
          {
            "M": {
              "name": {
                "S": "enabled"
              },
              "description": {
                "S": "User enabled"
              },
              "system": {
                "BOOL": True
              },
              "type": {
                "S": "checkbox"
              },
              "required": {
                "BOOL": True
              },
              "long_desc": {
                "S": "User enabled"
              }
            }
          },
          {
            "M": {
              "name": {
                "S": "status"
              },
              "description": {
                "S": "User status"
              },
              "system": {
                "BOOL": True
              },
              "type": {
                "S": "string"
              },
              "required": {
                "BOOL": True
              },
              "long_desc": {
                "S": "User status"
              }
            }
          },
          {
            "M": {
              "name": {
                "S": "groups"
              },
              "description": {
                "S": "User groups"
              },
              "system": {
                "BOOL": True
              },
              "type": {
                "S": "groups"
              },
              "required": {
                "BOOL": True
              },
              "long_desc": {
                "S": "User groups"
              }
            }
          },
          {
            "M": {
              "name": {
                "S": "mfaEnabled"
              },
              "description": {
                "S": "User MFA enabled"
              },
              "system": {
                "BOOL": True
              },
              "type": {
                "S": "checkbox"
              },
              "required": {
                "BOOL": True
              },
              "long_desc": {
                "S": "User MFA enabled"
              }
            }
          }
        ]
      }
    },
    {
      "schema_name": {
        "S": "script"
      },
      "schema_type": {
        "S": "system"
      },
      "attributes": {
        "L": [
          {
            "M": {
              "system": {
                "BOOL": True
              },
              "validation_regex": {
                "S": "^(?!\\s*$).+"
              },
              "name": {
                "S": "script_name"
              },
              "description": {
                "S": "Script Name"
              },
              "validation_regex_msg": {
                "S": "Provide a name for this script."
              },
              "type": {
                "S": "string"
              },
              "required": {
                "BOOL": True
              },
              "long_desc": {
                "S": "Script name."
              }
            }
          },
          {
            "M": {
              "system": {
                "BOOL": True
              },
              "validation_regex": {
                "S": "^(?!\\s*$).+"
              },
              "name": {
                "S": "script_description"
              },
              "description": {
                "S": "Script Description"
              },
              "validation_regex_msg": {
                "S": "Provide a description of the outcome for this script."
              },
              "type": {
                "S": "string"
              },
              "required": {
                "BOOL": True
              },
              "long_desc": {
                "S": "Script description."
              }
            }
          },
          {
            "M": {
              "system": {
                "BOOL": True
              },
              "validation_regex": {
                "S": "^(?!\\s*$).+"
              },
              "name": {
                "S": "fileName"
              },
              "description": {
                "S": "Script Filename"
              },
              "validation_regex_msg": {
                "S": "Select a filename."
              },
              "type": {
                "S": "string"
              },
              "long_desc": {
                "S": "Script filename."
              }
            }
          },
          {
            "M": {
              "system": {
                "BOOL": True
              },
              "validation_regex": {
                "S": "^(?!\\s*$).+"
              },
              "name": {
                "S": "path"
              },
              "description": {
                "S": "Script path"
              },
              "validation_regex_msg": {
                "S": "Select a file path."
              },
              "type": {
                "S": "string"
              },
              "long_desc": {
                "S": "Script path."
              }
            }
          },
          {
            "M": {
              "system": {
                "BOOL": True
              },
              "validation_regex": {
                "S": "^(?!\\s*$).+"
              },
              "name": {
                "S": "script_masterfile"
              },
              "description": {
                "S": "Script master filename"
              },
              "validation_regex_msg": {
                "S": "Select a master filename path."
              },
              "type": {
                "S": "string"
              },
              "long_desc": {
                "S": "Script master filename."
              }
            }
          },
          {
            "M": {
              "name": {
                "S": "package_uuid"
              },
              "description": {
                "S": "Script UUID"
              },
              "system": {
                "BOOL": True
              },
              "type": {
                "S": "string"
              },
              "long_desc": {
                "S": "Automation script UUID."
              }
            }
          },
          {
            "M": {
              "system": {
                "BOOL": True
              },
              "readonly": {
                "BOOL": True
              },
              "name": {
                "S": "default"
              },
              "description": {
                "S": "Default Version"
              },
              "type": {
                "S": "string"
              },
              "required": {
                "BOOL": True
              },
              "long_desc": {
                "S": "Default Version."
              }
            }
          },
          {
            "M": {
              "system": {
                "BOOL": True
              },
              "readonly": {
                "BOOL": True
              },
              "name": {
                "S": "latest"
              },
              "description": {
                "S": "Latest Version"
              },
              "type": {
                "S": "string"
              },
              "required": {
                "BOOL": True
              },
              "long_desc": {
                "S": "Latest Version."
              }
            }
          }
        ]
      }
    },
    {
      "schema_name": {
        "S": "group"
      },
      "schema_type": {
        "S": "system"
      },
      "attributes": {
        "L": [
          {
            "M": {
              "name": {
                "S": "group_name"
              },
              "description": {
                "S": "Group Name"
              },
              "system": {
                "BOOL": True
              },
              "type": {
                "S": "string"
              },
              "required": {
                "BOOL": True
              },
              "long_desc": {
                "S": "Group name"
              }
            }
          }
        ]
      }
    },
    {
      "schema_name": {
        "S": "policy"
      },
      "schema_type": {
        "S": "system"
      },
      "attributes": {
        "L": [
          {
            "M": {
              "system": {
                "BOOL": True
              },
              "name": {
                "S": "policy_name"
              },
              "description": {
                "S": "Policy Name"
              },
              "group_order": {
                "N": "1"
              },
              "type": {
                "S": "string"
              },
              "required": {
                "BOOL": True
              },
              "long_desc": {
                "S": "Policy name"
              }
            }
          },
          {
            "M": {
              "system": {
                "BOOL": True
              },
              "hidden": {
                "BOOL": True
              },
              "name": {
                "S": "policy_id"
              },
              "description": {
                "S": "Policy Id"
              },
              "type": {
                "S": "string"
              },
              "required": {
                "BOOL": True
              },
              "long_desc": {
                "S": "Policy ID"
              }
            }
          },
          {
            "M": {
              "listMultiSelect": {
                "BOOL": True
              },
              "system": {
                "BOOL": True
              },
              "name": {
                "S": "entity_access"
              },
              "description": {
                "S": "Access"
              },
              "type": {
                "S": "policy"
              },
              "required": {
                "BOOL": False
              },
              "long_desc": {
                "S": "Access"
              }
            }
          }
        ]
      }
    },
    {
      "schema_name": {
        "S": "ce"
      },
      "schema_type": {
        "S": "automation"
      },
      "friendly_name": {
        "S": "CloudEndure"
      },
      "attributes": {
        "L": [
          {
            "M": {
              "system": {
                "BOOL": True
              },
              "validation_regex": {
                "S": "^(?!\\s*$).+"
              },
              "name": {
                "S": "userapitoken"
              },
              "description": {
                "S": "CloudEndure API Token"
              },
              "validation_regex_msg": {
                "S": "CE token must be provided."
              },
              "type": {
                "S": "password"
              },
              "required": {
                "BOOL": True
              },
              "long_desc": {
                "S": "CloudEndure API token."
              }
            }
          },
          {
            "M": {
              "rel_display_attribute": {
                "S": "cloudendure_projectname"
              },
              "system": {
                "BOOL": True
              },
              "validation_regex": {
                "S": "^(?!\\s*$).+"
              },
              "rel_key": {
                "S": "cloudendure_projectname"
              },
              "source_filter_attribute_name": {
                "S": "waveid"
              },
              "name": {
                "S": "projectname"
              },
              "description": {
                "S": "CloudEndure project name"
              },
              "rel_entity": {
                "S": "application"
              },
              "validation_regex_msg": {
                "S": "CE project name must be provided."
              },
              "rel_filter_attribute_name": {
                "S": "wave_id"
              },
              "type": {
                "S": "relationship"
              },
              "required": {
                "BOOL": True
              }
            }
          },
          {
            "M": {
              "rel_display_attribute": {
                "S": "wave_name"
              },
              "system": {
                "BOOL": True
              },
              "validation_regex": {
                "S": "^(?!\\s*$).+"
              },
              "rel_key": {
                "S": "wave_id"
              },
              "name": {
                "S": "waveid"
              },
              "description": {
                "S": "Wave"
              },
              "rel_entity": {
                "S": "wave"
              },
              "validation_regex_msg": {
                "S": "Wave must be provided."
              },
              "type": {
                "S": "relationship"
              },
              "required": {
                "BOOL": True
              }
            }
          },
          {
            "M": {
              "system": {
                "BOOL": True
              },
              "validation_regex": {
                "S": "^(?!\\s*$).+"
              },
              "listvalue": {
                "S": "yes, no"
              },
              "name": {
                "S": "dryrun"
              },
              "description": {
                "S": "Dryrun"
              },
              "validation_regex_msg": {
                "S": "You must choose if this is a dry run or not."
              },
              "type": {
                "S": "list"
              },
              "required": {
                "BOOL": True
              }
            }
          },
          {
            "M": {
              "system": {
                "BOOL": True
              },
              "validation_regex": {
                "S": "^(?!\\s*$).+"
              },
              "listvalue": {
                "S": "test, cutover"
              },
              "name": {
                "S": "launchtype"
              },
              "description": {
                "S": "Launch type"
              },
              "validation_regex_msg": {
                "S": "You must select a Launch type."
              },
              "type": {
                "S": "list"
              },
              "required": {
                "BOOL": True
              }
            }
          },
          {
            "M": {
              "name": {
                "S": "relaunch"
              },
              "description": {
                "S": "Enforce a server relaunch"
              },
              "system": {
                "BOOL": True
              },
              "type": {
                "S": "checkbox"
              }
            }
          }
        ]
      },
      "group": {
        "S": "Rehost"
      },
      "description": {
        "S": "CloudEndure server migration"
      },
      "actions": {
        "L": [
          {
            "M": {
              "name": {
                "S": "Status check"
              },
              "apiMethod": {
                "S": "post"
              },
              "id": {
                "S": "statuscheck"
              },
              "awsuistyle": {
                "S": "normal"
              },
              "additionalData": {
                "M": {
                  "statuscheck": {
                    "S": "yes"
                  }
                }
              },
              "apiPath": {
                "S": "/cloudendure"
              }
            }
          },
          {
            "M": {
              "name": {
                "S": "Remove servers from CE"
              },
              "apiMethod": {
                "S": "post"
              },
              "id": {
                "S": "cleanup"
              },
              "awsuistyle": {
                "S": "normal"
              },
              "additionalData": {
                "M": {
                  "cleanup": {
                    "S": "yes"
                  }
                }
              },
              "apiPath": {
                "S": "/cloudendure"
              }
            }
          },
          {
            "M": {
              "name": {
                "S": "Launch"
              },
              "apiMethod": {
                "S": "post"
              },
              "id": {
                "S": "launch"
              },
              "awsuistyle": {
                "S": "primary"
              },
              "apiPath": {
                "S": "/cloudendure"
              }
            }
          }
        ]
      }
    },
    {
      "schema_name": {
        "S": "mgn"
      },
      "schema_type": {
        "S": "automation"
      },
      "friendly_name": {
        "S": "MGN"
      },
      "attributes": {
        "L": [
          {
            "M": {
              "listMultiSelect": {
                "BOOL": True
              },
              "rel_display_attribute": {
                "S": "aws_accountid"
              },
              "hidden": {
                "BOOL": True
              },
              "rel_key": {
                "S": "aws_accountid"
              },
              "description": {
                "S": "AWS account ID"
              },
              "rel_entity": {
                "S": "application"
              },
              "type": {
                "S": "relationship"
              },
              "required": {
                "BOOL": True
              },
              "system": {
                "BOOL": True
              },
              "validation_regex": {
                "S": "^(?!\\s*$).+"
              },
              "listvalue": {
                "S": "All Accounts"
              },
              "name": {
                "S": "accountid"
              },
              "validation_regex_msg": {
                "S": "AWS account ID must be provided."
              }
            }
          },
          {
            "M": {
              "listMultiSelect": {
                "BOOL": True
              },
              "rel_display_attribute": {
                "S": "app_name"
              },
              "rel_key": {
                "S": "app_id"
              },
              "source_filter_attribute_name": {
                "S": "waveid"
              },
              "description": {
                "S": "Applications"
              },
              "rel_entity": {
                "S": "application"
              },
              "type": {
                "S": "relationship"
              },
              "required": {
                "BOOL": True
              },
              "system": {
                "BOOL": True
              },
              "validation_regex": {
                "S": "^(?!\\s*$).+"
              },
              "rel_additional_attributes": {
                "L": [
                  {
                    "S": "aws_accountid"
                  },
                  {
                    "S": "aws_region"
                  }
                ]
              },
              "name": {
                "S": "appidlist"
              },
              "validation_regex_msg": {
                "S": "At least one application must be provided."
              },
              "rel_filter_attribute_name": {
                "S": "wave_id"
              },
              "group_order": {
                 "S": "3"
              }
            }
          },
          {
            "M": {
              "rel_display_attribute": {
                "S": "wave_name"
              },
              "system": {
                "BOOL": True
              },
              "validation_regex": {
                "S": "^(?!\\s*$).+"
              },
              "rel_key": {
                "S": "wave_id"
              },
              "name": {
                "S": "waveid"
              },
              "description": {
                "S": "Wave"
              },
              "rel_entity": {
                "S": "wave"
              },
              "validation_regex_msg": {
                "S": "Wave must be provided."
              },
              "type": {
                "S": "relationship"
              },
              "required": {
                "BOOL": True
              },
              "group_order": {
                 "S": "2"
               }
            }
          },
          {
            "M": {
              "system": {
                "BOOL": True
              },
              "validation_regex": {
                "S": "^(?!\\s*$).+"
              },
              "listvalue": {
                "S": "Validate Launch Template,Launch Test Instances,Mark as Ready for Cutover,Launch Cutover Instances,Finalize Cutover,- Revert to ready for testing,- Revert to ready for cutover,- Terminate Launched instances,- Disconnect from AWS,- Mark as archived"
              },
              "name": {
                "S": "action"
              },
              "description": {
                "S": "Action"
              },
              "validation_regex_msg": {
                "S": "You must select an action to perform."
              },
              "type": {
                "S": "list"
              },
              "required": {
                "BOOL": True
              },
              "group_order": {
                "S": "1"
              }
            }
          }
        ]
      },
      "group": {
        "S": "Rehost"
      },
      "description": {
        "S": "MGN server migration"
      },
      "actions": {
        "L": [
          {
            "M": {
              "name": {
                "S": "Submit"
              },
              "apiMethod": {
                "S": "post"
              },
              "id": {
                "S": "submit"
              },
              "awsuistyle": {
                "S": "primary"
              },
              "apiPath": {
                "S": "/mgn"
              }
            }
          }
        ]
      }
    },
    {
      "schema_name": {
        "S": "ssm_job"
      },
      "schema_type": {
        "S": "automation"
      },
      "friendly_name": {
        "S": "Run Automation"
      },
      "attributes": {
        "L": [
          {
            "M": {
              "system": {
                "BOOL": True
              },
              "name": {
                "S": "mi_id"
              },
              "description": {
                "S": "Automation Server"
              },
              "group_order": {
                "S": "3"
              },
              "type": {
                "S": "list"
              },
              "listValueAPI": {
                "S": "/ssm"
              },
              "valueKey": {
                "S": "mi_id"
              },
              "labelKey": {
                "S": "mi_name"
              },
              "required": {
                "BOOL": True
              },
              "long_desc": {
                "S": "SSM Instance IDs. Only showing those with a tag defined of role=mf_automation"
              }
            }
          },
          {
            "M": {
              "system": {
                "BOOL": True
              },
              "validation_regex": {
                "S": "^(?!\\s*$).+"
              },
              "name": {
                "S": "jobname"
              },
              "description": {
                "S": "Job Name"
              },
              "validation_regex_msg": {
                "S": "Job name must be supplied."
              },
              "group_order": {
                "S": "1"
              },
              "type": {
                "S": "string"
              },
              "required": {
                "BOOL": True
              },
              "long_desc": {
                "S": "Job name."
              }
            }
          },
          {
            "M": {
              "rel_display_attribute": {
                "S": "script_name"
              },
              "system": {
                "BOOL": True
              },
              "validation_regex": {
                "S": "^(?!\\s*$).+"
              },
              "rel_key": {
                "S": "package_uuid"
              },
              "name": {
                "S": "script.package_uuid"
              },
              "description": {
                "S": "Script Name"
              },
              "rel_entity": {
                "S": "script"
              },
              "validation_regex_msg": {
                "S": "Script name must be provided."
              },
              "group_order": {
                "S": "3"
              },
              "type": {
                "S": "relationship"
              },
              "required": {
                "BOOL": True
              }
            }
          },
          {
            "M": {
              "lookup": {
                "S": "script.package_uuid"
              },
              "system": {
                "BOOL": True
              },
              "rel_attribute": {
                "S": "script_arguments"
              },
              "rel_key": {
                "S": "package_uuid"
              },
              "name": {
                "S": "script.script_arguments"
              },
              "description": {
                "S": "Script Arguments"
              },
              "rel_entity": {
                "S": "script"
              },
              "type": {
                "S": "embedded_entity"
              },
              "required": {
                "BOOL": True
              },
              "long_desc": {
                "S": "Automation Script."
              },
              "group_order": {
                "S": "4"
              },
            }
          }
        ]
      },
      "description": {
        "S": "Run Automation"
      },
      "actions": {
        "L": [
          {
            "M": {
              "name": {
                "S": "Submit Automation Job"
              },
              "apiMethod": {
                "S": "post"
              },
              "id": {
                "S": "submit"
              },
              "awsuistyle": {
                "S": "primary"
              },
              "apiPath": {
                "S": "/ssm"
              }
            }
          }
        ]
      }
    },
    {
      "schema_name": {
        "S": "job"
      },
      "schema_type": {
        "S": "automation"
      },
      "friendly_name": {
        "S": "Job"
      },
      "attributes": {
        "L": [
          {
            "M": {
              "system": {
                "BOOL": True
              },
              "hidden": {
                "BOOL": True
              },
              "validation_regex": {
                "S": "^(?!\\s*$).+"
              },
              "name": {
                "S": "SSMId"
              },
              "description": {
                "S": "SSMID"
              },
              "validation_regex_msg": {
                "S": "CE token must be provided."
              },
              "type": {
                "S": "string"
              },
              "long_desc": {
                "S": "SSM Task ID [system generated]."
              }
            }
          },
          {
            "M": {
              "default": {
                "S": "i-0de99e421ecf0fc2c"
              },
              "system": {
                "BOOL": True
              },
              "validation_regex": {
                "S": "^(?!\\s*$).+"
              },
              "name": {
                "S": "mi_id"
              },
              "description": {
                "S": "SSM Instance ID"
              },
              "validation_regex_msg": {
                "S": "MI must be supplied."
              },
              "type": {
                "S": "string"
              },
              "long_desc": {
                "S": "SSM Instance IDs. Only showing those with a tag defined of role=mf_automation"
              }
            }
          },
          {
            "M": {
              "system": {
                "BOOL": True
              },
              "validation_regex": {
                "S": "^(?!\\s*$).+"
              },
              "name": {
                "S": "jobname"
              },
              "description": {
                "S": "Job Name"
              },
              "validation_regex_msg": {
                "S": "Job name must be supplied."
              },
              "type": {
                "S": "string"
              },
              "required": {
                "BOOL": True
              },
              "long_desc": {
                "S": "Job name."
              }
            }
          },
          {
            "M": {
              "name": {
                "S": "outputLastMessage"
              },
              "description": {
                "S": "Last Message"
              },
              "system": {
                "BOOL": True
              },
              "type": {
                "S": "string"
              },
              "required": {
                "BOOL": True
              },
              "long_desc": {
                "S": "Last Message."
              }
            }
          },
          {
            "M": {
              "lookup": {
                "S": "script.package_uuid"
              },
              "system": {
                "BOOL": True
              },
              "rel_attribute": {
                "S": "script_arguments"
              },
              "rel_key": {
                "S": "package_uuid"
              },
              "name": {
                "S": "script.script_arguments"
              },
              "description": {
                "S": "Script Arguments"
              },
              "rel_entity": {
                "S": "script"
              },
              "type": {
                "S": "embedded_entity"
              },
              "required": {
                "BOOL": True
              },
              "long_desc": {
                "S": "Automation Script."
              }
            }
          },
          {
            "M": {
              "name": {
                "S": "script.script_name"
              },
              "description": {
                "S": "Script Name"
              },
              "system": {
                "BOOL": True
              },
              "type": {
                "S": "string"
              },
              "long_desc": {
                "S": "Automation Script."
              }
            }
          },
          {
            "M": {
              "name": {
                "S": "script.package_uuid"
              },
              "description": {
                "S": "Script Package UUID"
              },
              "system": {
                "BOOL": True
              },
              "type": {
                "S": "string"
              },
              "long_desc": {
                "S": "Automation Script UUID."
              }
            }
          },
          {
            "M": {
              "name": {
                "S": "script.default"
              },
              "description": {
                "S": "Script Version"
              },
              "system": {
                "BOOL": True
              },
              "type": {
                "S": "string"
              },
              "long_desc": {
                "S": "Automation Script Version Run."
              }
            }
          },
          {
            "M": {
              "name": {
                "S": "script.script_description"
              },
              "description": {
                "S": "Script Description"
              },
              "system": {
                "BOOL": True
              },
              "type": {
                "S": "string"
              },
              "long_desc": {
                "S": "Automation Script Description."
              }
            }
          },
          {
            "M": {
              "name": {
                "S": "script.script_masterfile"
              },
              "description": {
                "S": "Script FileName"
              },
              "system": {
                "BOOL": True
              },
              "type": {
                "S": "string"
              },
              "long_desc": {
                "S": "Automation script file name."
              }
            }
          },
          {
            "M": {
              "name": {
                "S": "status"
              },
              "description": {
                "S": "Status"
              },
              "system": {
                "BOOL": True
              },
              "type": {
                "S": "status"
              },
              "required": {
                "BOOL": True
              },
              "long_desc": {
                "S": "Job Status."
              }
            }
          },
          {
            "M": {
              "name": {
                "S": "SSMAutomationExecutionId"
              },
              "description": {
                "S": "SSM Execution ID"
              },
              "system": {
                "BOOL": True
              },
              "type": {
                "S": "string"
              },
              "required": {
                "BOOL": True
              },
              "long_desc": {
                "S": "SSM Execution ID."
              }
            }
          },
          {
            "M": {
              "name": {
                "S": "uuid"
              },
              "description": {
                "S": "Job ID"
              },
              "system": {
                "BOOL": True
              },
              "type": {
                "S": "string"
              },
              "long_desc": {
                "S": "Migration Factory Job ID."
              }
            }
          }
        ]
      },
      "description": {
        "S": "Automation"
      },
      "actions": {
        "L": []
      }
    }
]
