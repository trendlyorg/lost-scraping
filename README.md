# lost-scraping Backup Repository

This repository serves as a dedicated backup location for the organization's n8n workflows.

## Overview

The contents of this repository are automatically managed by an automated n8n workflow. It ensures that all workflows from the n8n instance are securely backed up to GitHub, providing version history and disaster recovery capabilities.

## Structure

Workflows are organized by creation date:
`workflows/<YEAR>/<MONTH>/<WORKFLOW_ID>.json`

## Automation Details

The backup process is handled by the **[Git Backup Workflow](workflows/2025/12/32e1DuAL4dQ4bCrY.json)** detailed below:

### How it works
1.  **Trigger**: The workflow runs on a defined schedule (e.g., daily) to identify new or updated workflows.
2.  **Fetch & Compare**: It retrieves the latest workflow data from the n8n instance and checks against this repository.
3.  **Commit**: If changes or new workflows are detected, they are automatically committed to this repository.
4.  **Notification**: Upon successful backup, a notification is sent to a configured **Discord** channel (as seen in the workflow configuration).

### Configuration
The workflow is configured to commit to the `trendlyorg/lost-scraping` repository.
