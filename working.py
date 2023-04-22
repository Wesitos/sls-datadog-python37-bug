import json

try:
    import lambda_runtime_marshaller

    OriginalEncoder = lambda_runtime_marshaller.DecimalEncoder

    class PatchedEncoder(OriginalEncoder):
        def default(self, o):
            if isinstance(o, bytes):
                return o.decode()
            return super().default(self, o)

    lambda_runtime_marshaller.DecimalEncoder = PatchedEncoder
    print('Response encoder patched')
except ImportError:
    pass

def handler(event, context):
    return {
        'principalId': ' ',
        'policyDocument': ' '
    }
