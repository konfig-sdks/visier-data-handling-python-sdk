<div align="center">

[![Visit Visier](./header.png)](https://visier.com)

# Visier<a id="visier"></a>

Visier APIs for data and job handling


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`visierdatahandling.data_and_job_handling.assign_connector_credential`](#visierdatahandlingdata_and_job_handlingassign_connector_credential)
  * [`visierdatahandling.data_and_job_handling.cancel_jobs`](#visierdatahandlingdata_and_job_handlingcancel_jobs)
  * [`visierdatahandling.data_and_job_handling.create_connector_credential`](#visierdatahandlingdata_and_job_handlingcreate_connector_credential)
  * [`visierdatahandling.data_and_job_handling.data_connector_credentials`](#visierdatahandlingdata_and_job_handlingdata_connector_credentials)
  * [`visierdatahandling.data_and_job_handling.data_connectors`](#visierdatahandlingdata_and_job_handlingdata_connectors)
  * [`visierdatahandling.data_and_job_handling.delete_connector_credential`](#visierdatahandlingdata_and_job_handlingdelete_connector_credential)
  * [`visierdatahandling.data_and_job_handling.disable_dv`](#visierdatahandlingdata_and_job_handlingdisable_dv)
  * [`visierdatahandling.data_and_job_handling.dispatching_job_status`](#visierdatahandlingdata_and_job_handlingdispatching_job_status)
  * [`visierdatahandling.data_and_job_handling.exclude_data_uplaods`](#visierdatahandlingdata_and_job_handlingexclude_data_uplaods)
  * [`visierdatahandling.data_and_job_handling.extraction_job_and_status`](#visierdatahandlingdata_and_job_handlingextraction_job_and_status)
  * [`visierdatahandling.data_and_job_handling.include_data_uploads`](#visierdatahandlingdata_and_job_handlinginclude_data_uploads)
  * [`visierdatahandling.data_and_job_handling.job_id_status`](#visierdatahandlingdata_and_job_handlingjob_id_status)
  * [`visierdatahandling.data_and_job_handling.job_status`](#visierdatahandlingdata_and_job_handlingjob_status)
  * [`visierdatahandling.data_and_job_handling.latest_enabled_dv`](#visierdatahandlingdata_and_job_handlinglatest_enabled_dv)
  * [`visierdatahandling.data_and_job_handling.processing_job_and_status`](#visierdatahandlingdata_and_job_handlingprocessing_job_and_status)
  * [`visierdatahandling.data_and_job_handling.processing_job_status`](#visierdatahandlingdata_and_job_handlingprocessing_job_status)
  * [`visierdatahandling.data_and_job_handling.receiving_job_and_status`](#visierdatahandlingdata_and_job_handlingreceiving_job_and_status)
  * [`visierdatahandling.data_and_job_handling.receiving_job_status`](#visierdatahandlingdata_and_job_handlingreceiving_job_status)
  * [`visierdatahandling.data_and_job_handling.retrieve_data_uploads`](#visierdatahandlingdata_and_job_handlingretrieve_data_uploads)
  * [`visierdatahandling.data_and_job_handling.start_extraction`](#visierdatahandlingdata_and_job_handlingstart_extraction)
  * [`visierdatahandling.data_and_job_handling.start_load`](#visierdatahandlingdata_and_job_handlingstart_load)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Visier&serviceName=DataHandling&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from visier_data_handling_python_sdk import VisierDataHandling, ApiException

visierdatahandling = VisierDataHandling(

        api_key_auth = 'YOUR_API_KEY',

    access_token = 'YOUR_BEARER_TOKEN',

        cookie_auth = 'YOUR_API_KEY',

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',,

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',
)

try:
    # Assign connector credentials to data connectors
    assign_connector_credential_response = visierdatahandling.data_and_job_handling.assign_connector_credential(
        connectors=[
        {
        }
    ],
    )
    print(assign_connector_credential_response)
except ApiException as e:
    print("Exception when calling DataAndJobHandlingApi.assign_connector_credential: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python

import asyncio
from pprint import pprint
from visier_data_handling_python_sdk import VisierDataHandling, ApiException

visierdatahandling = VisierDataHandling(

        api_key_auth = 'YOUR_API_KEY',

    access_token = 'YOUR_BEARER_TOKEN',

        cookie_auth = 'YOUR_API_KEY',

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',,

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',
)

async def main():
    try:
        # Assign connector credentials to data connectors
        assign_connector_credential_response = await visierdatahandling.data_and_job_handling.aassign_connector_credential(
            connectors=[
        {
        }
    ],
        )
        print(assign_connector_credential_response)
    except ApiException as e:
        print("Exception when calling DataAndJobHandlingApi.assign_connector_credential: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)

asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from visier_data_handling_python_sdk import VisierDataHandling, ApiException

visierdatahandling = VisierDataHandling(

        api_key_auth = 'YOUR_API_KEY',

    access_token = 'YOUR_BEARER_TOKEN',

        cookie_auth = 'YOUR_API_KEY',

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',,

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',
)

try:
    # Assign connector credentials to data connectors
    assign_connector_credential_response = visierdatahandling.data_and_job_handling.raw.assign_connector_credential(
        connectors=[
        {
        }
    ],
    )
    pprint(assign_connector_credential_response.body)
    pprint(assign_connector_credential_response.body["tenants"])
    pprint(assign_connector_credential_response.headers)
    pprint(assign_connector_credential_response.status)
    pprint(assign_connector_credential_response.round_trip_time)
except ApiException as e:
    print("Exception when calling DataAndJobHandlingApi.assign_connector_credential: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `visierdatahandling.data_and_job_handling.assign_connector_credential`<a id="visierdatahandlingdata_and_job_handlingassign_connector_credential"></a>

This API allows you to assign a connector credential to a data connector.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
assign_connector_credential_response = visierdatahandling.data_and_job_handling.assign_connector_credential(
    connectors=[
        {
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### connectors: List[`Connector`]<a id="connectors-listconnector"></a>

A list of objects representing the data connectors to be assigned with credentials.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AssignConnectorCredentialRequest`](./visier_data_handling_python_sdk/type/assign_connector_credential_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AssignConnectorCredentialsResponseDTO`](./visier_data_handling_python_sdk/pydantic/assign_connector_credentials_response_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/op/data-connectors/assignCredentials` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visierdatahandling.data_and_job_handling.cancel_jobs`<a id="visierdatahandlingdata_and_job_handlingcancel_jobs"></a>

Use this API to cancel a list of processing jobs, upload jobs, receiving jobs, and extraction jobs.

 Note: Receiving jobs with the Running status cannot be cancelled.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
cancel_jobs_response = visierdatahandling.data_and_job_handling.cancel_jobs(
    job_ids=[
        "string_example"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### job_ids: [`CancelJobBatchFromJobIdDTOJobIds`](./visier_data_handling_python_sdk/type/cancel_job_batch_from_job_id_dto_job_ids.py)<a id="job_ids-canceljobbatchfromjobiddtojobidsvisier_data_handling_python_sdktypecancel_job_batch_from_job_id_dto_job_idspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CancelJobBatchFromJobIdDTO`](./visier_data_handling_python_sdk/type/cancel_job_batch_from_job_id_dto.py)
#### 🔄 Return<a id="🔄-return"></a>

[`JobCancellationResultsDTO`](./visier_data_handling_python_sdk/pydantic/job_cancellation_results_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/op/jobs/cancel` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visierdatahandling.data_and_job_handling.create_connector_credential`<a id="visierdatahandlingdata_and_job_handlingcreate_connector_credential"></a>

Use this API to create connector credentials for a specified tenant. Connector credentials allow Visier to
 retrieve data from your source systems through an integration user in the source system.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_connector_credential_response = visierdatahandling.data_and_job_handling.create_connector_credential(
    data_provider_auth_params={
        "provider": "Bamboo",
        "auth_context": "DefaultDataExtraction",
    },
    data_provider_basic_information={
    },
    data_provider_metadata={
    },
    tenant_code="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### data_provider_auth_params: [`DataProviderAuthParamsDTO`](./visier_data_handling_python_sdk/type/data_provider_auth_params_dto.py)<a id="data_provider_auth_params-dataproviderauthparamsdtovisier_data_handling_python_sdktypedata_provider_auth_params_dtopy"></a>


The authentication information for the credential.

##### data_provider_basic_information: [`DataProviderBasicInformationDTO`](./visier_data_handling_python_sdk/type/data_provider_basic_information_dto.py)<a id="data_provider_basic_information-dataproviderbasicinformationdtovisier_data_handling_python_sdktypedata_provider_basic_information_dtopy"></a>


The display name and description for the credential.

##### data_provider_metadata: [`DataProviderBasicMetadataDTO`](./visier_data_handling_python_sdk/type/data_provider_basic_metadata_dto.py)<a id="data_provider_metadata-dataproviderbasicmetadatadtovisier_data_handling_python_sdktypedata_provider_basic_metadata_dtopy"></a>


##### tenant_code: `str`<a id="tenant_code-str"></a>

The tenant code of a specific analytic tenant that you want to create the credential for.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DataProviderAuthInformationDTO`](./visier_data_handling_python_sdk/type/data_provider_auth_information_dto.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CredentialCreationAPIResponseDTO`](./visier_data_handling_python_sdk/pydantic/credential_creation_api_response_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/op/data-connector-credentials` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visierdatahandling.data_and_job_handling.data_connector_credentials`<a id="visierdatahandlingdata_and_job_handlingdata_connector_credentials"></a>

Use this API to retrieve a list of the connector credentials in a specified tenant. Connector credentials allow
 Visier to retrieve data from your source systems through an integration user in the source system.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
data_connector_credentials_response = visierdatahandling.data_and_job_handling.data_connector_credentials(
    tenant_code="string_example",
    limit=1,
    start=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tenant_code: `str`<a id="tenant_code-str"></a>

The tenant code of a specific analytic tenant that you want to retrieve for.

##### limit: `int`<a id="limit-int"></a>

The limit to retrieve.

##### start: `int`<a id="start-int"></a>

The index to start retrieving results from, also known as offset. The index begins at 0.

#### 🔄 Return<a id="🔄-return"></a>

[`ExtractorCredentialsAPIDTO`](./visier_data_handling_python_sdk/pydantic/extractor_credentials_apidto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/op/data-connector-credentials` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visierdatahandling.data_and_job_handling.data_connectors`<a id="visierdatahandlingdata_and_job_handlingdata_connectors"></a>

Use this API to retrieve a list of the data connectors in a specified tenant. Data connectors are an alternative
 to generating flat files and transferring them to Visier via SFTP.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
data_connectors_response = visierdatahandling.data_and_job_handling.data_connectors(
    tenant_code="string_example",
    limit=1,
    start=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tenant_code: `str`<a id="tenant_code-str"></a>

The tenant code of a specific analytic tenant that you want to retrieve for.

##### limit: `int`<a id="limit-int"></a>

The limit to retrieve.

##### start: `int`<a id="start-int"></a>

The index to start retrieving results from, also known as offset. The index begins at 0.

#### 🔄 Return<a id="🔄-return"></a>

[`ImportDefinitionsAPIDTO`](./visier_data_handling_python_sdk/pydantic/import_definitions_apidto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/op/data-connectors` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visierdatahandling.data_and_job_handling.delete_connector_credential`<a id="visierdatahandlingdata_and_job_handlingdelete_connector_credential"></a>

Use this API to delete connector credentials from your tenants. Credentials that are no longer valid
 should be deleted.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_connector_credential_response = visierdatahandling.data_and_job_handling.delete_connector_credential(
    id="string_example",
    tenant_code="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The credentialId of the credential you want to delete.

##### tenant_code: `str`<a id="tenant_code-str"></a>

The tenant code of the analytic tenant in which the credential you're deleting.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/op/data-connector-credentials/:id` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visierdatahandling.data_and_job_handling.disable_dv`<a id="visierdatahandlingdata_and_job_handlingdisable_dv"></a>

If you discover that a data version is not what is expected after running metric value validation on a data load,
 you may want to disable the data version for that processing job.

 Use this API to disable the latest enabled data versions for affected analytic tenants or to disable a particular
 data version for each analytic tenant.

 Note: Disabling an older data version may not have an effect on the state of the solution.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
disable_dv_response = visierdatahandling.data_and_job_handling.disable_dv(
    model={
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### model: [`DisableDVModel`](./visier_data_handling_python_sdk/type/disable_dv_model.py)<a id="model-disabledvmodelvisier_data_handling_python_sdktypedisable_dv_modelpy"></a>


A form body key that contains a collection of key-value pairs.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DisableDVRequest`](./visier_data_handling_python_sdk/type/disable_dv_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`DisableDVResponse`](./visier_data_handling_python_sdk/pydantic/disable_dv_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/op/data-versions/disable` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visierdatahandling.data_and_job_handling.dispatching_job_status`<a id="visierdatahandlingdata_and_job_handlingdispatching_job_status"></a>

Use this API to retrieve the status of a dispatching job, including its job ID and the number of jobs it generated.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
dispatching_job_status_response = visierdatahandling.data_and_job_handling.dispatching_job_status(
    job_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### job_id: `str`<a id="job_id-str"></a>

The ID of the job you want to retrieve.

#### 🔄 Return<a id="🔄-return"></a>

[`DispatchingJobStatusResponse`](./visier_data_handling_python_sdk/pydantic/dispatching_job_status_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/op/jobs/dispatching-jobs/:jobId` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visierdatahandling.data_and_job_handling.exclude_data_uplaods`<a id="visierdatahandlingdata_and_job_handlingexclude_data_uplaods"></a>

Use this API to exclude either a specified list of data uploads or all data uploads for each analytic tenant.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
exclude_data_uplaods_response = visierdatahandling.data_and_job_handling.exclude_data_uplaods(
    model={
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### model: [`UploadToExcludeModel`](./visier_data_handling_python_sdk/type/upload_to_exclude_model.py)<a id="model-uploadtoexcludemodelvisier_data_handling_python_sdktypeupload_to_exclude_modelpy"></a>


A form body key that contains a collection of key-value pairs.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ExcludeDataUploadsRequest`](./visier_data_handling_python_sdk/type/exclude_data_uploads_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`TenantDataUploadsUpdateResponseDTO`](./visier_data_handling_python_sdk/pydantic/tenant_data_uploads_update_response_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/op/data/uploads/exclude` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visierdatahandling.data_and_job_handling.extraction_job_and_status`<a id="visierdatahandlingdata_and_job_handlingextraction_job_and_status"></a>

Use this API to retrieve the statuses of extraction jobs associated with a dispatching job. The dispatching job
 is a "parent" to extraction jobs, which retrieve data from your source systems through data connectors.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
extraction_job_and_status_response = visierdatahandling.data_and_job_handling.extraction_job_and_status(
    dispatching_job_id="string_example",
    tenant_code="string_example",
    limit=1,
    start=1,
    job_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### dispatching_job_id: `str`<a id="dispatching_job_id-str"></a>

The ID of the dispatching job that generated the extraction jobs.

##### tenant_code: `str`<a id="tenant_code-str"></a>

The tenant code of a specific analytic tenant that you want to retrieve the extraction job status for.  Use this if you are only interested in the results for one analytic tenant.

##### limit: `int`<a id="limit-int"></a>

The limit of extraction job statuses to retrieve.

##### start: `int`<a id="start-int"></a>

The index to start retrieving results from, also known as offset. The index begins at 0.

##### job_id: `str`<a id="job_id-str"></a>

The ID of the dispatching job you want to retrieve.

#### 🔄 Return<a id="🔄-return"></a>

[`ExtractionJobAndStatusResponse`](./visier_data_handling_python_sdk/pydantic/extraction_job_and_status_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/op/jobs/dispatching-jobs/:jobId/extraction-jobs` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visierdatahandling.data_and_job_handling.include_data_uploads`<a id="visierdatahandlingdata_and_job_handlinginclude_data_uploads"></a>

Use this API to include either the specified list of data uploads or all data uploads for each analytic tenant.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
include_data_uploads_response = visierdatahandling.data_and_job_handling.include_data_uploads(
    model={
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### model: [`UploadToIncludeModel`](./visier_data_handling_python_sdk/type/upload_to_include_model.py)<a id="model-uploadtoincludemodelvisier_data_handling_python_sdktypeupload_to_include_modelpy"></a>


A form body key that contains a collection of key-value pairs.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`IncludeDataUploadsRequest`](./visier_data_handling_python_sdk/type/include_data_uploads_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`TenantDataUploadsUpdateResponseDTO`](./visier_data_handling_python_sdk/pydantic/tenant_data_uploads_update_response_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/op/data/uploads/include` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visierdatahandling.data_and_job_handling.job_id_status`<a id="visierdatahandlingdata_and_job_handlingjob_id_status"></a>

Use this API to retrieve the list of statuses for a specific job with id `jobId`.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
job_id_status_response = visierdatahandling.data_and_job_handling.job_id_status(
    job_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### job_id: `str`<a id="job_id-str"></a>

The unique ID of the job to retrieve the status for.

#### 🔄 Return<a id="🔄-return"></a>

[`ReceivingJobStatusResponse`](./visier_data_handling_python_sdk/pydantic/receiving_job_status_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/op/job-status/jobs/:jobId` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visierdatahandling.data_and_job_handling.job_status`<a id="visierdatahandlingdata_and_job_handlingjob_status"></a>

Use this API to retrieve the list of statuses for all jobs.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
job_status_response = visierdatahandling.data_and_job_handling.job_status(
    start_time="string_example",
    end_time="string_example",
    status="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### start_time: `str`<a id="start_time-str"></a>

The start time from which to retrieve job statuses.

##### end_time: `str`<a id="end_time-str"></a>

The end time from which to retrieve job statuses.

##### status: `str`<a id="status-str"></a>

The specific status to restrict the list of job to.

#### 🔄 Return<a id="🔄-return"></a>

[`ReceivingJobStatusResponse`](./visier_data_handling_python_sdk/pydantic/receiving_job_status_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/op/job-status/jobs` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visierdatahandling.data_and_job_handling.latest_enabled_dv`<a id="visierdatahandlingdata_and_job_handlinglatest_enabled_dv"></a>

If you discover any inconsistencies after running metric value validation, you may want to find the data versions
 causing inconsistencies so you can later disable them.

 Use this API to retrieve up to five (5) of the latest enabled data versions for all your analytic tenants or a
 single specified analytic tenant.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
latest_enabled_dv_response = visierdatahandling.data_and_job_handling.latest_enabled_dv(
    tenant_code="string_example",
    limit=1,
    start=1,
    number_of_versions=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tenant_code: `str`<a id="tenant_code-str"></a>

The tenant code of a specific analytic tenant that you want to retrieve data versions for.  Use this if you are only interested in the results for one analytic tenant.

##### limit: `int`<a id="limit-int"></a>

The limit of analytic tenants to retrieve data versions for.  This parameter is not used if the tenantCode parameter is specified.

##### start: `int`<a id="start-int"></a>

The index to start retrieving results from, also known as offset. The index begins at 0.

##### number_of_versions: `int`<a id="number_of_versions-int"></a>

The number of latest enabled data versions to retrieve. The maximum value is 5.

#### 🔄 Return<a id="🔄-return"></a>

[`MultipleTenantDataVersionsListDTO`](./visier_data_handling_python_sdk/pydantic/multiple_tenant_data_versions_list_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/op/data-versions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visierdatahandling.data_and_job_handling.processing_job_and_status`<a id="visierdatahandlingdata_and_job_handlingprocessing_job_and_status"></a>

Use this API to retrieve the statuses of processing jobs associated with a dispatching job. The dispatching job
 is a "parent" to extraction jobs, which in turn generate processing jobs and receiving jobs.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
processing_job_and_status_response = visierdatahandling.data_and_job_handling.processing_job_and_status(
    dispatching_job_id="string_example",
    tenant_code="string_example",
    limit=1,
    start=1,
    job_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### dispatching_job_id: `str`<a id="dispatching_job_id-str"></a>

The ID of the dispatching job that generated the extraction jobs.

##### tenant_code: `str`<a id="tenant_code-str"></a>

The tenant code of a specific analytic tenant that you want to retrieve the extraction job status for.  Use this if you are only interested in the results for one analytic tenant.

##### limit: `int`<a id="limit-int"></a>

The limit of extraction job statuses to retrieve.

##### start: `int`<a id="start-int"></a>

The index to start retrieving results from, also known as offset. The index begins at 0.

##### job_id: `str`<a id="job_id-str"></a>

The ID of the dispatching job you want to retrieve.

#### 🔄 Return<a id="🔄-return"></a>

[`ProcessingJobAndStatusResponse`](./visier_data_handling_python_sdk/pydantic/processing_job_and_status_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/op/jobs/dispatching-jobs/:jobId/processing-jobs` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visierdatahandling.data_and_job_handling.processing_job_status`<a id="visierdatahandlingdata_and_job_handlingprocessing_job_status"></a>

Use this API to retrieve a list of statuses for all processing jobs associated with the given receiving job ID.
 Processing jobs deal with an individual analytic tenant's data load. A processing job is either triggered through
 the UI or is one of many processing jobs spawned from a receiving job. When a processing job is triggered as part
 of a set from an receiving job, it is associated to the receiving job through a Parent ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
processing_job_status_response = visierdatahandling.data_and_job_handling.processing_job_status(
    tenant_code="string_example",
    limit=1,
    start=1,
    receiving_job_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tenant_code: `str`<a id="tenant_code-str"></a>

The tenant code of the tenant you want to retrieve the processing jobs for.  Use this if you are only interested in the results for one analytic tenant.

##### limit: `int`<a id="limit-int"></a>

The limit of processing jobs to retrieve per page.

##### start: `int`<a id="start-int"></a>

The index to start retrieving results from, also known as offset. The index begins at 0.

##### receiving_job_id: `str`<a id="receiving_job_id-str"></a>

The receiving job ID

#### 🔄 Return<a id="🔄-return"></a>

[`ProcessingJobStatusResponse`](./visier_data_handling_python_sdk/pydantic/processing_job_status_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/op/jobs/processing-jobs/:receivingJobId` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visierdatahandling.data_and_job_handling.receiving_job_and_status`<a id="visierdatahandlingdata_and_job_handlingreceiving_job_and_status"></a>

Use this API to retrieve the statuses of receiving jobs associated with a dispatching job. The dispatching job
 is a "parent" to extraction jobs, which in turn generate processing jobs and receiving jobs.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
receiving_job_and_status_response = visierdatahandling.data_and_job_handling.receiving_job_and_status(
    dispatching_job_id="string_example",
    tenant_code="string_example",
    limit=1,
    start=1,
    job_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### dispatching_job_id: `str`<a id="dispatching_job_id-str"></a>

The ID of the dispatching job that generated the extraction jobs.

##### tenant_code: `str`<a id="tenant_code-str"></a>

The tenant code of a specific analytic tenant that you want to retrieve the extraction job status for.  Use this if you are only interested in the results for one analytic tenant.

##### limit: `int`<a id="limit-int"></a>

The limit of extraction job statuses to retrieve.

##### start: `int`<a id="start-int"></a>

The index to start retrieving results from, also known as offset. The index begins at 0.

##### job_id: `str`<a id="job_id-str"></a>

The ID of the dispatching job you want to retrieve.

#### 🔄 Return<a id="🔄-return"></a>

[`ReceivingJobAndStatusResponse`](./visier_data_handling_python_sdk/pydantic/receiving_job_and_status_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/op/jobs/dispatching-jobs/:jobId/receiving-jobs` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visierdatahandling.data_and_job_handling.receiving_job_status`<a id="visierdatahandlingdata_and_job_handlingreceiving_job_status"></a>

After sending data to Visier, you may want to know the status of the receiving job and the associated tenant
 receiving jobs. A receiving job validates the transferred data and adds the transferred data to Visier's data
 store.

 Use this API to retrieve the receiving job status and summary of analytic tenant receiving jobs.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
receiving_job_status_response = visierdatahandling.data_and_job_handling.receiving_job_status(
    jobs=True,
    tenant_code="string_example",
    start=1,
    limit=1,
    receiving_job_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### jobs: `bool`<a id="jobs-bool"></a>

If \"true\", returns the status of receiving jobs spawned by the receiving job specified by jobId.

##### tenant_code: `str`<a id="tenant_code-str"></a>

The tenant code of the tenant you want to retrieve the receiving jobs for. Use this if you are only interested  in the results for one analytic tenant.

##### start: `int`<a id="start-int"></a>

The index to start retrieving results from, also known as offset. The index begins at 0.

##### limit: `int`<a id="limit-int"></a>

The number of job statuses to return per page.

##### receiving_job_id: `str`<a id="receiving_job_id-str"></a>

The jobId provided after sending data to Visier.

#### 🔄 Return<a id="🔄-return"></a>

[`ReceivingJobStatusResponse`](./visier_data_handling_python_sdk/pydantic/receiving_job_status_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/op/jobs/receiving-jobs/:receivingJobId` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visierdatahandling.data_and_job_handling.retrieve_data_uploads`<a id="visierdatahandlingdata_and_job_handlingretrieve_data_uploads"></a>

Use this API to retrieve the data uploads and whether they're included in one of:
 - A list of analytic tenants managed by you.
 - A single specified analytic tenant.
 - An upload job.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
retrieve_data_uploads_response = visierdatahandling.data_and_job_handling.retrieve_data_uploads(
    upload_job_id="string_example",
    tenant_code=1,
    limit=1,
    start=1,
    number_of_data_uploads=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### upload_job_id: `str`<a id="upload_job_id-str"></a>

The job ID of an upload job. Use this if you are interested in the data uploads for a specific upload job.

##### tenant_code: `int`<a id="tenant_code-int"></a>

The tenant code of a specific analytic tenant that you want to retrieve the data uploads for.

##### limit: `int`<a id="limit-int"></a>

The limit of analytic tenants to retrieve data uploads for. This parameter is not used if the tenantCode parameter is specified.

##### start: `int`<a id="start-int"></a>

The index to start retrieving results from, also known as offset. The index begins at 0.

##### number_of_data_uploads: `int`<a id="number_of_data_uploads-int"></a>

The maximum number of latest enabled data uploads to retrieve for each analytic tenant. The maximum value is 5.

#### 🔄 Return<a id="🔄-return"></a>

[`TenantDataUploadsListResponseDTO`](./visier_data_handling_python_sdk/pydantic/tenant_data_uploads_list_response_dto.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/op/data/uploads` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visierdatahandling.data_and_job_handling.start_extraction`<a id="visierdatahandlingdata_and_job_handlingstart_extraction"></a>

Use this API to generate extraction jobs for a list of analytic tenants or for the administrating tenant.
 This API creates a dispatching job that generates one extraction job per tenant. The extraction jobs retrieve
 data from your source systems through data connectors. The dispatching job is the "parent" of the extraction
 jobs and its job ID is returned in the response.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
start_extraction_response = visierdatahandling.data_and_job_handling.start_extraction(
    model={
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### model: [`StartExtractionModel`](./visier_data_handling_python_sdk/type/start_extraction_model.py)<a id="model-startextractionmodelvisier_data_handling_python_sdktypestart_extraction_modelpy"></a>


A form body key that contains a collection of key-value pairs.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`StartExtractionRequest`](./visier_data_handling_python_sdk/type/start_extraction_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`StartExtractionResponse`](./visier_data_handling_python_sdk/pydantic/start_extraction_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/op/data/startExtractAndLoad` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `visierdatahandling.data_and_job_handling.start_load`<a id="visierdatahandlingdata_and_job_handlingstart_load"></a>

This API starts the data load process for all analytic tenants included in the specified data files uploaded
 to the Visier SFTP server. On success, you receive a job ID that can be filtered and searched for within the
 Jobs room in Visier. This job ID is associated with the receiving job, and related to all processing jobs that
 spawn for each analytic tenant.

 With the job ID, you can also call the next two APIs to retrieve the status of the receiving job and the status
 list of all related processing jobs.

 **Prerequisite:** You must first obtain Visier's public encryption key and upload the source data files to Visier's
 SFTP server. Files must have a .zip.gpg extension, meaning the files are encrypted using the PGP protocol and compressed.

 Visier provides SFTP server credentials and instructions. You can find the encryption key at https://www.visier.com/pgp/visier.public.pgp.asc.
 After downloading the file, open the file in a text editor or by dragging it into your browser.

 **Note:**
  - To see the full status of all analytic tenant data loads, navigate to the Jobs room in a project.
  - For performance and efficiency, Visier requires that the uncompressed batch file size is below 5 GB and that no
    more than 5000 tenants are included in a batch.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
start_load_response = visierdatahandling.data_and_job_handling.start_load(
    model={
        "key": {
        },
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### model: [`DataLoadRequestModel`](./visier_data_handling_python_sdk/type/data_load_request_model.py)<a id="model-dataloadrequestmodelvisier_data_handling_python_sdktypedata_load_request_modelpy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DataLoadRequest`](./visier_data_handling_python_sdk/type/data_load_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`DataLoadResponse`](./visier_data_handling_python_sdk/pydantic/data_load_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/op/data/startload` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
