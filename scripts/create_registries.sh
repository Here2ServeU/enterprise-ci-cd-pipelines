#!/bin/bash

# ----------- CONFIGURE YOUR VARIABLES ------------
AWS_REGION="us-east-1"
AWS_ECR_REPO="emmanuel-services"

AZURE_ACR_NAME="emmanuelsvcacr"
AZURE_RESOURCE_GROUP="EmmanuelRG"

GCP_PROJECT_ID="your-gcp-project-id"
GCR_REPO_NAME="emmanuel-services"
# -------------------------------------------------

# ----------- AWS ECR -----------------------------
echo "Checking AWS ECR..."
aws ecr describe-repositories --repository-names "$AWS_ECR_REPO" --region "$AWS_REGION" >/dev/null 2>&1

if [ $? -ne 0 ]; then
  echo "ECR repo not found. Creating $AWS_ECR_REPO..."
  aws ecr create-repository --repository-name "$AWS_ECR_REPO" --region "$AWS_REGION"
else
  echo "ECR repository already exists."
fi

# ----------- AZURE ACR ---------------------------
echo "Checking Azure ACR..."
ACR_CHECK=$(az acr show --name "$AZURE_ACR_NAME" --resource-group "$AZURE_RESOURCE_GROUP" --query "name" -o tsv 2>/dev/null)

if [ -z "$ACR_CHECK" ]; then
  echo "ACR not found. Creating $AZURE_ACR_NAME..."
  az acr create --name "$AZURE_ACR_NAME" --resource-group "$AZURE_RESOURCE_GROUP" --sku Basic --admin-enabled true
else
  echo "Azure ACR already exists."
fi

# ----------- GOOGLE GCR --------------------------
echo "Checking Google GCR..."
GCR_IMAGE_PATH="gcr.io/$GCP_PROJECT_ID/$GCR_REPO_NAME"
EXISTING_TAGS=$(gcloud container images list-tags "$GCR_IMAGE_PATH" --project="$GCP_PROJECT_ID" --limit=1 2>/dev/null)

if [[ $? -ne 0 ]]; then
  echo "GCR repo not found. Creating placeholder image to initialize $GCR_IMAGE_PATH..."
  docker pull hello-world
  docker tag hello-world "$GCR_IMAGE_PATH:init"
  docker push "$GCR_IMAGE_PATH:init"
else
  echo "GCR repository already exists."
fi

echo "Registry checks and creations complete."
