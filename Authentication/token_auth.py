"""
Token authentication 
"""

"Problem that token authentication solves"

"Basic Authentication"
# sends username and password on every request that is risky 
# no logout = as no real login happens and nothing stored in the server side to verify so the backend only verifies the credentials sent over the request and response accordig to that 

"Session Authentication"
"""
session authentication actually logs in with username and password then server verifies that and store a session id in the memory and sends a session id cookie and browser sends that cookie on every request then server looks up on the session and allow access .
"""
# session authentication is not mobile friendly


"Token Authentication "
"client sends credentials backend verifies it and create a token and sends it to cleint client store it and sends that token with request to get access."

# disadvantages
"no expiration by default thats why jwtToken prefers"
"not ideal for large apps"