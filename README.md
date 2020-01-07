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

I also have a line that prints the number of characters in the GH token, just to verify that the token has worked. The number should be 40 characters. On top of that, there is also 

Then, run the script:

```bash
python3 repos_to_csv.py
```

Creates a file called `YOUR_ORG_repos.csv` as a list of all public repos from the organization with the following fields:

* name
* archived
* html_url
* description
* language
* created_at
* updated_at

## Original Team

* Derek Eder, DataMade


## Copyright and attribution

Copyright (c) 2016 DataMade. Released under the [MIT License](https://github.com/datamade/readme-roundup/blob/master/LICENSE).
