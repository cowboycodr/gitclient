from src.main import clone_repos

# cloning repos

repos = [
    'https://github.com/cowboycodr/gitclient'
]

clone_repos(repos)

# import from repos outdir
from output.gitclient.src.main import clone

clone('https://github.com/cowboycodr/fileengine')