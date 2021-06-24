#!/bin/sh
echo "BUILD SCRIPT: Script alive!"
 
echo "BUILD SCRIPT: building with Dockerfile."
docker build -t ggchallenge .

echo "BUILD SCRIPT: building done."

return 0