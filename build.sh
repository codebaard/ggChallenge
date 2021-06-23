#!/bin/sh
echo "BUILD SCRIPT: Script alive!"

git pull
 
echo "BUILD SCRIPT: building with Dockerfile."
docker build -t docker.luzifer.cloud/ggchallenge .

echo "BUILD SCRIPT: building done. Pushing..."
 
docker push docker.luzifer.cloud/ggchallenge
 
echo "BUILD SCRIPT: successfully pushed."

return 0