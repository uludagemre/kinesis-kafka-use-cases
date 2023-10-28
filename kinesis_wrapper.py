import boto3


class KinesisWrapper:
    def __init__(self, stream_name):
        self.client = boto3.client('kinesis', region_name='us-east-1')
        self.stream_name = stream_name

    def put_record(self, data):
        self.client.put_record(
            StreamName=self.stream_name,
            Data=data.encode('utf-8'),
            PartitionKey='some_key'
        )

    def get_records(self, shard_iterator, limit, stream_arn):
        # Simulating record retrieval from Kinesis
        response = self.client.get_records(
            ShardIterator=shard_iterator,
            Limit=limit,
            StreamARN=stream_arn
        )

        return response['Records']
