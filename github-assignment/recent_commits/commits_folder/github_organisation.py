from environ import Env
from pathlib import Path
from os.path import join
from github import Github
from csv import DictWriter


class GithubOrganisation:
    def __init__(self):
        self.__BASE_DIR = Path(__file__).resolve().parent.parent.parent
        self.__ENV = Env()
        self.__ENV.read_env(join(self.__BASE_DIR, '.env'))
        self.__GITHUB = Github(self.__ENV('GITHUB_TOKEN'))
        self.__CSVFILE = join(self.__BASE_DIR, 'github_project/csv')
        self.__URLFILE = join(self.__BASE_DIR, 'github_project/url/urls.txt')

    # Method returns the list of all repositories in an organisation.
    def __get_all_repositories(self):
        repositories = list()
        with open(self.__URLFILE, 'r') as file:
            org = self.__GITHUB.get_organization(file.readlines()[1])

        for repo in org.get_repos():
            repositories.append(repo)

        return repositories

    # Method dumps the commits of all repositories of an organisation.
    def dump_all_commits_in_csv(self):
        print('$$$$$"Inside dump_all_commits_in_csv')
        repositories = self.__get_all_repositories()
        # Defined column attributes for CSV file.
        column_names = ['username', 'author', 'date']

        with open(join(self.__CSVFILE, "all_commits.csv"), "w") as csvfile:
            print('$"Inside dump_all_commits_in_csv with column_names')
            # Defined writer object which writes the data in given csv file.
            writer = DictWriter(csvfile, fieldnames=column_names)
            # Header or column name dumped in given csv file.
            writer.writeheader()

            # Iterating through commits in all the repositories of an organisation.
            for repo in repositories:
                for commit in repo.get_commits():
                    # if author of commit is not present then skipping the commit otherwise writing it in csv file..
                    if commit.author is None:
                        continue

                    else:
                        commit_data = dict()
                        commit_data['username'] = commit.author.login
                        commit_data['author'] = commit.commit.author.name
                        commit_data['date'] = commit.commit.committer.date

                        writer.writerow(commit_data)

