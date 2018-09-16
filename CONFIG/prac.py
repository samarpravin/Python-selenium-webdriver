import re
import json

with open("C:\Api_Automation\Python_Automation_Framework\CONF\commonconfig.json","r") as f:
    config_json=json.load(f)
    print config_json
    replace_string=config_json["XPATH"]["dropdwonlandingpage_increment"]
    print  replace_string
    for i in range(1,10):
        v=re.sub("~",str(i),replace_string)
        print v

import json

with open("C:\Api_Automation\Python_Automation_Framework\CONF\commonconfig.json", "r") as f:
    config_json = json.load(f)
    print config_json["URL"]["facebook"]