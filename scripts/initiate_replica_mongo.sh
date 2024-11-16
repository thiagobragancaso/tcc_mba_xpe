curl -i -X POST -H "Accept:application/json" -H "Content-Type:application/json" \
    localhost:8083/connectors/ -d @kafka/connectors/MongoSourceConnector.json

curl -i -X POST -H "Accpet:application/json" -H "Content-Type:application/json" \
    localhost:8083/connectors/ -d @kafka/connectors/S3SinkConnector.json

# List connectors
curl -i -X GET -H "Accept:application/json" -H "Content-Type:application/json" \
    localhost:8083/connectors/



use admin;
db.auth("mongoadmin", "mongoadmin");
rs.initiate();
rs.add("xpe_mongodb_2:27017");