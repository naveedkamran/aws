# AWS ECS Demo

## Pre-requisite

You need to have following dependencies:

- Ansible 2.9
- Terraform v0.15

## How to setup

Put your python app in:
- ansible/modules/roles/python-app/files/app/src

Typically the source code shall come from CI/CD pipeline or from a artifact management system but to avoid going into too much details I have wrote the code to expect the app source in above directory.

Then run ansible playbook to crete a docker image and push it to registry. The registry setting can be changed from global.yml file.

```bash
ansible-playbook "./ansible/modules/main.yml" -i ansible/hosts/hosts.yml -e "target_host=ubuntu01 profile_name=test action=all" --tags "python-app"
```

Once the image is created then run terraform apply to provision infra.
