print("http://%s:%s@0.0.0.0:9001/1" % (ProjectKey.objects.first().public_key, ProjectKey.objects.first().secret_key))
