import subprocess

def main():
    # pull necessary submodule
    repo = "{{cookiecutter.git_submodule}}"
    repo_name = repo.strip().split("/")[-1].replace(".git", "")

    print(repo)

    subprocess.check_call(['git', 'init'])
    subprocess.check_call(['git', 'checkout', '-b', 'main'])
    subprocess.check_call(['rm', '-rf', f'{repo_name}'])
    subprocess.check_call(['git', 'submodule', 'add', f'{repo}'])
    
    # merge config
    f = open('config.yaml', 'a')
    subprocess.check_call(['cat', f'{repo_name}/config.yaml'], stdout=f)
    f.close()

if __name__ == '__main__':
    main()
