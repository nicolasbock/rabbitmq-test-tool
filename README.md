# RabbitMQ-Test-Tool

![Lint](https://github.com/nicolasbock/rabbitmq-tools/workflows/CI/badge.svg)
![Publish Python Package](https://github.com/nicolasbock/rabbitmq-test-tool/workflows/Publish%20Python%20Package/badge.svg)
[![PyPI version](https://badge.fury.io/py/RabbitMQ-Test-Tool.svg)](https://badge.fury.io/py/RabbitMQ-Test-Tool)
[![rabbitmq-test-tool](https://snapcraft.io//rabbitmq-test-tool/badge.svg)](https://snapcraft.io/rabbitmq-test-tool)
[![rabbitmq-test-tool](https://snapcraft.io//rabbitmq-test-tool/trending.svg?name=0)](https://snapcraft.io/rabbitmq-test-tool)
![GitHub issues](https://img.shields.io/github/issues/nicolasbock/rabbitmq-test-tool)
![GitHub pull requests](https://img.shields.io/github/issues-pr/nicolasbock/rabbitmq-test-tool)

[![Get it from the Snap Store](https://snapcraft.io/static/images/badges/en/snap-store-black.svg)](https://snapcraft.io/rabbitmq-test-tool)

This repository contains a simple test script to test a RabbitMQ
cluster.

## Usage

Let's say we have a RabbitMQ cluster at IP address `10.5.0.{1,2,3}`.
Prepare the cluster by running:

    ./prepare-rabbit.sh 10.5.0.1

This script will create a test user and a test vhost. Detailed usage
is:

    Usage:

    prepare-rabbit.sh [options] BROKER

    Where BROKER is the address of the RabbitMQbroker to prepare.

    Options:

    --user USER       The username to set
    --password PASS   The password for USER
    --vhost VHOST     The vhost to create

Set up a `virtualenv` to run the actual test script:

    virtualenv venv
    . venv/bin/activate
    pip install -r requirements.txt
    python setup.py install

Now send a message:

    rabbitmq-test-tool 10.5.0.1 --send "My first message"

Full usage:

    usage: rabbitmq-test-tool [-h] [--durable] [--queue QUEUE] [--send MSG] [--get]
                              [--list] [--user USER] [--password PASSWORD]
                              [--vhost VHOST] [--delete QUEUE]
                              BROKER [BROKER ...]

    positional arguments:
      BROKER               The IP address or hostname of the broker, default =
                           localhost

    optional arguments:
      -h, --help           show this help message and exit
      --durable
      --queue QUEUE        The queue to use, default = test_queue
      --send MSG           Send MSG to queue
      --get                Get one message from queue
      --list               List messages in queue
      --user USER          The user to use for the RabbitMQ connection, default =
                           tester
      --password PASSWORD  The password to use for the RabbitMQ connection,
                           default = linux
      --vhost VHOST        The vhost to use for the RabbitMQ connection, default =
                           tester
      --delete QUEUE       Delete QUEUE
