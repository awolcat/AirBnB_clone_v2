#!/usr/bin/env bash
# Set up web servers for the deployment of web_static

# Install nginx
sudo apt-get update
sudo apt-get install -y nginx

# Create document directories
sudo mkdir -p /data/web_static/shared
sudo mkdir -p /data/web_static/releases/test

# Create html document
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Change owner of document directory hierarchy
sudo chown -R "$USER":"$USER" /data/

# Edit the config file

sudo sed -i '/server_name _;/a \ \tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}\n' /etc/nginx/sites-available/default

# Restart nginx
sudo service nginx restart


