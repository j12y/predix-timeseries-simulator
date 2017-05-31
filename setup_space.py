
import predix.admin.uaa
import predix.admin.timeseries

# You can customize these if you feel fancy
admin_secret = 'voltaged'
client_id = 'voltaged'
client_secret = 'voltaged'
manifest_path = 'manifest.yml'

# Create a UAA instance and a client for our application
uaa = predix.admin.uaa.UserAccountAuthentication()
uaa.create(admin_secret)
uaa.create_client(client_id, client_secret)

# Create a Time Series instance and grant access to our client
ts = predix.admin.timeseries.TimeSeries()
ts.create()
ts.grant_client(client_id)

# Save everything in a manifest for convenient access
uaa.add_to_manifest(manifest_path)
uaa.add_client_to_manifest(client_id, client_secret, manifest_path)
ts.add_to_manifest(manifest_path)
