from git import Git
import os

from git.exc import GitCommandError, GitCommandNotFound

def clone(url: str, outdir: str = 'output') -> None:
    '''
    Clone a single repo in a specified path
    '''
    
    if not os.path.exists(outdir):
        os.mkdir(outdir)
  
    try:
        Git(outdir).clone(url)
    except GitCommandError:
        pass
    
def clone_repos(repos: list[str], outdir: str = 'output') -> None:
    '''
    Clone multiple repos into a specified path
    '''
    
    for repo in repos:
        clone(repo, outdir)