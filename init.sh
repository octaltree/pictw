#!/bin/bash

env="virtualenv-3.4"
pip="pip3.4"

root=`git rev-parse --show-toplevel`
sandbox="${root}/ve"

${env} ${sandbox}
source ${sandbox}/bin/activate
${pip} install tweepy
${pip} install flask
${pip} install flask-cors
${pip} install flask-cache
