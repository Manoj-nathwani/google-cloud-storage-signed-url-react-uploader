import datetime
from google.oauth2.service_account import Credentials
from google.cloud import storage
from utils import settings

credentials=Credentials.from_service_account_info(
    settings.SERVICE_ACCOUNT_CREDENTIALS
)
storage_client = storage.Client(
    credentials=credentials
)

def get_upload_url(metadata, redirect_url):
    # see: https://bit.ly/2FaJ5sI
    fields = {
        'x-goog-meta-{}'.format(key): str(value)
        for key, value in metadata.items()
    }
    fields['success_action_redirect'] = redirect_url
    policy = storage_client.generate_signed_post_policy_v4(
        settings.BUCKET_NAME,
        '${filename}',
        expiration=datetime.timedelta(minutes=60),        
        fields=fields
    )
    return policy