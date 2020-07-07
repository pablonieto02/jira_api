from jira import JIRA
import jiraToken as token

jira = JIRA('https://jira.atlassian.com')

api_token = token.getToken()
email = token.getEmail()

auth_jira = JIRA(auth=(email, api_token))
issue = jira.issue('TPO-3')

print(issue.fields.project.key)             # 'JRA'
print(issue.fields.issuetype.name)           # 'New Feature'
print(issue.fields.reporter.displayName)    # 'Mike Cannon-Brookes [Atlassian]'