import csv
import requests
import os

def get_repo_list():

    # change these things for your org
    # org_name = 'ORG NAME'
    pages_to_fetch = 3 # number of repos you have, divided by 100. kinda hack-y!

    api_url = 'https://api.github.com/orgs/%s/repos?per_page=300' % org_name
    repos_list = []

    fields = ['name',
              'archived',
              'html_url',
              'description',
              'language',
              'created_at',
              'updated_at']

    for page in range(1,(pages_to_fetch + 1)):
        print("Page %s" % page)
        headers = {"Authorization": "token {0}".format(os.environ['GITHUB_ACCESS_TOKEN']),
        "Accept": "application/vnd.github.nebula-preview+json"}
        repos = requests.get(api_url + "&page=" + str(page), headers=headers)
        if repos.status_code == 200:
            for r in repos.json():
                repos_list.append([r[key] for key in fields])
    print(len(os.environ['GITHUB_ACCESS_TOKEN']))
    print("Repo list created. Length: %s" % len(repos_list))

    outp = open(('%s_repos.csv' % org_name), 'w')
    writer = csv.writer(outp)
    writer.writerow(fields) # header
    writer.writerows(repos_list) # data
    outp.close()

    print("File written: %s" % ('%s_repos.csv' % org_name))
    print("done")

if __name__ == "__main__":
    get_repo_list()
