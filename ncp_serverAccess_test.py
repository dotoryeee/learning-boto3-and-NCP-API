# https://github.com/NaverCloudPlatform/ncloud-sdk-python/blob/master/lib/services/vserver/docs/V2Api.md#get_server_instance_list
import ncloud_vserver
from ncloud_vserver.api.v2_api import V2Api
from ncloud_vserver.model import get_server_instance_list_request
from ncloud_vserver.rest import ApiException

conf = ncloud_vserver.Configuration()
conf.access_key = "5724A942A8DBEDD50524"
conf.secret_key = "656D758405AED7944511EA27B4DF26E4272FF302"
REGION_CODE = "KR"

api = V2Api(ncloud_vserver.ApiClient(conf))

serverList = ncloud_vserver.GetServerInstanceListRequest(
    {"region_code": REGION_CODE, "vpc_no": 6817}
)

try:
    response = api.get_server_instance_list(get_server_instance_list_request)
    print(response)
except ApiException as e:
    print(f"ERROR OCCURRED: {e}")
