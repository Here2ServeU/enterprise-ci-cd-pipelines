#!/bin/bash
docker run --rm -v $(pwd):/project aquasec/trivy:latest fs /project
