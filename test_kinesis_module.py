import unittest
import boto3
from moto import mock_kinesis
from kinesis_wrapper import KinesisWrapper


class TestKinesisWithMoto(unittest.TestCase):
    @mock_kinesis
    def test_kinesis_put_and_get_records(self):
        stream_name = 'test-stream'

        # Create the Kinesis stream
        kinesis = boto3.client('kinesis', region_name='us-east-1')

        kinesis.create_stream(StreamName=stream_name, ShardCount=1)

        # Use KinesisWrapper
        kinesis_wrapper = KinesisWrapper(stream_name)

        # Put records into the stream
        kinesis_wrapper.put_record('Test data 1')
        kinesis_wrapper.put_record('Test data 2')


if __name__ == '__main__':
    unittest.main()
