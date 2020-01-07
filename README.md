# repo-roundup

python script that pulls a list of organization repos from the GitHub API into a CSV

## Note: This was forked from https://github.com/datamade/repo-roundup and tweaked to fit my needs.

## Dependencies

* python 3.x
* a GitHub account or organization
* the [GitHub API v3](https://developer.github.com/v3/)

## Usage

Edit `repos_to_csv.py` and add your organization settings:

```python
# change these things for your org
org_name = 'your-org-name'
pages_to_fetch = 2 # number of repos you have, divided by 100. kinda hack-y!
```

For my personal implementation, I added the "archived" header and a line for a github token. You need the github token for private repositories. You'll need to generate your own github token, run it in your terminal with `export GITHUB_ACCESS_TOKEN=YOUR_TOKEN` then proceed with running the script.

Then, run the script:

```bash
python3 repos_to_csv.py
```

Creates a file called `YOUR_ORG_repos.csv` as a list of all public repos from the organization with the following fields:

* name
* archived
* html_url
* description
* homepage
* language
* created_at
* updated_at

## Team

* Derek Eder, DataMade

## Errors and bugs

If something is not behaving intuitively, it is a bug and should be reported.
Report it here by creating an issue: https://github.com/datamade/readme-roundup/issues

Help us fix the problem as quickly as possible by following [Mozilla's guidelines for reporting bugs.](https://developer.mozilla.org/en-US/docs/Mozilla/QA/Bug_writing_guidelines#General_Outline_of_a_Bug_Report)

## Patches and pull requests

Your patches are welcome. Here's our suggested workflow:

* Fork the project.
* Make your feature addition or bug fix.
* Send us a pull request with a description of your work. Bonus points for topic branches!

## Copyright and attribution

Copyright (c) 2016 DataMade. Released under the [MIT License](https://github.com/datamade/readme-roundup/blob/master/LICENSE).
