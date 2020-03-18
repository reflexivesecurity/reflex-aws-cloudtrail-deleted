# reflex-aws-cloudtrail-deleted
Setup up detection of DeleteTrail calls in an AWS Account.

## Usage
To use this rule either add it to your `reflex.yaml` configuration file:  
```
rules:
  - reflex-aws-cloudtrail-deleted:
      email: "example@example.com"
```

or add it directly to your Terraform:  
```
...

module "reflex-aws-cloudtrail-deleted" {
  source           = "github.com/cloudmitigator/reflex-aws-cloudtrail-deleted"
  email            = "example@example.com"
}

...
```

## License
This Reflex rule is made available under the MPL 2.0 license. For more information view the [LICENSE](https://github.com/cloudmitigator/reflex-aws-cloudtrail-deleted/blob/master/LICENSE) 