curl -XPUT 127.0.0.1:9199/_template/domain_name_typosquatting_template -H 'Content-Type: application/json' -d '
{
	"template": "domain_name_typosquatting",
	"mappings":{
		"doc*":{
			"properties":{
				"fuzzer": {
					"type": "keyword"
				},
				"domain": {
					"type": "keyword"
				},
				"original":{
					"type": "keyword"
				},
				"generator":{
					"type": "byte"
				}
			}
		}
	}
}'
