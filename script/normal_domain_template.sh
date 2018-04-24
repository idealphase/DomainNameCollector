curl -XPUT 127.0.0.1:9199/_template/normal_domain_name_template -H 'Content-Type: application/json' -d '
{
	"template": "normal_domain_name",
	"mappings":{
		"doc*":{
			"properties":{
				"domain": {
					"type": "keyword"
				},
				"source":{
					"type": "keyword"
				},
				"created_date":{
					"type":"date",
					"format":"yyyy-MM-dd"
				}
			}
		}
	}
}'
