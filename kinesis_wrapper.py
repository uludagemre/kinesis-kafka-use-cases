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

    def consume_records(self):
        shard_iterator = self.client.get_shard_iterator(
            StreamName=self.stream_name,
            ShardId='shardId-000000000000',  # Replace with your actual shard ID
            ShardIteratorType='TRIM_HORIZON'
        )['ShardIterator']

        records = []
        while True:
            response = self.client.get_records(ShardIterator=shard_iterator, Limit=10)
            if not response['Records']:
                break
            records.extend(list(map(lambda x: x['Data'], response['Records'])))
            shard_iterator = response['NextShardIterator']

        return records
