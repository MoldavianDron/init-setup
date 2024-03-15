from jiraone import LOGIN, issue_export
import json

file = "config.json"
config = json.load(open(file))
LOGIN(**config)

jql = "project in (Whiteboards) order by created DESC"
issue_export(jql=jql)