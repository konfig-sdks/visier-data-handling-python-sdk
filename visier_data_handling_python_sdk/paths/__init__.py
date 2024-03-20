# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from visier_data_handling_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    V1_OP_DATACONNECTORCREDENTIALS = "/v1/op/data-connector-credentials"
    V1_OP_DATACONNECTORS = "/v1/op/data-connectors"
    V1_OP_DATACONNECTORS_ASSIGN_CREDENTIALS = "/v1/op/data-connectors/assignCredentials"
    V1_OP_DATAVERSIONS_DISABLE = "/v1/op/data-versions/disable"
    V1_OP_DATA_START_EXTRACT_AND_LOAD = "/v1/op/data/startExtractAndLoad"
    V1_OP_DATA_STARTLOAD = "/v1/op/data/startload"
    V1_OP_DATA_UPLOADS = "/v1/op/data/uploads"
    V1_OP_DATA_UPLOADS_EXCLUDE = "/v1/op/data/uploads/exclude"
    V1_OP_DATA_UPLOADS_INCLUDE = "/v1/op/data/uploads/include"
    V1_OP_JOBSTATUS_JOBS = "/v1/op/job-status/jobs"
    V1_OP_JOBSTATUS_JOBS_JOB_ID = "/v1/op/job-status/jobs/:jobId"
    V1_OP_JOBS_CANCEL = "/v1/op/jobs/cancel"
    V1_OP_JOBS_DISPATCHINGJOBS_JOB_ID = "/v1/op/jobs/dispatching-jobs/:jobId"
    V1_OP_JOBS_DISPATCHINGJOBS_JOB_ID_EXTRACTIONJOBS = "/v1/op/jobs/dispatching-jobs/:jobId/extraction-jobs"
    V1_OP_JOBS_DISPATCHINGJOBS_JOB_ID_PROCESSINGJOBS = "/v1/op/jobs/dispatching-jobs/:jobId/processing-jobs"
    V1_OP_JOBS_DISPATCHINGJOBS_JOB_ID_RECEIVINGJOBS = "/v1/op/jobs/dispatching-jobs/:jobId/receiving-jobs"
    V1_OP_JOBS_RECEIVINGJOBS_RECEIVING_JOB_ID = "/v1/op/jobs/receiving-jobs/:receivingJobId"
    V1_OP_DATAVERSIONS = "v1/op/data-versions"
    V1_OP_JOBS_PROCESSINGJOBS_RECEIVING_JOB_ID = "v1/op/jobs/processing-jobs/:receivingJobId"
    V1_OP_DATACONNECTORCREDENTIALS_ID = "/v1/op/data-connector-credentials/:id"
