from __future__ import print_function
from ncp_serverAccess_test import REGION_CODE
import ncloud_vserver
from ncloud_vserver.rest import ApiException

REGION_CODE = "KR"
IMAGE_CODE = "SW.VSVR.OS.LNX64.CNTOS.0708.B050"  # CentOS 7.8 64bit

conf = ncloud_vserver.Configuration()
conf.access_key = "5724A942A8DBEDD50524"
conf.secret_key = "656D758405AED7944511EA27B4DF26E4272FF302"
api_instance = ncloud_vserver.V2Api(ncloud_vserver.ApiClient(conf))
get_server_product_list_request = ncloud_vserver.GetServerProductListRequest(
    {"region_code": REGION_CODE, "server_image_product_code": IMAGE_CODE}
)

try:
    api_response = api_instance.get_server_product_list(get_server_product_list_request)
    print(api_response)
except ApiException as e:
    print(f"ERROR OCCURED : {e}")
