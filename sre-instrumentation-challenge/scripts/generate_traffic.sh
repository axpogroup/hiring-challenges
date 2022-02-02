#!/bin/bash

# Put, get and delete some data to the storage API
task(){
  curl --silent --output /dev/null --location --request PUT "http://localhost:5000/api/buckets/$1" --data-raw '{ "data": "some json" }' ;
  sleep 0.5;

  curl --silent --output /dev/null --location --request GET "http://localhost:5000/api/buckets/$1";
  sleep 0.25;

  curl --silent --output /dev/null --location --request DELETE "http://localhost:5000/api/buckets/$1";
}


# Generate traffic in parallel runs in N-process batches
N=8
(
for i in {1..1000}; do
  ((i=i%N)); ((i++==0)) && wait

  task $i &
done
)
