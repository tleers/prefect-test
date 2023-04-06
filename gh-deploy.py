from flows import pipe
from prefect.deployments import Deployment
from prefect.filesystems import GitHub

github_block = GitHub.load("test-github-repo")

deploy_gh = Deployment.build_from_flow(
    flow=pipe,
    name="GH Python Test Deploy",
    storage=github_block,
)


if __name__ == "__main__":
    deploy_gh.apply()
