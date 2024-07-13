#!/bin/bash

# Install system dependencies
apt-get update && apt-get install -y libmysqlclient-dev

# Continue with the build process
vercel build
