def upload_data_to_blob(
    filepath: Union[str, bytes],
    container_name: str,
    blob_name: str,
    sas_expiration_time: int = 10,
    overwrite: bool = False,
) -> str:
    """Upload data to Azure Blob Storage.

    Args:
        filepath (Union[str,bytes]): Filepath or bytes to upload.
        container_name (str): Name of the container to upload to.
        blob_name (str): Name of the blob to upload to.
        connection_string (str): Connection string for the storage account.
        sas_expiration_time (int): Expiration time for the SAS token in hours. Defaults to 10 hours
    Returns:
        str: URL of the uploaded blob.
    """
    if not isinstance(filepath, (str, bytes)):
        raise ValueError(
            f"filepath must be a string or bytes object, not {type(filepath).__name__}"
        )
    if isinstance(filepath, str):
        with open(filepath, "rb") as file:
            filepath = file.read()

    connection_string = get_connection_string()
    if not connection_string:
        raise ValueError(
            "Connection string not found. Please set the environment variable 'AZURE_STORAGE_CONNECTION_STRING'"
        )
    blob_service_client: BlobServiceClient = BlobServiceClient.from_connection_string(
        connection_string
    )
    try:
        blob_service_client.create_container(container_name)
    except ResourceExistsError:
        logging.info("Container %s already exists", container_name)
    container_client: ContainerClient = blob_service_client.get_container_client(
        container_name
    )
    blob_client: BlobClient = container_client.get_blob_client(blob_name)
    if overwrite:
        blob_client.upload_blob(filepath, overwrite=True)
    else:
        try:
            blob_client.upload_blob(filepath)
        except ResourceExistsError as exc:
            raise ResourceExistsError(
                f"Blob {blob_name} already exists. Use this method with overwrite if you want to overwrite an existing blob"
            ) from exc
    sas_token = generate_account_sas(
        blob_service_client.account_name,
        account_key=blob_service_client.credential.account_key,
        resource_types=ResourceTypes(container=True),
        permission=AccountSasPermissions(read=True, write=True, delete=True, list=True),
        expiry=datetime.utcnow() + timedelta(hours=sas_expiration_time),
    )
    return f"{blob_client.url}?{sas_token}"