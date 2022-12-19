schema = [
  {
    "groups": {
      "L": [
        {
          "M": {
            "group_name": {
              "S": "admin"
            }
          }
        }
      ]
    },
    "role_id": {
      "S": "1"
    },
    "role_name": {
      "S": "FactoryAdmin"
    },
    "policies": {
      "L": [
        {
          "M": {
            "policy_id": {
              "S": "1"
            }
          }
        }
      ]
    }
  },
  {
    "groups": {
      "L": [
        {
          "M": {
            "group_name": {
              "S": "readonly"
            }
          }
        }
      ]
    },
    "role_id": {
      "S": "2"
    },
    "role_name": {
      "S": "FactoryReadOnly"
    },
    "policies": {
      "L": [
        {
          "M": {
            "policy_id": {
              "S": "2"
            }
          }
        }
      ]
    }
  }
]
