#!/bin/bash

export PYSPARK_DRIVER_PYTHON=jupyter
export PYSPARK_DRIVER_PYTHON_OPTS='lab --ip=0.0.0.0'

$SPARK_HOME/bin/pyspark --packages io.delta:${DELTA_PACKAGE_VERSION},org.apache.hadoop:hadoop-aws:3.0.0 \
--conf "spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension" \
--conf "spark.sql.catalog.spark_catalog=org.apache.spark.sql.delta.catalog.DeltaCatalog" \
--conf "spark.hadoop.fs.s3a.impl=org.apache.hadoop.fs.s3a.S3AFileSystem" \
--conf "spark.hadoop.fs.s3a.aws.credentials.provider=org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider" \
--conf "spark.hadoop.fs.s3a.endpoint=http://172.18.0.2:9000" \
--conf "spark.hadoop.fs.s3a.access.key=minioadmin" \
--conf "spark.hadoop.fs.s3a.secret.key=minioadmin" \