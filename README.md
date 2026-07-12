# SpartaEdNotes

Notes and practice files for AWS/Boto3, cloud concepts, and MongoDB/PyMongo.

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [File Notes](#file-notes)
- [Dependencies](#dependencies)

## Overview

This workspace is a collection of learning notes and small Python examples.
It is split into a few topic folders so related material stays together.

## Project Structure

```text
SpartaEdNotes/
|-- Boto3/
|   |-- app.py
|   |-- basic-boto-3.py
|   |-- s3_operations.py
|   |-- s3_operations_test.py
|   `-- test-s3-connection.py
|-- Cloud&AwsNotes/
|   |-- cloudnotes.md
|   |-- EC2 - MongoDB.md
|   `-- services.png
|-- MongoDB/
|   |-- MongoDB._commands.md
|   |-- PyMongo_commands.md
|   `-- PyMongoScripts/
|       |-- script.py
|       |-- script2.py
|       |-- test_connections.py
|       `-- test_script.py
|-- requirements.txt
`-- gitignore
```

## File Notes

### Boto3

- `app.py` - simple menu-driven interface for S3 actions.
- `basic-boto-3.py` - starter Boto3 example script.
- `s3_operations.py` - live S3 helper functions for bucket and object operations.
- `s3_operations_test.py` - test-friendly S3 helper module used by `app.py`.
- `test-s3-connection.py` - connection check / experimentation script.

### Cloud&AwsNotes

- `cloudnotes.md` - general cloud computing notes and terminology.
- `EC2 - MongoDB.md` - notes on using EC2 with MongoDB.
- `services.png` - image used in the cloud notes.

### MongoDB

- `MongoDB._commands.md` - command notes for MongoDB.
- `PyMongo_commands.md` - PyMongo cheat sheet and common query examples.
- `PyMongoScripts/` - small Python scripts for connecting and testing MongoDB usage.

### Root Files

- `requirements.txt` - Python dependency list for the workspace.
- `gitignore` - ignore rules for local files and environments.

## Dependencies

Current Python dependency list:

- `boto3`

