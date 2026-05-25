# COMMON STANDARDS FOR ALL .md

## Hint

Click the 'Open Preview to the Side' and see the end outcome of your document.

## Markdown Lint

Add it to the VSCode Settings :

settings.json

"markdownlint.config": {
    "MD033" : false
}

## Heading

Always increment/decrement your heading level by one hash to avoid linting warnings and errors.

At the top there will be ONLY ONE heading which could be the name of the document.

No two headings should have the same name/content.

## Unordered lists

* list item 1
* next list item

Example:

* Severity: Medium
* Resource type: `AWS::SNS::Topic`
* AWS Config rule: `sns-encrypted-kms`

If another list within a list, use indents in multiples of three(or it 4?..Check what screams with underneath yellow!) characters to maintain the list ordering

Example:

* Family
  * Dad
  * Mum
  * Child

## Ordered lists

* Mark as 1. for every line.

Markdown will number these items correctly, provided you have formatted the lines and indents to the list correctly
  
Example :

1. Python 3.10+ installed (3.12 recommended)
1. AWS CLI v2 configured with SSO profiles
1. Repository cloned and dependencies installed

## Checkout for those yellow notifications on the document

These will tell you what markdownlint reference you are breaking.

## Only 1 major heading

* Only one heading. The name of the document , marked with 1 '#'

* The rest are sub-headings and sub-sub-headings.

## URLs - Generating a clickable Link

[Name of your link](Link URL)

Example:
[Bitbucket repo](https://bitbucket.int.corp.sun/scm/cta/aws-msb-config-remediation-automation)

## Code

Should shown the language.

* If inline :

`inline code`

Example :

`config:GetComplianceDetailsByConfigRule`

`sns:GetTopicAttributes`

* If multiline :

```language_descriptor
block of code
```

Example :

```bash
git clone <repo-url>
cd aws-msb-config-remediation-automation
pip install -r requirements.txt
```

```bash
python3 -m sns.audit 1006
```

## formating 

* Bold : **text** or __text__
  
  Be consistent with the method you choose to avoid linting warnings and errors.

* Italics: *text* or _text_

  Be consistent with the method you choose to avoid linting warnings and errors.

## Blank lines at the end

* Headings should be surrounded by blank lines i.e a blank line before and after.

* No multiple consecutive blank lines.

* Files should end with a single newline character.
