import urllib3, requests, json, sys

# Disable SSL Warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Create verification function for authrntication
def Verf_Res(Res):
    if b'<html>' in Res.content:
        print("Response Test Failed")
        sys.exit(0)

# Create verification function for resonse data
def Verf_Data(Res):
    # Check entire response 
    if not isinstance(Res,dict):
        print("Main Response Not Dict")
        sys.exit(0)
    # Check if there is a data
    elif "data" not in Res:
        print("Data Part does not exist")
        sys.exit(0)
    elif not Res["data"]:
        print("Data Part is empty")
        sys.exit(0)


# Host Creds
UserName = "admin"
PassWord = "C1sco12345"
Headers={'Accept': 'application/json',
        'Content-Type': 'application/json'}

# URL for auth, key=j
URL_Login = "https://10.10.20.90/j_security_check"

# PayLoad with creds
Body_Login = {"j_username": UserName,"j_password": PassWord}

# keeps connection up with same login creds
Sess_Login = requests.session()

# Login using Post
Res_Login = Sess_Login.post(url=URL_Login, data=Body_Login, verify=False)

# Use the verification function on the returned response
Verf_Res(Res_Login)

# URL for Token
URL_Token = "https://10.10.20.90/dataservice/client/token"

# Get Token
Res_Token = Sess_Login.get(url=URL_Token)

# Use the verification function on the returned Token
Verf_Res(Res_Token)

Sess_Login.headers['X-XSRF-TOKEN']=Res_Token.text


##################  end of auth ##################

URL_Interfaces = 'https://10.10.20.90/dataservice/statistics/interface'

Res_Interfaces = Sess_Login.get(url=URL_Interfaces, verify=False).json()

print (json.dumps(Res_Interfaces, indent=2))

# Verf_Data(Res_Interfaces)

# print (json.dumps(Res_Interfaces["data"], indent=2))