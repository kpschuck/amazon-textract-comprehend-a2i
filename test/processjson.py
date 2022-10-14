import json
import re

def main():
    f = open('sample-human-review-completion-event.json')
    event = json.load(f)
    s3location = event['detail']['humanLoopOutput']['outputS3Uri']
    s3location = s3location.replace('s3://', '')
    a2iOutputBucket = s3location[0:s3location.index('/')]
    a2iOutputKey = s3location[s3location.index('/') + 1: len(s3location)]

    print("A2I Key: " + a2iOutputKey)
    print("A2I Bucket: " + a2iOutputBucket)

    custom_entities_file_uri = "s3://idp-us-east-1/comprehend-data/entity_list.csv"

    # Read the updated custom entities file and retrieve its contents
    custom_entities_file_uri = custom_entities_file_uri.replace('s3://', '')
    print("After replace", custom_entities_file_uri)
    comprehend_data_bucket = custom_entities_file_uri[0:custom_entities_file_uri.index('/')]
    print("Data bucket: " + comprehend_data_bucket)

    # Entity file that the last Custom Entity Model was trained on
    comprehend_entity_last_trained_file_key = custom_entities_file_uri[custom_entities_file_uri.index('/') + 1: len(custom_entities_file_uri)]
    print("Last trained file key:    ", comprehend_entity_last_trained_file_key)

    # Entity file that contains the latest updates from human reviews
    temp_comprehend_entity_updated_file_key = custom_entities_file_uri[custom_entities_file_uri.index('/') + 1: len(custom_entities_file_uri)]
    temp_comprehend_entity_updated_file_key = temp_comprehend_entity_updated_file_key.split('/')
    temp_comprehend_entity_updated_file_key[-1] = "updated_" + temp_comprehend_entity_updated_file_key[-1]
    temp_comprehend_entity_updated_file_key = "/".join(temp_comprehend_entity_updated_file_key)
    print("Temp comprehend updated file: ", temp_comprehend_entity_updated_file_key)
    comprehend_entity_file_key = temp_comprehend_entity_updated_file_key


if __name__ == "__main__":
    main()