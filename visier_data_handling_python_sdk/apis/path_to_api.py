import typing_extensions

from visier_data_handling_python_sdk.paths import PathValues
from visier_data_handling_python_sdk.apis.paths.v1_op_data_connector_credentials import V1OpDataConnectorCredentials
from visier_data_handling_python_sdk.apis.paths.v1_op_data_connectors import V1OpDataConnectors
from visier_data_handling_python_sdk.apis.paths.v1_op_data_connectors_assign_credentials import V1OpDataConnectorsAssignCredentials
from visier_data_handling_python_sdk.apis.paths.v1_op_data_versions_disable import V1OpDataVersionsDisable
from visier_data_handling_python_sdk.apis.paths.v1_op_data_start_extract_and_load import V1OpDataStartExtractAndLoad
from visier_data_handling_python_sdk.apis.paths.v1_op_data_startload import V1OpDataStartload
from visier_data_handling_python_sdk.apis.paths.v1_op_data_uploads import V1OpDataUploads
from visier_data_handling_python_sdk.apis.paths.v1_op_data_uploads_exclude import V1OpDataUploadsExclude
from visier_data_handling_python_sdk.apis.paths.v1_op_data_uploads_include import V1OpDataUploadsInclude
from visier_data_handling_python_sdk.apis.paths.v1_op_job_status_jobs import V1OpJobStatusJobs
from visier_data_handling_python_sdk.apis.paths.v1_op_job_status_jobs_job_id import V1OpJobStatusJobsJobId
from visier_data_handling_python_sdk.apis.paths.v1_op_jobs_cancel import V1OpJobsCancel
from visier_data_handling_python_sdk.apis.paths.v1_op_jobs_dispatching_jobs_job_id import V1OpJobsDispatchingJobsJobId
from visier_data_handling_python_sdk.apis.paths.v1_op_jobs_dispatching_jobs_job_id_extraction_jobs import V1OpJobsDispatchingJobsJobIdExtractionJobs
from visier_data_handling_python_sdk.apis.paths.v1_op_jobs_dispatching_jobs_job_id_processing_jobs import V1OpJobsDispatchingJobsJobIdProcessingJobs
from visier_data_handling_python_sdk.apis.paths.v1_op_jobs_dispatching_jobs_job_id_receiving_jobs import V1OpJobsDispatchingJobsJobIdReceivingJobs
from visier_data_handling_python_sdk.apis.paths.v1_op_jobs_receiving_jobs_receiving_job_id import V1OpJobsReceivingJobsReceivingJobId
from visier_data_handling_python_sdk.apis.paths.v1_op_data_versions import V1OpDataVersions
from visier_data_handling_python_sdk.apis.paths.v1_op_jobs_processing_jobs_receiving_job_id import V1OpJobsProcessingJobsReceivingJobId
from visier_data_handling_python_sdk.apis.paths.v1_op_data_connector_credentials_id import V1OpDataConnectorCredentialsId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.V1_OP_DATACONNECTORCREDENTIALS: V1OpDataConnectorCredentials,
        PathValues.V1_OP_DATACONNECTORS: V1OpDataConnectors,
        PathValues.V1_OP_DATACONNECTORS_ASSIGN_CREDENTIALS: V1OpDataConnectorsAssignCredentials,
        PathValues.V1_OP_DATAVERSIONS_DISABLE: V1OpDataVersionsDisable,
        PathValues.V1_OP_DATA_START_EXTRACT_AND_LOAD: V1OpDataStartExtractAndLoad,
        PathValues.V1_OP_DATA_STARTLOAD: V1OpDataStartload,
        PathValues.V1_OP_DATA_UPLOADS: V1OpDataUploads,
        PathValues.V1_OP_DATA_UPLOADS_EXCLUDE: V1OpDataUploadsExclude,
        PathValues.V1_OP_DATA_UPLOADS_INCLUDE: V1OpDataUploadsInclude,
        PathValues.V1_OP_JOBSTATUS_JOBS: V1OpJobStatusJobs,
        PathValues.V1_OP_JOBSTATUS_JOBS_JOB_ID: V1OpJobStatusJobsJobId,
        PathValues.V1_OP_JOBS_CANCEL: V1OpJobsCancel,
        PathValues.V1_OP_JOBS_DISPATCHINGJOBS_JOB_ID: V1OpJobsDispatchingJobsJobId,
        PathValues.V1_OP_JOBS_DISPATCHINGJOBS_JOB_ID_EXTRACTIONJOBS: V1OpJobsDispatchingJobsJobIdExtractionJobs,
        PathValues.V1_OP_JOBS_DISPATCHINGJOBS_JOB_ID_PROCESSINGJOBS: V1OpJobsDispatchingJobsJobIdProcessingJobs,
        PathValues.V1_OP_JOBS_DISPATCHINGJOBS_JOB_ID_RECEIVINGJOBS: V1OpJobsDispatchingJobsJobIdReceivingJobs,
        PathValues.V1_OP_JOBS_RECEIVINGJOBS_RECEIVING_JOB_ID: V1OpJobsReceivingJobsReceivingJobId,
        PathValues.V1_OP_DATAVERSIONS: V1OpDataVersions,
        PathValues.V1_OP_JOBS_PROCESSINGJOBS_RECEIVING_JOB_ID: V1OpJobsProcessingJobsReceivingJobId,
        PathValues.V1_OP_DATACONNECTORCREDENTIALS_ID: V1OpDataConnectorCredentialsId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.V1_OP_DATACONNECTORCREDENTIALS: V1OpDataConnectorCredentials,
        PathValues.V1_OP_DATACONNECTORS: V1OpDataConnectors,
        PathValues.V1_OP_DATACONNECTORS_ASSIGN_CREDENTIALS: V1OpDataConnectorsAssignCredentials,
        PathValues.V1_OP_DATAVERSIONS_DISABLE: V1OpDataVersionsDisable,
        PathValues.V1_OP_DATA_START_EXTRACT_AND_LOAD: V1OpDataStartExtractAndLoad,
        PathValues.V1_OP_DATA_STARTLOAD: V1OpDataStartload,
        PathValues.V1_OP_DATA_UPLOADS: V1OpDataUploads,
        PathValues.V1_OP_DATA_UPLOADS_EXCLUDE: V1OpDataUploadsExclude,
        PathValues.V1_OP_DATA_UPLOADS_INCLUDE: V1OpDataUploadsInclude,
        PathValues.V1_OP_JOBSTATUS_JOBS: V1OpJobStatusJobs,
        PathValues.V1_OP_JOBSTATUS_JOBS_JOB_ID: V1OpJobStatusJobsJobId,
        PathValues.V1_OP_JOBS_CANCEL: V1OpJobsCancel,
        PathValues.V1_OP_JOBS_DISPATCHINGJOBS_JOB_ID: V1OpJobsDispatchingJobsJobId,
        PathValues.V1_OP_JOBS_DISPATCHINGJOBS_JOB_ID_EXTRACTIONJOBS: V1OpJobsDispatchingJobsJobIdExtractionJobs,
        PathValues.V1_OP_JOBS_DISPATCHINGJOBS_JOB_ID_PROCESSINGJOBS: V1OpJobsDispatchingJobsJobIdProcessingJobs,
        PathValues.V1_OP_JOBS_DISPATCHINGJOBS_JOB_ID_RECEIVINGJOBS: V1OpJobsDispatchingJobsJobIdReceivingJobs,
        PathValues.V1_OP_JOBS_RECEIVINGJOBS_RECEIVING_JOB_ID: V1OpJobsReceivingJobsReceivingJobId,
        PathValues.V1_OP_DATAVERSIONS: V1OpDataVersions,
        PathValues.V1_OP_JOBS_PROCESSINGJOBS_RECEIVING_JOB_ID: V1OpJobsProcessingJobsReceivingJobId,
        PathValues.V1_OP_DATACONNECTORCREDENTIALS_ID: V1OpDataConnectorCredentialsId,
    }
)
