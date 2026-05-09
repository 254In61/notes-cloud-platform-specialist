# Issue 1 : botocore.exceptions.NoRegionError: You must specify a region.

boto3 looks for a region in this order:
1. Explicit region in the code
2. Environment variable AWS_DEFAULT_REGION
3. AWS profile configuration (~/.aws/config)
5. Instance metadata (EC2 only)

- Ensured region=***** is included in the profile.


# issue 2 : botocore.exceptions.ConfigParseError: Unable to parse config file: C:\Users\U275003/.aws/config

- This means your AWS config file has invalid syntax, and boto3 cannot read it at all.
Because boto3 loads the same config as the AWS CLI, the parser fails before the script even runs.

- I found out that the files/aws-workspaces.txt had duplicates, so duplicate profiles.

- Fixing that fixed the issue.

# issue 3 : from modules.sso_login import SsoLogin ModuleNotFoundError: No module named 'modules'

- The structure is OK but Python doesn’t know where to look for modules.

- When you run: > python .\scripts\aws-config-rule.py , Python sets its working directory context to scripts/, not your project root.
  So it looks for: scripts/modules ❌ (doesn't exist)
  Instead of: project-root/modules ✅

- Fix Option 1 - Run as a module: 
  
  From your project root, run: > python -m scripts.aws-config-rule 1362

  This tells Python: “Treat this like a package, start from the root”

  Your structure must include:

  scripts/
    __init__.py   ✅ (add this if missing)

- Fix Option 2: Set PYTHONPATH

In PowerShell:
 $env:PYTHONPATH="."
 python .\scripts\aws-config-rule.py 1362

This manually tells Python: “Include project root in import path”

NB: Naming issue (important)

aws-config-rule.py : When using -m, Python treats - as invalid in module names.

Renamed to aws_config_rule.py
