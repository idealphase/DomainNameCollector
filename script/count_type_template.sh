curl -XPUT 127.0.0.1:9199/_template/count_type_template -H 'Content-Type: application/json' -d '
{
    "template": "count_type",
    "mappings":{
        "doc*":{
            "properties":{
                "count": {
                    "type": "keyword"
                },
                "timestamp":{
                    "type":"date",
                    "format":"yyyy-MM-dd:HH-mm"
                }
            }
        }
    }
}'
