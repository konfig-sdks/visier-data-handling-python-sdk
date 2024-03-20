operation_parameter_map = {
    '/v1/op/data-connectors/assignCredentials-POST': {
        'parameters': [
            {
                'name': 'connectors'
            },
        ]
    },
    '/v1/op/jobs/cancel-POST': {
        'parameters': [
            {
                'name': 'jobIds'
            },
        ]
    },
    '/v1/op/data-connector-credentials-POST': {
        'parameters': [
            {
                'name': 'dataProviderAuthParams'
            },
            {
                'name': 'dataProviderBasicInformation'
            },
            {
                'name': 'dataProviderMetadata'
            },
            {
                'name': 'tenantCode'
            },
        ]
    },
    '/v1/op/data-connector-credentials-GET': {
        'parameters': [
            {
                'name': 'tenantCode'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'start'
            },
        ]
    },
    '/v1/op/data-connectors-GET': {
        'parameters': [
            {
                'name': 'tenantCode'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'start'
            },
        ]
    },
    '/v1/op/data-connector-credentials/:id-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'tenantCode'
            },
        ]
    },
    '/v1/op/data-versions/disable-PUT': {
        'parameters': [
            {
                'name': 'model'
            },
        ]
    },
    '/v1/op/jobs/dispatching-jobs/:jobId-GET': {
        'parameters': [
            {
                'name': 'jobId'
            },
        ]
    },
    '/v1/op/data/uploads/exclude-PUT': {
        'parameters': [
            {
                'name': 'model'
            },
        ]
    },
    '/v1/op/jobs/dispatching-jobs/:jobId/extraction-jobs-GET': {
        'parameters': [
            {
                'name': 'dispatchingJobId'
            },
            {
                'name': 'tenantCode'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'start'
            },
            {
                'name': 'jobId'
            },
        ]
    },
    '/v1/op/data/uploads/include-PUT': {
        'parameters': [
            {
                'name': 'model'
            },
        ]
    },
    '/v1/op/job-status/jobs/:jobId-GET': {
        'parameters': [
            {
                'name': 'jobId'
            },
        ]
    },
    '/v1/op/job-status/jobs-GET': {
        'parameters': [
            {
                'name': 'startTime'
            },
            {
                'name': 'endTime'
            },
            {
                'name': 'status'
            },
        ]
    },
    '/v1/op/data-versions-GET': {
        'parameters': [
            {
                'name': 'tenantCode'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'start'
            },
            {
                'name': 'numberOfVersions'
            },
        ]
    },
    '/v1/op/jobs/dispatching-jobs/:jobId/processing-jobs-GET': {
        'parameters': [
            {
                'name': 'dispatchingJobId'
            },
            {
                'name': 'tenantCode'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'start'
            },
            {
                'name': 'jobId'
            },
        ]
    },
    '/v1/op/jobs/processing-jobs/:receivingJobId-GET': {
        'parameters': [
            {
                'name': 'tenantCode'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'start'
            },
            {
                'name': 'receivingJobId'
            },
        ]
    },
    '/v1/op/jobs/dispatching-jobs/:jobId/receiving-jobs-GET': {
        'parameters': [
            {
                'name': 'dispatchingJobId'
            },
            {
                'name': 'tenantCode'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'start'
            },
            {
                'name': 'jobId'
            },
        ]
    },
    '/v1/op/jobs/receiving-jobs/:receivingJobId-GET': {
        'parameters': [
            {
                'name': 'jobs'
            },
            {
                'name': 'tenantCode'
            },
            {
                'name': 'start'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'receivingJobId'
            },
        ]
    },
    '/v1/op/data/uploads-GET': {
        'parameters': [
            {
                'name': 'uploadJobId'
            },
            {
                'name': 'tenantCode'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'start'
            },
            {
                'name': 'numberOfDataUploads'
            },
        ]
    },
    '/v1/op/data/startExtractAndLoad-POST': {
        'parameters': [
            {
                'name': 'model'
            },
        ]
    },
    '/v1/op/data/startload-POST': {
        'parameters': [
            {
                'name': 'model'
            },
        ]
    },
};