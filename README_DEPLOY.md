# ARKCloudSkill Deployment

This project has been prepared for the shared ARK deployment flow:

- GitHub Actions builds a Docker image and pushes it to GHCR.
- Servers pull the image through `ops/deploy.sh`.
- Container port is always `8080`; host port is controlled by `APP_PORT`.
- `.env` stays on the server and must not be committed.
- Healthcheck endpoint is `/health`.

Workflow file: `.github/workflows/deploy-container.yml`

Project mode: `documentation-or-stack`

Required GitHub Actions secrets and variables are the same as the Deploy project:

- `PROD_SSH_PRIVATE_KEY`
- `SERVER_1_HOST`, `SERVER_2_PRIVATE_IP`, `SERVER_3_PRIVATE_IP`
- optional `GHCR_READ_TOKEN`
- variables such as `APP_NAME`, `APP_PORT`, `REMOTE_DIR`, `DEPLOY_SERVERS`

For manual redeploy of an existing image, run the workflow with `image_tag=<commit-sha>`.
