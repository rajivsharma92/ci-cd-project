#!/bin/bash
echo "Deploying new version..."
cd /home/rajiv/htmlcicd
sudo git pull origin main  # Pull the latest code
sudo systemctl restart nginx  # Restart Nginx to reflect changes
echo "Deployment complete."
