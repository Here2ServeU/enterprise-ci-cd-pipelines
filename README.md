# DevSecOps Project: Build Secure CI/CD Pipelines with AI & Multi-Cloud Deployment

## Overview

This project is your all-in-one starter kit to learn and apply **DevOps**, **Site Reliability Engineering (SRE)**, and **DevSecOps** using modern automation practices and AI. No prior experience required — just follow the steps and build real-world infrastructure, pipelines, and secure deployments.

By the end, you will:

- Build and containerize a Python Flask web application
- Use **virtual environments** to isolate dependencies
- Scan infrastructure and code using **Checkov**, **Trivy**, and **Gitleaks**
- Automate deployments via **GitHub Actions**, **GitLab CI**, and **Jenkins**
- Deploy to cloud registries: AWS ECR, Azure ACR, and Google GCR
- Use AI to analyze and recommend remediations from scan results

---

## Prerequisites

Before getting started, make sure the following tools are installed on your machine:

- [Python 3.10+](https://www.python.org/)
- [Docker](https://www.docker.com/)
- [Git](https://git-scm.com/)
- [Terraform](https://developer.hashicorp.com/terraform)
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)
- [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli)
- [Google Cloud CLI](https://cloud.google.com/sdk/docs/install)
- Optional: Jenkins (for local CI/CD)

---

## Project Structure

```
.
├── emmanuel-services/
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── templates/index.html
│
├── terraform/
│   ├── main.tf
│   ├── variables.tf
│   ├── terraform.tfvars
│   └── outputs.tf
│
├── .github/workflows/deploy.yml
├── .gitlab-ci.yml
├── jenkins/Jenkinsfile
├── scripts/
│   ├── trivy-scan.sh
│   ├── create_registries.sh
│   └── ai_analyzer.py
└── README.md
```

---

## Getting Started with Python Virtual Environment

### 1. Clone the Repository

```bash
git clone https://github.com/Here2ServeU/portfolio-sre-devops.git
cd portfolio-sre-devops/emmanuel-services
```

### 2. Set Up Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Run Flask App Locally

```bash
python app.py
```

Access your app at: [http://localhost:5050](http://localhost:5050)

---

## Deploying Infrastructure with Terraform

```bash
cd ../terraform
terraform init
terraform plan
terraform apply
```

---

## Run Security Scans

```bash
chmod +x ../scripts/trivy-scan.sh
../scripts/trivy-scan.sh

# AI-enhanced analysis
python ../scripts/ai_analyzer.py
```

---

## Use CI/CD Pipelines

### GitHub Actions
- Uncomment the following lines on .github/workflows/deploy.yml
```yml
#name: DevSecOps CI/CD Pipeline

#on:
#  push:
#    branches: [main]
#  pull_request:
```
- Push to `main` triggers `.github/workflows/deploy.yml`

### GitLab CI

On push, `.gitlab-ci.yml` runs and deploys

### Jenkins

Connect Jenkins to your repo and use `jenkins/Jenkinsfile`

---

## Deploy to Cloud Registries

You can auto-create the container registries via:

```bash
./scripts/create_registries.sh
```

Then your pipelines push to:
- **AWS ECR**
- **Azure ACR**
- **Google GCR**

---

## Built-in Security Tools

| Tool     | Use Case                        |
|----------|----------------------------------|
| Checkov  | Terraform IaC misconfigs         |
| Trivy    | Docker image vulnerabilities     |
| Gitleaks | Secrets exposed in code          |
| OpenAI   | Summarize & suggest remediations |

---

## Author

**By Emmanuel Naweji, 2025**  
Cloud | DevOps | SRE | FinOps | AI Engineer

- [LinkedIn](https://www.linkedin.com/in/ready2assist/)
- [GitHub](https://github.com/Here2ServeU)
- [Free 1:1 Consultation](https://bit.ly/letus-meet)

---

## License

MIT License - free to use and modify for learning or production.

